# Risk Assessment

Per Playbook Chapter 4. Tag every fact: **[Claim]** (vendor/builder says),
**[Observed]** (analyst saw), or **[Recommendation]** (analyst advises).

Use-case ID: [ORG-UC-NNN] — Name: [Name] — Tier: [1/2/3/4]
Analyst: [Name] — Date: [YYYY-MM-DD] — Version: [v1.0]

## 1. Scope

- In scope: [System, data, interfaces, people affected, decisions influenced]
- Out of scope: [Explicitly excluded adjacent uses]
- Assumptions: [What is taken as given, e.g., vendor infrastructure claims accepted]

## 2. Evidence summary

### Vendor / builder claims [Claim]

- [Claim 1 — source]
- [Claim 2 — source]

### Analyst observations [Observed]

- [Observation 1 — method: test/interview/log review, date]
- [Observation 2]

### Evidence gaps

- [What could not be verified — and why it matters]

## 3. Risk register

Likelihood 1–5 × Impact 1–5 = Score. Bands: 1–4 low, 5–9 medium, 10–15
high, 16–25 critical.

| ID | Failure mode (concrete) | L | I | Score | Controls (IDs from Ch. 5) | Residual |
|---|---|---|---|---|---|---|
| R-1 | [Concrete failure mode] | [ ] | [ ] | [ ] | [IDs + any custom controls] | [ ] |
| R-2 | [Concrete failure mode] | [ ] | [ ] | [ ] | [ ] | [ ] |
| R-3 | [Concrete failure mode] | [ ] | [ ] | [ ] | [ ] | [ ] |

Highest residual risk: [Score] — Tier tolerance: [e.g., none > 9 for Tier 2]

## 4. Control requirements

| Control ID | Control | Owner | Effectiveness test | Due |
|---|---|---|---|---|
| [ID] | [Name + tailoring] | [Name] | [How tested — see control-test-plan.md] | [Date] |

## 5. Evaluation traceability

| Risk ID | Test scenario(s) | Result | Date / version |
|---|---|---|---|
| [R-1] | [Scenario description] | [Pass / Fail] | [Date, model vX] |

## 6. Recommendation

- [ ] **Go** — residual risks within tolerance; controls implemented and tested
- [ ] **Conditional-go** — deploy only when §7 conditions are met
- [ ] **No-go** — [what would change this decision]

Rationale: [3–5 sentences tying the evidence to the recommendation]

## 7. Conditions (conditional-go only)

| # | Condition | Owner | Due date | Verified |
|---|---|---|---|---|
| 1 | [Specific, measurable] | [Name] | [YYYY-MM-DD] | [ ] |

## 8. Review

- Peer/program-owner review: [Name, date, outcome]
- Dissent (if any): [Recorded disagreement and rationale]
- Next review date: [YYYY-MM-DD]
