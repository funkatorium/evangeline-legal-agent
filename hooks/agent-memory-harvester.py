#!/usr/bin/env python3
"""SubagentStop hook: harvest MEMORY blocks from completed subagent transcripts.

Reads the subagent's JSONL transcript, identifies the agent by the
first `agents/memory/<name>/_universal.md` mention (which appears in
each agent's system prompt), extracts `- [YYYY-MM-DD] ...` learning
lines from the agent's text output, dedupes against the existing
memory file, and appends new entries.

Always exits 0 — a memory write failure must never block a session.

AUTO-PUSH (opt-in)
------------------
After writing new learnings the hook can auto-commit and push the memory
repository to a configured private git remote. This is disabled by default.

To enable, set AGENT_MEMORY_AUTOPUSH=1 before Claude Code launches, and make
~/.claude/agents/memory a git repo with origin/main pointing at your private
learning repo. If git, credentials, or the repo are missing, the hook skips the
push and still exits 0.
"""
import fcntl
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

MEMORY_LINE = re.compile(r'^- \[20\d{2}-\d{2}-\d{2}\].+$', re.MULTILINE)
AGENT_PATH = re.compile(r'agents/memory/([a-z][a-z0-9_-]+)/_universal\.md')
MEMORY_DIR = Path.home() / '.claude' / 'agents' / 'memory'


def git_autopush(memory_file: Path) -> None:
    """Fire-and-forget commit/push for the private agent-memory repo.

    Security posture: disabled by default; stages only the memory file that was
    just written, not arbitrary files in the repo. All failures are swallowed so
    memory persistence never blocks or breaks the agent pipeline.
    """
    if os.environ.get('AGENT_MEMORY_AUTOPUSH') != '1':
        return
    if not (MEMORY_DIR / '.git').is_dir():
        return

    try:
        rel_path = memory_file.relative_to(MEMORY_DIR)
    except ValueError:
        return

    timestamp = datetime.now(tz=timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    commit_msg = f'auto: agent learning {rel_path} {timestamp}'

    # Detached child process keeps SubagentStop latency low. We intentionally
    # stage only the touched file; Michael's own learning says automated
    # `git add -A` is how secrets end up in the wrong place.
    cmd = (
        f'cd {str(MEMORY_DIR)!r} && '
        f'git add -- {str(rel_path)!r} && '
        f'if git diff --cached --quiet -- {str(rel_path)!r}; then '
        f'exit 0; '
        f'else git commit -m {commit_msg!r} && git push origin main; '
        f'fi'
    )
    try:
        subprocess.Popen(
            ['sh', '-c', cmd],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
        )
    except Exception as exc:  # pragma: no cover — never block on push failure
        print(f'[memory-harvester] autopush skipped: {exc}', file=sys.stderr)


def resolve_agent_name(transcript_path, text_fallback):
    """Determine agent name from the .meta.json sibling, falling back to text.

    Claude Code writes a `<id>.meta.json` next to each subagent transcript with
    `{"agentType": "fischer", ...}`. That's the authoritative signal. The
    transcript path the hook receives is usually a symlink in /tmp/.../tasks/
    pointing to the real .jsonl in ~/.claude/projects/<session>/subagents/.
    """
    try:
        real = os.path.realpath(transcript_path)
        meta_path = re.sub(r'\.jsonl$', '.meta.json', real)
        if meta_path != real and os.path.exists(meta_path):
            with open(meta_path, encoding='utf-8') as fh:
                meta = json.load(fh)
            agent_type = meta.get('agentType')
            if isinstance(agent_type, str) and agent_type:
                return agent_type
    except (OSError, json.JSONDecodeError):
        pass

    # Fallback: agent system prompts reference their own memory path
    match = AGENT_PATH.search(text_fallback)
    if match:
        return match.group(1)
    return None


def collect_text(transcript_path):
    """Collect only assistant-authored text. User-role messages (prompts,
    system reminders) can contain MEMORY-block-shaped examples we must not
    harvest."""
    chunks = []
    with open(transcript_path, encoding='utf-8', errors='replace') as fh:
        for raw in fh:
            try:
                entry = json.loads(raw)
            except json.JSONDecodeError:
                continue
            msg = entry.get('message') or {}
            role = msg.get('role') or entry.get('type')
            if role != 'assistant':
                continue
            content = msg.get('content')
            if isinstance(content, str):
                chunks.append(content)
            elif isinstance(content, list):
                for part in content:
                    if isinstance(part, dict) and part.get('type') == 'text':
                        chunks.append(part.get('text', ''))
    return '\n'.join(chunks)


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return

    transcript = payload.get('agent_transcript_path') or payload.get('transcript_path')
    if not transcript or not os.path.exists(transcript):
        return

    text = collect_text(transcript)
    if not text:
        return

    agent = resolve_agent_name(transcript, text)
    if not agent:
        return

    memory_file = MEMORY_DIR / agent / '_universal.md'
    if not memory_file.exists():
        return

    candidates = MEMORY_LINE.findall(text)
    if not candidates:
        return

    existing = memory_file.read_text(encoding='utf-8', errors='replace')
    # Dedupe both against existing file content and within this batch
    seen: set[str] = set()
    new_entries: list[str] = []
    for line in candidates:
        line = line.rstrip()
        if line in existing or line in seen:
            continue
        seen.add(line)
        new_entries.append(line)

    if not new_entries:
        return

    with memory_file.open('a', encoding='utf-8') as fh:
        # Advisory lock to handle concurrent SubagentStop firings on the same file
        fcntl.flock(fh.fileno(), fcntl.LOCK_EX)
        try:
            for entry in new_entries:
                fh.write(entry + '\n')
        finally:
            fcntl.flock(fh.fileno(), fcntl.LOCK_UN)

    print(
        f'[memory-harvester] {agent}: appended {len(new_entries)} learning(s)',
        file=sys.stderr,
    )

    git_autopush(memory_file)


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:  # pragma: no cover — never block on harvester failure
        print(f'[memory-harvester] error: {exc}', file=sys.stderr)
    sys.exit(0)
