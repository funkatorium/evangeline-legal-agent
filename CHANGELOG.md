# Changelog

All notable changes to Evangeline Legal Agent are documented here.

## [1.2.0] — 2026-06-30

### Added

- **Legal Deploy Guard** (`hooks/legal-deploy-guard.sh`) — a reusable shell hook that detects changes to AGB, Datenschutz, Widerrufsbelehrung, or Impressum content since the last deploy tag and forces acknowledgment before the deploy can proceed. Designed as an ADHD accommodation: the gate cannot be skipped. Source it in your `deploy.sh` or run standalone. Includes German law context (BGB, DSGVO notification requirements).

- **AGB drafting capability** — Evangeline can now produce research-grade bilingual (DE/EN) Allgemeine Geschäftsbedingungen for German Einzelunternehmen operating digital/SaaS products, covering:
  - Kleinunternehmerregelung (§19 UStG) pricing disclosures
  - PAngV §1 gross price requirements for B2C
  - Open-source license mapping per product (Apache 2.0, MIT, CC-BY-NC-SA 4.0)
  - §312g BGB consumer contract requirements
  - Haftungsbeschränkung (liability limitation) under AGB-Kontrolle (§§305–310 BGB)

- **Widerrufsbelehrung drafting capability** — bilingual withdrawal notice compliant with §355 BGB, including:
  - Muster-Widerrufsformular (model withdrawal form per Anlage 2 zu Art. 246a §1 Abs. 2 EGBGB)
  - Special notices for digital content, services, and free content
  - §356a BGB Widerrufsbutton awareness (new law, effective 2026-06-19)
  - Separate consent checkbox guidance for immediate-delivery digital content

### Fixed

- 96 learnings (8 new from AGB/Widerrufsbelehrung production work)

## [1.1.0] — 2026-06-20

### Changed

- Five-jurisdiction navigation with updated badges
- Deduplicated memory (99 → 88 learnings after removing duplicates)
- Corrected frontmatter

## [1.0.0] — 2026-06-20

### Added

- Initial public release
- Agent definition with four operating modes (Scan, Review, Research, Framework)
- 88 accumulated learnings from production legal reviews
- Four-jurisdiction intelligence (Germany, US, Nigeria, Uganda)
- 9-section structural completeness checklist
- Contract Lifecycle Management frameworks
- SubagentStop memory harvester hook with optional autopush
- Apache 2.0 license (technical capabilities)

[1.2.0]: https://github.com/falcoschaefer99-eng/evangeline-legal-agent/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/falcoschaefer99-eng/evangeline-legal-agent/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/falcoschaefer99-eng/evangeline-legal-agent/releases/tag/v1.0.0
