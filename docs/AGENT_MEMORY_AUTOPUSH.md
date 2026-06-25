# Agent Memory Autopush

Evangeline learns locally through the `SubagentStop` memory harvester. Autopush adds a durable cloud leg: after the hook appends a new learning, it can commit and push the touched memory file to a private git repo you control.

The public Evangeline repo ships the mechanism. Your actual learnings should live in your own private memory repo.

## What gets pushed

By default, nothing. Autopush is opt-in.

When enabled, the hook stages only the file it just changed, for example:

```text
~/.claude/agents/memory/evangeline/_universal.md
```

It does not stage arbitrary files with `git add -A`.

## Setup

Create or choose a private repo for agent memory. Then initialize your local memory directory as its own git repo:

```bash
mkdir -p ~/.claude/agents/memory/evangeline
cd ~/.claude/agents/memory

git init
git branch -M main
git remote add origin git@github.com:YOUR_ORG/agent-memory.git

touch evangeline/_universal.md
git add evangeline/_universal.md
git commit -m "init: evangeline agent memory"
git push -u origin main
```

## Enable the hook

Register Evangeline's harvester in `~/.claude/settings.json` and set `AGENT_MEMORY_AUTOPUSH=1` in the command:

```json
{
  "hooks": {
    "SubagentStop": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "AGENT_MEMORY_AUTOPUSH=1 python3 /Users/YOU/.claude/hooks/agent-memory-harvester.py",
            "timeout": 20
          }
        ]
      }
    ]
  }
}
```

Restart Claude Code after changing hook settings.

## Behavior

- Fire-and-forget: push happens in a detached background process.
- Fail-open for sessions: git/network/auth failures never block the agent pipeline.
- Private-by-configuration: the hook only pushes to the remote you configured on `~/.claude/agents/memory`.
- Scoped staging: only the touched agent memory file is staged.

## Verify

After an Evangeline run that emits a `MEMORY:` learning:

```bash
git -C ~/.claude/agents/memory status --short
git -C ~/.claude/agents/memory log --oneline -5
git -C ~/.claude/agents/memory remote -v
```

If no commit appears, check:

1. `AGENT_MEMORY_AUTOPUSH=1` is present in the hook command or shell environment.
2. `~/.claude/agents/memory` is a git repo.
3. `origin` points to a repo you can push to.
4. Branch is `main`.

## With MUSE Brain

Autopush is the durable raw-learning layer. MUSE Brain sync is the synthesis layer: use the Agent Learning Bridge in MUSE Brain to ingest memory files as reviewed brain observations.
