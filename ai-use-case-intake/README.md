# AI Use-Case Intake & Triage

Operational intake for AI governance: a standard intake form, a transparent
scoring rubric, a machine-readable registry, and a small CLI that triages a
new use case and appends it to the registry. Illustrative sample content.

## Problem

AI governance programs fail at the front door: business teams adopt AI tools
without telling anyone, and governance teams learn about them after an
incident. Without a standard intake path, there is no inventory, no risk
tiering, and no auditable record of *why* a use case got the review it got.

## Users / Stakeholders

- **Business requestors** — submit the intake form to get a fast, predictable answer on what review their AI idea needs.
- **AI governance analyst** — runs triage, assigns review tracks, keeps the registry current.
- **Governance committee / legal / security** — receive Track C and D escalations with complete context.
- **Auditors** — read the registry to verify that intake, tiering, and review decisions are documented.

## Methods

- **Intake form** ([intake-form.md](./intake-form.md)) — requestor details, use-case
  description, data categories, technology and deployment posture, human
  oversight level, risk-indicator checklist, approvals.
- **Triage rubric** ([triage-rubric.md](./triage-rubric.md)) — five scored dimensions
  (data, decision impact, exposure, vendor posture, regulatory sensitivity),
  0–15 scale, mapped to four review tracks (A Minimal → D Critical) with SLAs,
  plus score-independent automatic Track D triggers.
- **Registry** ([registry.json](./registry.json)) — every triaged use case with
  dimension scores, one-line rationale per dimension, total score, assigned
  track, SLA due date, and status. Three illustrative sample entries included.
- **Triage CLI** (`triage.py`, stdlib only) — interactive scoring prompts or
  `--demo` mode; computes the track, stamps SLA dates, and appends to the
  registry.

```bash
cd ai-use-case-intake
python3 triage.py --demo        # triage an illustrative sample, append to registry.json
python3 triage.py              # interactive triage
```

## Results

- A repeatable front door: any AI use case can be registered in one sitting,
  with a defensible review track assigned the same day.
- Triage decisions are reconstructable — each registry entry carries the
  scores and rationale behind its track, which is what auditors ask for.
- Sample registry demonstrates the full range: a Track A notify-only pilot
  (score 2), a Track B standard review (score 7), and a Track C elevated
  review (score 10) requiring a full risk assessment before any pilot.

## Risks and Controls

| Risk | Control |
|---|---|
| Requestors understate risk to skip review | Automatic Track D triggers; rubric instructs scoring up under uncertainty; analyst validates the form before scoring |
| "Shadow AI" never enters intake | Procurement and IT asset reviews feed discoveries back into intake; Track D covers already-deployed unapproved tools |
| Rubric bands drift from real risk | Quarterly calibration review: compare scores against incidents and review outcomes; record decisions |
| Registry becomes stale | Status field + SLA dates; analyst owns monthly registry hygiene |

## Next Steps

- Connect intake to the procurement/vendor-review workflow (see
  [../vendor-ai-assessment/](../vendor-ai-assessment/)).
- Auto-generate Track C risk-assessment shells from registry entries using the
  [educational-AI assessment format](../edtech-risk-assessment/).
- Add a quarterly registry report view (counts by track, overdue SLAs) to the
  [governance dashboard](../governance-dashboard/).
