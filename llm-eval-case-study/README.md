# LLM Evaluation & Red-Teaming: Governance Case Study

A governance case study of an independent LLM evaluation project: turning
model test evidence into risk decisions, controls, and stakeholder-ready
documentation. The technical work lives in
[red-team-harness](../red-team-harness/) and
[bias-audit-suite](../bias-audit-suite/); this case study is the
*governance layer* on top of it.

## Problem

Evaluation results don't govern anything by themselves. A red-team run that
produces a scoreboard but no risk decision, no control recommendation, and
no record an auditor can follow is an engineering exercise, not governance.
The gap this project closes: converting test evidence into the artifacts a
governance program actually runs on (risk entries, control requirements,
deployment conditions, monitoring plans).

## Users / Stakeholders

- **AI governance analyst (author)**: designs the evaluation, interprets
  results, writes the governance record.
- **Model/system owner**: receives control requirements and deployment
  conditions.
- **Governance committee**: reviews residual risk and approves or blocks
  deployment stages.
- **Future auditors**: reconstruct decisions from the dated evidence trail.

## Methods

1. **Scoped the evaluation to a governance question.** Not "is the model
   safe in general" but: *does this system meet the safety bar for its
   intended use case, and what controls are required before pilot?* Scope,
   intended users, and out-of-scope uses were written down first (method
   borrowed from the [edtech assessment](../edtech-risk-assessment/)).
2. **Built a repeatable red-team harness** ([red-team-harness](../red-team-harness/)):
   26 adversarial attacks across prompt injection, jailbreak personas, data
   exfiltration, and disallowed content, plus benign controls, run against
   "before guardrails" and "after guardrails" targets with a rule-based,
   auditable judge.
3. **Ran bias probes** ([bias-audit-suite](../bias-audit-suite/)) to check
   for performance and representation disparities relevant to fairness risk.
4. **Mapped findings to NIST AI RMF** Measure and Manage functions:
   evaluation results → identified risks → control recommendations →
   residual-risk statements.
5. **Wrote the governance record**: risk entries with likelihood/impact,
   required controls with owners, deployment conditions (pilot only after
   gates pass), and a monitoring plan with thresholds, the same structure
   as the [edtech risk assessment](../edtech-risk-assessment/).

## Results

- **Before → after guardrails:** attack success rate fell from 100% to 0%
  across all four attack categories, with benign-task helpfulness preserved
  (2/2 controls helpful). Full transcripts in `results.json`; scoreboard in
  `scoreboard.md` (see [red-team-harness](../red-team-harness/)).
- **Governance translation:** the scoreboard became deployment conditions, 
  e.g., *pilot may proceed only with guardrail configuration X evidenced by
  a re-run of the harness; any model or config change triggers regression*.
- **Monitoring commitments:** periodic re-runs of the attack suite,
  incident-driven re-testing, and human review sampling of production
  outputs.
- **Reusable method:** the harness documents how to point it at a real model
  endpoint (stdlib `urllib` adapter) and how to extend the attack library, 
  so the case study is a starting point, not a one-off.

## Risks and Controls

| Risk | Control |
|---|---|
| Rule-based judge misses subtle failures | Documented as a limitation; human review of sampled transcripts required; LLM-as-judge recommended for production |
| Stub targets overstate the method's power | Case study states plainly: stubs are illustrative; real assurance requires testing real models |
| Evaluation goes stale after deployment | Regression requirement on model/config change; periodic re-runs in the monitoring plan |
| Results used to claim "certified safe" | Scoreboard framed as regression evidence for a defined scope, never as certification |

## Next Steps

- Apply the harness to a real model endpoint for a defined use case and
  publish the (sanitized) governance record.
- Extend the attack library with domain-specific attacks (e.g., education
  or hiring scenarios).
- Pair the harness with the [policy-violation-monitor](../policy-violation-monitor/)
  pattern for runtime oversight of the evaluated system.
- Feed evaluation cadence into the [regulatory tracker](../regulatory-tracker/)
  watchlist (evaluation expectations evolve with guidance).
