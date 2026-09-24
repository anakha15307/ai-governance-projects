# AI Governance Projects

Six buildable, portfolio-ready projects covering the core competencies of AI governance — the same "one project per skill" format as the [AI engineer roadmap](https://instagram.com/p/DdpwoQgD3kk/) that inspired it, adapted for governance roles.

| # | Project | Governance competency |
|---|---------|----------------------|
| 01 | [`eu-ai-act-risk-classifier/`](./eu-ai-act-risk-classifier/) | Risk assessment — classify AI systems under EU AI Act tiers |
| 02 | [`bias-audit-suite/`](./bias-audit-suite/) | Evaluation — bias probes + fairness report cards |
| 03 | [`red-team-harness/`](./red-team-harness/) | Safety testing — adversarial evals with before/after scoreboard |
| 04 | [`policy-violation-monitor/`](./policy-violation-monitor/) | Oversight — supervisor monitor with human-in-the-loop escalation |
| 05 | [`model-registry/`](./model-registry/) | Provenance & control — registry with lineage + approval workflow |
| 06 | [`governance-dashboard/`](./governance-dashboard/) | Reporting — risk register dashboard for stakeholders |

## Quickstart

Every project is self-contained, runs on Python 3.12 with **standard library only** (no pip installs, no API keys), and ships with a `--demo` mode.

```bash
# Run all demos
./run_all_demos.sh

# Or run one project
cd eu-ai-act-risk-classifier && python classify.py --demo
```

## Why these six

Governance hiring managers look for evidence you can *do* the work: assess risk, run evaluations, test safety, build oversight, track provenance, and communicate status. Each project produces an artifact (a report, a scoreboard, an audit log, a dashboard) — the kind of evidence that lands interviews.

## Notes

- The EU AI Act classifier is an educational simplification, not legal advice.
- Stub models in the audit/red-team projects are illustrative; each documents how to plug in a real model endpoint.
