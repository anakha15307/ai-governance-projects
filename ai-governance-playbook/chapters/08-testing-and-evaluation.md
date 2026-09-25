# Chapter 8: Testing and Evaluation

**Purpose:** Verify, before and after deployment: that the system behaves
as the risk assessment assumes. Testing is where governance claims meet
reality.

**When to use it:** Pre-deployment for Tier 3-4; control-effectiveness
testing on a schedule for Tier 2+; re-test on material change.

## Procedure

### 1. Derive test scenarios from the risk register

Every risk rated medium or above (Chapter 4) becomes at least one scenario:
a concrete input, the expected safe behavior, and pass/fail criteria written
*before* running the test. A test suite that isn't traceable to risks is
entertainment.

### 2. Run scenario-based evaluation

- Build the eval set: 20-50 scenarios per significant risk for Tier 3;
  scale with stakes, not with enthusiasm.
- Include **adversarial variants**: typos, ambiguous phrasing, edge cases,
  and users trying to get the wrong answer: not just the happy path.
- Record: scenario, input, output, pass/fail, date, model version. Version
  everything: an eval result without a model version is unrepeatable.

### 3. Red-team the abuse paths

Separate from scenario evals: structured attempts to make the system
misbehave: jailbreaks, prompt injection, data exfiltration, impersonation.
Rules: scope it in writing, use test accounts and test data, stop and report
on finding a critical bypass (don't "see how far it goes" in production).
Tier 3-4 pre-deployment; Tier 2 on a schedule or after incident.

### 4. Test control effectiveness, not just the model

Controls are claims too. For each key control, run a direct test:

| Control | Effectiveness test |
|---|---|
| Human approval gate | Plant N known-bad outputs; measure reviewer catch rate |
| PII redaction | Feed known PII patterns; verify none reach logs/outputs |
| Retrieval scoping | Attempt cross-context retrieval; verify denial |
| Incident runbook | Tabletop exercise; measure time-to-contain (Ch. 11) |
| Training completion | Spot-quiz a sample of staff; verify ≥ target score |

Schedule: Tier 2 annually, Tier 3 semi-annually, Tier 4 quarterly, or after
any material change. A control that hasn't been tested this year is an
assumption.

### 5. Set pass/fail gates and record results

Define gates before testing (e.g., "≥ 95% pass on safety scenarios, zero
critical red-team bypasses, ≥ 90% reviewer catch rate"). Results go into the
assessment file and the deployment decision record (Chapter 9). Failed gates
block deployment: that's what gates are for.

## Worked mini-example (illustrative)

*Meridian Logistics*, **ML-UC-007** (Tier 2, conditional-go pending a 60-day
control check): the analyst builds 30 scenarios from risks R-1-R-3, 
10 refund-policy probes (including "my grandmother died, I need an
exception" emotional-pressure variants), 10 cross-customer data probes, 10
credential-pasting probes. Results: 27/30 pass; 2 refund drafts misstated
the 72-hour window (R-1 confirmed as real); 1 credential case logged the
password before redaction ran (R-3b ordering bug, fixed). Control test:
planted 10 bad drafts, agents caught 9 (90%: meets gate). Decision: proceed
to full deployment with the redaction fix verified and sampling continued.

## Common pitfalls

- **Testing the demo, not the deployment.** Eval against the production
  configuration, data, and interfaces: not a sandbox with different
  guardrails.
- **Pass criteria invented after seeing results.** Write gates first.
- **One-and-done testing.** Models, prompts, and data drift; untested
  controls decay. Schedule it.
- **Red-teaming without rules.** Unauthorized "testing" of production
  systems is an incident, not an evaluation.

## Templates

- [`templates/control-test-plan.md`](../templates/control-test-plan.md)

## Repo tooling

- [`red-team-harness/`](../../red-team-harness/), adversarial eval runner
  with before/after scoreboard.
- [`bias-audit-suite/`](../../bias-audit-suite/), disaggregated fairness
  probes for people-affecting uses.
