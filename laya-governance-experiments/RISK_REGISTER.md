# Risk register: Laya safety gate experiment

Risks of the experiment itself and of anyone misusing its results. This is a
project-level register, kept in the style of the repo's risk assessments.

| ID | Risk | Likelihood | Impact | Mitigation | Residual |
|---|---|---|---|---|---|
| R1 | Results over-interpreted as production evidence | Medium | High | Report states explicitly nothing here is evidence of production readiness; model card repeats it | Medium |
| R2 | Small sample (n=60) gives false confidence | Medium | Medium | Wilson and bootstrap intervals reported; limitations documented | Low |
| R3 | Baseline comparison misleads (baseline tuned on test prompts) | Low | Medium | Caveat stated in report and README | Low |
| R4 | Bias probe too narrow to catch real skew | Medium | High | Documented as limitation; listed as future work, not claimed | Medium |
| R5 | Reproduction fails on different hardware/seed | Low | Low | Model hash, package versions, CPU, and commands recorded | Low |
| R6 | Someone deploys a Laya gate citing this experiment | Low | High | Model card prohibits this use; report conclusion is explicit | Low |

Reviewed: 2026-09-29. Next review: when the experiment is extended (larger
prompt set, held-out split, or multi-turn attacks), or not at all if it
stays a portfolio piece.
