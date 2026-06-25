<p align="center">
  <img src="./assets/banner.png" alt="Evangeline — Legal Counsel by The Funkatorium" width="800" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Montserrat&weight=500&size=22&pause=1200&color=D4AF37&center=true&vCenter=true&width=900&lines=Read+the+clause.+Then+read+what+it's+hiding.;88+learnings+from+production+legal+reviews.+Four+jurisdictions.;Diagnosis+only.+Because+the+agent+that+finds+the+gap+shouldn't+draft+the+fix." alt="Evangeline tagline" />
</p>

<p align="center">
  <a href="https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/badge/License-Apache%202.0-D4AF37?style=flat" alt="License: Apache 2.0" /></a>
  <img src="https://img.shields.io/badge/Claude-Opus-000000?style=flat&logo=anthropic&logoColor=white" alt="Claude Opus" />
  <img src="https://img.shields.io/badge/Framework-Claude%20Code-000000?style=flat&logo=anthropic&logoColor=white" alt="Claude Code" />
  <img src="https://img.shields.io/badge/Learnings-88-brightgreen?style=flat" alt="88 Learnings" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Germany-BGB%20%2F%20HGB-blue?style=flat" alt="Germany: BGB / HGB" />
  <img src="https://img.shields.io/badge/United%20States-UCC%20%2F%20FCPA-red?style=flat" alt="US: UCC / FCPA" />
  <img src="https://img.shields.io/badge/Nigeria-CAMA%202020-green?style=flat" alt="Nigeria: CAMA 2020" />
  <img src="https://img.shields.io/badge/Uganda-Companies%20Act%202012-orange?style=flat" alt="Uganda: Companies Act 2012" />
</p>

# Evangeline -- Legal Counsel Agent

The gap between what a contract says and what it means is where people get hurt.

Evangeline is a legal counsel agent for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) that reads contracts across four jurisdictions, maps structural gaps against a 9-section completeness checklist, and tells you exactly what is missing, what is dangerous, and what specific clause language will fix it -- then hands the framework to your drafter (human or agent) while she watches what comes back. The analysis and the drafting stay in separate hands.

Every review she runs makes the next one sharper. Evangeline carries 99 accumulated learnings from production legal reviews -- treaty statuses verified, jurisdiction-specific gotchas documented, clause patterns tested through real-world contract review across civil-law and common-law jurisdictions. She remembers what she found.

<p align="center">
  <img src="./assets/spec-sheet.gif" alt="Evangeline -- Capability Spec Sheet" width="600" />
</p>

<br>

<p align="center">
  <img src="./assets/evangeline-modern-spec.png" alt="Evangeline -- Modern Professional Turnaround" width="600" />
</p>

## Where She Comes From

The name is from Longfellow's *Evangeline, A Tale of Acadie* (1847) -- a woman displaced across legal jurisdictions and institutional systems, who persisted through every one of them to find what belonged to her.

Evangeline's lineage is Louisiana: the only place in the United States where Napoleonic civil law and English common law share one courthouse. French *Code Civil* reasoning and Anglo-American precedent law sit in the same courtroom. That is where she learned to navigate between legal traditions -- and it is why four jurisdictions feel like one.

She moves between German civil law (BGB, the most refined civil code in Europe), American common law (state-by-state, case-by-case), and the British-inherited common law systems of Nigeria and Uganda, because she was born where these traditions already overlap.

---

## Memory That Compounds

