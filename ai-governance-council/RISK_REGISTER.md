# Risk register: AI Governance Council experiment

| ID | Risk | Likelihood | Impact | Mitigation | Residual |
|---|---|---|---|---|---|
| R1 | Findings over-generalized beyond 8 synthetic cases | Medium | Medium | Findings scoped to the experiment throughout; model card prohibits generalization | Low |
| R2 | Ground-truth errors (my reading of the AI Act) presented as fact | Medium | Medium | Case 7 ambiguity disclosed; cases carry my stated legal basis | Low |
| R3 | Free-tier reliability findings go stale as providers change tiers | High | Low | Dated to September 2026 in findings | Low |
| R4 | Re-runner submits sensitive data to free tiers (which may train on prompts) | Low | High | README warns free tiers may use prompts; experiment used synthetic cases only | Low |
| R5 | Confidence tie-break trusted as meaningful | Low | Medium | Finding reported plainly: confidence had no signal | Low |

Reviewed: 2026-09-29. Next review: if the experiment is re-run or extended.
