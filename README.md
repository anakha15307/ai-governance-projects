# AI Governance Projects

Thirteen buildable, portfolio-ready projects covering the core competencies of AI governance — six technical builds plus seven analyst/operations projects (07–13) drawn from a 25-posting analysis of junior AI governance roles.

| # | Project | Governance competency |
|---|---------|----------------------|
| 01 | [`eu-ai-act-risk-classifier/`](./eu-ai-act-risk-classifier/) | Risk assessment — classify AI systems under EU AI Act tiers |
| 02 | [`bias-audit-suite/`](./bias-audit-suite/) | Evaluation — bias probes + fairness report cards |
| 03 | [`red-team-harness/`](./red-team-harness/) | Safety testing — adversarial evals with before/after scoreboard |
| 04 | [`policy-violation-monitor/`](./policy-violation-monitor/) | Oversight — supervisor monitor with human-in-the-loop escalation |
| 05 | [`model-registry/`](./model-registry/) | Provenance & control — registry with lineage + approval workflow |
| 06 | [`governance-dashboard/`](./governance-dashboard/) | Reporting — risk register dashboard for stakeholders |
| 07 | [`ai-use-case-intake/`](./ai-use-case-intake/) | Intake & triage — intake form, scoring rubric, registry, triage CLI |
| 08 | [`genai-usage-policy/`](./genai-usage-policy/) | Policy drafting — GenAI acceptable-use policy + exception template |
| 09 | [`edtech-risk-assessment/`](./edtech-risk-assessment/) | Risk assessment — EU AI Act tiering + NIST AI RMF mapping, controls, monitoring |
| 10 | [`vendor-ai-assessment/`](./vendor-ai-assessment/) | Vendor review — reusable checklist + completed public-tool assessment |
| 11 | [`regulatory-tracker/`](./regulatory-tracker/) | Regulatory tracking — monthly brief template, sample brief, scaffolding script |
| 12 | [`llm-eval-case-study/`](./llm-eval-case-study/) | Governance case study — turning LLM evaluation evidence into risk decisions |
| 13 | [`khanmigo-risk-assessment/`](./khanmigo-risk-assessment/) | Third-party risk assessment — Khanmigo (education AI), public-sources only |

## Skills coverage

Matrix mapping the analyst skills from a 25-posting sample of junior AI
governance roles (frequency in sample) to the projects demonstrating them.

| Analyst skill (share of postings) | Demonstrated in |
|---|---|
| AI system inventory (40%) | 07 intake registry · 05 model registry |
| Use-case intake / triage (36%) | 07 intake form, rubric, triage CLI |
| Stakeholder coordination (36%) | 07 intake workflow · 08 policy roles & review path · 10 vendor review · 06 dashboard · 13 stakeholder map & pilot gates |
| Risk-assessment authoring (36%) | 09 full assessment · 13 third-party assessment (public sources) · 01 EU AI Act classifier · 10 vendor findings |
| Privacy-law adjacency (36%) | 09 data-protection controls · 13 COPPA/FERPA DPA review · 08 data rules · 10 DPA checklist |
| Regulatory tracking (32%) | 11 monthly briefs · 09 EU AI Act tiering |
| Internal AI policy drafting (24%) | 08 GenAI acceptable-use policy |

Every project README follows one structure — **problem → users/stakeholders →
methods → results → risks and controls → next steps** — so each reads as a
standalone, audit-ready work sample.

## Quickstart

Every project is self-contained, runs on Python 3.12 with **standard library only** (no pip installs, no API keys), and ships with a `--demo` mode.

```bash
# Run all demos
./run_all_demos.sh

# Or run one project
cd eu-ai-act-risk-classifier && python classify.py --demo
```

## Why these thirteen

Governance hiring managers look for evidence you can *do* the work: assess risk, run evaluations, test safety, build oversight, track provenance, and communicate status. Projects 01–06 prove the technical evaluation skills; projects 07–13 prove the analyst/operations skills junior postings ask for most — intake, triage, policy drafting, vendor review, regulatory tracking, and third-party assessment from public sources. Each project produces an artifact (a report, a scoreboard, an audit log, a dashboard, a policy, a brief) — the kind of evidence that lands interviews.

## Notes

- The EU AI Act classifier is an educational simplification, not legal advice.
- Stub models in the audit/red-team projects are illustrative; each documents how to plug in a real model endpoint.
