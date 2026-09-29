# Changelog

All notable changes to this repo, newest first. I use simple version tags
(`v1.0`, `v1.1`, ...) and plain-language entries.

## [v1.1] - 2026-09-29

A documentation and reproducibility release. No new projects, no new
experiments; the work went into depth instead.

**Added**

- Rewrote the root README: fixed project counts (17 projects plus 2
  companion case studies), added project types (technical, analyst, case
  study, research) and honest maturity labels (prototype, research,
  demonstration, template), and highlighted three flagship projects
  (Laya experiments, AI Governance Council, governance playbook).
- `docs/` folder: framework crosswalk (NIST AI RMF, ISO/IEC 42001, EU AI
  Act mapped to real project evidence), end-to-end demo walkthrough
  (intake to incident response), proposed monitoring and incident
  procedures, assumptions and limitations, and a references page with
  citations.
- Model cards, data cards, threat models, and risk registers for the two
  research flagships (Laya, council).
- Charts generated from the real committed results: Laya metrics with
  Wilson confidence intervals vs the rules baseline, council accuracy per
  seat, and council deliberation outcomes (`docs/figures/`).
- Automated tests (`tests/`) covering every offline demo plus JSON
  validation of committed artifacts, and a GitHub Actions CI workflow
  (`.github/workflows/ci.yml`) that runs them on push and pull request.
- `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, and issue
  templates.
- Per-project install table in the README, resolving the old "standard
  library only" claim: projects 01-07 and the analysis scripts are stdlib
  only; the Laya experiments need `laya` and `numpy`; the council re-run
  needs provider API access.

**Changed**

- Removed "audit-ready" wording from the Khanmigo, edtech, and playbook
  READMEs and the root README. Nothing here has been independently
  validated, and the wording now says what the documents actually are.
- `run_all_demos.sh` now also runs the intake triage demo (project 07).

## [v1.0] - 2026-09-28

The portfolio as it stood: 17 projects and 2 companion case studies,
including the Laya governance experiments (project 16) and the AI
Governance Council experiment (project 17) with full reports and findings.