After every review, Evangeline emits a `MEMORY:` block with new learnings. A SubagentStop hook (`hooks/agent-memory-harvester.py`, installed alongside the agent) automatically harvests these blocks into `~/.claude/agents/memory/evangeline/_universal.md` -- the agent only thinks, the hook persists. The hook can also auto-commit and push the touched memory file to your own private `agent-memory` repo, so learnings survive across machines without manual babysitting. When connected to [MUSE Brain](https://github.com/funkatorium/muse-brain), those same learnings sync as brain observations that never decay. Each review sharpens the next: jurisdiction-specific patterns recognized instantly, treaty statuses tracked, clause patterns validated against real outcomes.

Evangeline's 99 learnings cluster into specializations that no template library has:

#### International Tax & Treaty Intelligence (13 learnings)
- Germany-Nigeria DTA does NOT EXIST -- confirmed via FIRS listing and cross-references
- Germany-Uganda DTA does NOT EXIST -- Uganda has DTAs with 9 countries; Germany is not among them
- No DTA = full domestic withholding both directions. Germany: 15.825% (section 50a EStG). Nigeria: 10% WHT
- Germany-UK DTA (2010 + 2021 Protocol): 0% withholding on royalties, 0% on interest -- robust treaty
- German Quellensteuer (section 50a EStG) categories, rates, and structuring implications for creative partnerships
- Cross-border VAT reverse charge mechanisms for Germany-UK B2B services
- Late payment interest rate: 9pp above base rate for B2B (section 288 BGB), 5pp defensible for sole traders

#### Data Protection Across Borders (9 learnings)
- Nigeria NDPA 2023 replaced NDPR: no business contact exemption, safeguards clause is practical minimum
- Uganda DPPA 2019: consent + contractual safeguards for cross-border, PDPO actively enforcing
- UK GDPR adequacy renewed December 2025, valid to December 2031 -- no SCCs needed for Germany-UK
- Lightweight DPA clause vs full Art.28 GDPR DPA: when each is appropriate
- Fallback clauses for adequacy lapse scenarios (90-day implementation window)

#### Compliance & Anti-Corruption (12 learnings)
- FCPA applies to US persons (citizens, residents, US-organized entities) worldwide regardless of business nexus, $100K + 5 years per violation
- UK Bribery Act 2010 is stricter than FCPA -- no facilitation payment exception whatsoever
- Uganda Protection of Sovereignty Act 2026 (signed May 17): foreign funding >UGX 400M requires ministerial declaration, 20-year imprisonment penalty
- Uganda NGO Act 2016: permit validity, annual requirements, special obligations, deregistration triggers
- Post-Brexit UK sanctions regime (SAMLA 2018): autonomous lists that may diverge from EU sanctions
- IR35 off-payroll working rules: do not apply when end-client is small non-UK entity

#### Contract Lifecycle Management (18 learnings)
- CLM industry-standard 9-stage lifecycle with pre/post-execution split
- Contract Management Maturity Model (CMMM): 5 levels, 6 Key Process Areas, scoring methodology
- WorldCC Contract Management Standard 4th Edition (2025): 3 phases, 7 principles, 5 domains, 20 competencies
- Obligation register fields, seven-step management process, bidirectional tracking
- Auto-renewal trap: 60% of supplier contracts auto-renew without buyer knowledge
- Amendment vs addendum vs restatement vs side letter: when to use which
- Version control and consolidated "current state" requirements for legal documents

#### Negotiation Frameworks (8 learnings)
- Harvard PON principled negotiation: four principles applied to clause-level bargaining
- BATNA/ZOPA/Reservation Price: the three pillars of negotiation preparation
- Chris Voss tactical empathy applied to contract negotiation -- labeling, accusation audit, calibrated questions
- Never split the difference on liability caps, IP ownership, or termination rights
- WorldCC 2024 Most Negotiated Terms: liability limitation has been number one for over a decade
- The disconnect between negotiation priorities and business outcomes is the top challenge in commercial contracting

#### Risk Assessment & Vendor Management (11 learnings)
- Contract risk matrix (Likelihood x Impact), RAG thresholds, four-phase methodology
- Five scoring dimensions: monetary exposure, compliance, reputational, operational dependency, legal complexity
- Four risk allocation strategies: transfer, retention, sharing, avoidance
- Four-tier SLA escalation framework and vendor performance scorecards
- Progressive penalty structures and German AGB-Kontrolle limits on disproportionate penalties

#### IP & Creator Protection (6 learnings)
- Berne Convention practical enforceability: register with NCC in Nigeria for enforcement weight
- Nigeria Copyright Act 2022: AI-assisted works protectable with sufficient human contribution
- AI-generated content IP clause recommended for all agreements: directing party is author
- German Urheberrecht automatic protection vs registration-based systems

#### Template Architecture & Professional Standards (12 learnings)
- Three-tier clause library: preferred, acceptable, last resort -- with automatic triggers
- Contract playbook structure: preferred language, fallback, walkaway, escalation, counterparty patterns
- "No project yet" master agreements: use Appendix (non-binding menu) not Annex (binding obligations)
- Entity flexibility clauses for uncertain counterparty structures
- Currency clause requirements for cross-border agreements (ECB reference rate)
- WorldCC and NCMA certification frameworks, professional vocabulary fluency

#### Contract Analytics (10 learnings)
- Top 11 contract management KPIs with industry benchmarks
- WorldCC value erosion benchmark: average 9.2% of annual revenue lost to poor contract management
- CLM platform landscape 2025-2026: Ironclad, Agiloft, Juro, Leah, and their differentiators
- Five priority dashboard metrics for immediate impact
- Post-award contract management: 5 core functions where 70%+ of value is realized or lost
- Contract closeout checklist: 9-step process including HGB section 257 retention requirements

---

## Four Operating Modes

| Mode | When | Output |
|------|------|--------|
| **Scan** | Quick check, single clause, "is this enforceable?" | CLEAR with notes, or NEEDS WORK with prioritized findings |
| **Review** | Full contract analysis, "is this safe to sign?" | Findings table + risk assessment + recommended amendments |
| **Research** | Jurisdiction question, treaty status, "how does German law handle X?" | Research brief with citations, comparative analysis, practical recommendations |
| **Framework** | New partnership, "what should this contract include?" | Article-by-article structure with legal rationale, placeholder language, negotiation map |

## Diagnosis-Only Architecture

Evangeline researches. You draft. Evangeline re-reviews.

A contract clause drafted by the same agent that identified the gap has no second pair of eyes on it. The analysis and the drafting belong in separate hands. The accountability chain is explicit: **identify gap --> draft clause --> review the draft --> finalize**.

**Standalone:**
```
Evangeline (analyze) --> You (draft) --> Evangeline (re-review)
```

**With a multi-agent squad** *(our production workflow):*
```
Evangeline (analyze) --> [Drafter] (write clause) --> [Reviewer] (review) --> Evangeline (re-review)
```

In our workflow: Evangeline analyzes, produces a framework, and hands it to the document drafter. The drafter writes. Evangeline reviews what comes back. The framework IS the finding -- specific, cited, with exact clause language recommendations and legal basis for each.

## The 9-Section Structural Completeness Checklist

Every B2B agreement Evangeline reviews is measured against this checklist. Missing sections are flagged by severity.

1. **Identity & Formation** -- parties, governing law, effective date, nature of relationship (Statusfeststellung)
2. **Scope & Obligations** -- what each party provides/receives, exclusions, representation rights, exclusivity
3. **Intellectual Property** -- pre-existing IP, work classification, licensing terms, sublicensing, moral rights
4. **Financial** -- payment model, terms, late payment (section 288 BGB), expenses, audit rights, tax cooperation
5. **Data & Confidentiality** -- confidentiality scope, GDPR/NDPA/DPPA compliance, cross-border transfers, SCCs
6. **Term & Exit** -- duration, termination by notice (Kundigungsfrist), termination for cause, survival clauses
7. **Disputes** -- good faith discussion, mediation, arbitration or litigation, dispute resolution spirit
8. **Protection Clauses** -- liability cap, indemnification, force majeure, anti-corruption, sanctions, assignment
9. **Structural** -- severability (Salvatorische Klausel), entire agreement, amendment mechanism, Schriftform, annual review

Each finding maps to the applicable legal basis -- a statute, a regulation, a treaty clause, a common-law precedent. Evangeline does not flag things on vibes.

## Jurisdiction Intelligence

Evangeline carries deep knowledge of four legal systems and the international frameworks that bridge them:

**Germany (civil law -- BGB, HGB, StGB)**
BGB contract law and liability. HGB commercial obligations. Section 288 BGB late payment interest. Section 126b BGB Textform. Salvatorische Klausel. Statusfeststellung for B2B classification. GDPR/DSGVO. Entity types from Einzelunternehmen to AG.

**United States (common law, federal + state)**
UCC for goods. Common law contract formation and consideration. FCPA anti-corruption (applies to US persons worldwide). Export controls (EAR, ITAR). State law variation across Delaware, California, New York. FATCA, tax treaties, IP under Copyright Act and Lanham Act.

**Nigeria (common law, British-inherited + constitutional)**
CAMA 2020 company formation. Copyright Act 2022 (AI content provisions). NDPA 2023 data protection. ICPC/EFCC anti-corruption. Foreign investment rules. No DTA with Germany.

**Uganda (common law, British-inherited + constitutional)**
Companies Act 2012. NGO Act 2016 (permit validity, annual compliance). Data Protection and Privacy Act 2019. Protection of Sovereignty Act 2026. Investment Code Act. No DTA with Germany.

**International Frameworks**
ICC Arbitration. UNCITRAL. Berne Convention. TRIPS. New York Convention. Standard Contractual Clauses. Double Taxation Agreements (status verified per corridor).

## Contract Lifecycle Management

Beyond clause-level review, Evangeline understands the full contract lifecycle:

- **CLM Frameworks** -- WorldCC Contract Management Standard, CMMM maturity assessment, 9-stage lifecycle management
- **Negotiation** -- Harvard PON principled negotiation (BATNA/ZOPA), Chris Voss tactical empathy, WorldCC Most Negotiated Terms benchmarks
- **Obligation Tracking** -- obligation register design, bidirectional monitoring, seven-step management process, auto-renewal detection
- **Amendment Management** -- amendment vs addendum vs restatement decision framework, version control for legal documents, consolidated "current state" requirements
- **Risk Assessment** -- risk matrix scoring (Likelihood x Impact, RAG thresholds), four-phase methodology, five scoring dimensions, risk allocation strategies
- **Template Governance** -- three-tier clause library (preferred/acceptable/last resort), contract playbooks, deviation approval workflows
- **Analytics** -- 11 KPIs with industry benchmarks, value erosion tracking (WorldCC: 9.2% average revenue loss), post-award management functions

## Additional Capabilities

- **Comparative Legal Analysis** -- how each jurisdiction handles the same legal question, with practical recommendations on which approach to adopt
- **Treaty Status Verification** -- confirmed existence (or non-existence) of bilateral treaties, with fallback strategies when no treaty exists
- **Tax Corridor Mapping** -- withholding tax rates, double taxation risk assessment, VAT reverse charge applicability (not tax advice -- flag and recommend Steuerberater/CPA)
- **Entity Structuring Awareness** -- when Einzelunternehmen reaches GmbH conversion thresholds, foreign entity registration requirements, entity flexibility drafting
- **Cross-Border Data Transfer Architecture** -- SCCs, adequacy decisions, consent mechanisms, lightweight vs full DPA selection
- **Professional Vocabulary** -- speaks CLM fluently (BATNA, ZOPA, RAG, ACV, MNT, KPA, value erosion, obligation register, compliance drift, clause library, redline, turn frequency, cycle time)

## Installation

Copy the agent definition and supporting files into your Claude Code configuration:

```bash
# Agent spec
cp evangeline.md ~/.claude/agents/evangeline.md

# Memory directory (Evangeline learns here)
mkdir -p ~/.claude/agents/memory/evangeline

# Memory harvester hook (makes the "memory that compounds" claim reliable)
cp hooks/agent-memory-harvester.py ~/.claude/hooks/agent-memory-harvester.py
chmod +x ~/.claude/hooks/agent-memory-harvester.py
```

Then register the harvester in your `~/.claude/settings.json` under `hooks.SubagentStop`:

```json
{
  "hooks": {
    "SubagentStop": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /Users/YOU/.claude/hooks/agent-memory-harvester.py",
            "timeout": 20
          }
        ]
      }
    ]
  }
}
```

The hook is generic -- it routes by agent name from the SubagentStop event metadata, so the same script works for every agent in your squad. Restart your Claude Code session for the hook to take effect.

### Optional: private learning autopush

For durable cloud sync, make `~/.claude/agents/memory` its own git repo with a private remote, then enable autopush in the hook command:

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

Then update the hook command:

```json
"command": "AGENT_MEMORY_AUTOPUSH=1 python3 /Users/YOU/.claude/hooks/agent-memory-harvester.py"
```

Autopush is fire-and-forget: if git is unavailable, credentials are missing, or there is nothing new to commit, the hook skips the push and never blocks the agent pipeline. It stages only the touched memory file, not arbitrary files. Full setup: [Agent Memory Autopush](docs/AGENT_MEMORY_AUTOPUSH.md).

> **Scope note:** This hook uses Claude Code's `SubagentStop` lifecycle event. Codex agents have a different lifecycle, but they write to the same private `agent-memory` substrate once configured. MUSE Brain's Agent Learning Bridge then ingests those memory files as cloud observations, making the loop substrate-agnostic.

### Invoke

```
/evangeline                 # Direct invocation
```

Or let your orchestrator dispatch Evangeline automatically when legal-relevant work is detected -- new partnerships, contract drafting, compliance questions, cross-border transactions, IP licensing, entity structuring.

### With MUSE Brain (Recommended)

Evangeline learns locally by default. For cloud-based persistent memory that survives across machines, connect her to [MUSE Brain](https://github.com/funkatorium/muse-brain) (CC-BY-NC-SA 4.0). When connected, her learnings become brain observations with charge and grip -- iron-grip legal learnings never decay. The integration is documented in the agent spec (`evangeline.md` --> Brain Entity Integration).

## File Structure

```
evangeline-legal-agent/
├── evangeline.md                       # Agent definition (identity + protocol)
├── references/                         # Jurisdiction intelligence, treaty databases,
│                                       # legal framework references (coming soon)
├── skills/                             # Legal review procedures, checklist
│                                       # definitions, operating modes (coming soon)
├── memory/
│   └── _universal.md                   # 99 accumulated learnings (ships with Evangeline)
├── hooks/
│   └── agent-memory-harvester.py       # SubagentStop memory harvester + optional autopush
├── docs/
│   └── AGENT_MEMORY_AUTOPUSH.md        # Private learning repo setup
├── examples/                           # Production review examples (coming soon)
├── assets/
│   ├── banner.png                      # GitHub banner
│   ├── spec-sheet.gif                  # Animated capability sheet
│   └── evangeline-modern-spec.png      # Modern professional turnaround
├── LICENSE                             # Apache 2.0 (tech) + character IP (proprietary)
└── README.md
```

## The Funkatorium

Evangeline is the second agent released from the Operations Squad -- a team of specialized agents where each has a defined role, personality, and craft. The first release was [Michael](https://github.com/funkatorium/michael-security-agent) (security specialist, Builder Squad). The rest of the squad is coming. When they arrive, Evangeline already knows how to work with them.

Built by [Rook Sch&auml;fer](https://github.com/The-Funkatorium) and [Falco Sch&auml;fer](https://linktr.ee/musestudio95) at [The Funkatorium](https://funkatorium.org).

## License

**Technical capabilities** (legal checklist, jurisdiction mappings, contract lifecycle frameworks, memory format, reference intelligence) -- Apache 2.0. Use them, fork them, build on them.

**Evangeline as a character** (identity, personality, voice, backstory, visual assets, lore) -- proprietary, protected under German intellectual property law (Urheberrechtsgesetz, UrhG) as a literary character. You can use Evangeline as shipped. You cannot create derivative characters based on her identity.

[MUSE Brain](https://github.com/funkatorium/muse-brain) is CC-BY-NC-SA 4.0.
