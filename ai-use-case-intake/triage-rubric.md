# AI Use-Case Triage Scoring Rubric

> **Illustrative template.** Calibrate score bands and SLAs to your organization's
> risk appetite before use. See [README.md](./README.md).

Score each dimension 0–3 using the evidence in the intake form. When in doubt,
score up and document the rationale.

## Dimensions

| # | Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|
| D1 | Personal data involvement | No personal data | Internal business data only | Customer / employee personal data | Sensitive, special-category, or minors' data |
| D2 | Decision impact & oversight | Informational output only | Advisory output, human decides | Automated recommendation with human override | Autonomous decision affecting people |
| D3 | External exposure | Internal, non-public | Limited internal pilot | Customer-facing | Public-facing or safety-adjacent |
| D4 | Data handling & vendor posture | Internal systems only | Approved vendor / tool | New vendor or public model API | Unmanaged / consumer tool |
| D5 | Regulatory sensitivity | General productivity | Regulated-adjacent domain | Employment, education, finance, legal | EU AI Act Annex III-type high-risk use |

**Total score:** 0–15 (sum of the five dimensions).

## Review tracks

| Track | Score | Review path | Triage SLA |
|---|---|---|---|
| A — Minimal | 0–3 | Notify-only; log in registry; no formal review | 10 business days to record |
| B — Standard | 4–7 | Governance analyst review; light documentation | 5 business days |
| C — Elevated | 8–11 | Full risk assessment required; committee review | 3 business days to start assessment |
| D — Critical | 12–15 | Executive + legal review; deployment hold until cleared | 2 business days to escalate |

### Automatic Track D triggers (score-independent)

Route to Track D immediately if any apply:

- Prohibited-use indicators under the EU AI Act (e.g., social scoring, real-time remote biometric identification for law enforcement)
- Processing of minors' data with automated decision-making
- Use of an unapproved tool already in production ("shadow AI" discovery)

## Documentation standard

Every triaged use case gets a registry entry with: intake summary, dimension
scores with one-line rationale each, total score, assigned track, reviewer,
SLA due date, and next step. Triage decisions are auditable — a reviewer
reading the entry a year later should be able to reconstruct *why*.

## Calibration

Review this rubric quarterly: check whether low-scoring use cases later
caused incidents (bands too loose) and whether high-scoring reviews routinely
find nothing material (bands too tight). Record calibration decisions in the
registry notes.
