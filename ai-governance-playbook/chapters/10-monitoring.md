# Chapter 10: Monitoring

**Purpose:** Know that a deployed system is still behaving as approved, 
and detect when it isn't, before customers or regulators do.

**When to use it:** From deployment onward; monitoring plans are written
during assessment (Chapter 4) and activated at go-decision (Chapter 9).

## Procedure

### 1. Write the monitoring plan before deployment

Use [`templates/monitoring-plan.md`](../templates/monitoring-plan.md). For
each use case, define: what is monitored (outputs, decisions, data flows),
how (sampling, automated checks, user reports), by whom, how often, alert
thresholds, and where alerts go. A monitoring plan written after deployment
is a postmortem outline.

### 2. Monitor three layers

- **Output quality:** sampled human review of outputs/decisions (Chapter 7's
  catch-rate measurement lives here as a recurring metric). Watch for
  accuracy decay, tone shifts, policy misstatements.
- **Behavioral drift:** volume anomalies, new failure modes, changes in
  user interaction patterns (e.g., sudden spike in jailbreak attempts).
  Compare against the pre-deployment baseline from Chapter 8.
- **Context drift:** the world changed around the model, new products, new
  policies, new regulations, new data distributions. The model didn't change;
  its correctness did.

### 3. Define review triggers, not just schedules

Scheduled reviews (by tier) plus event triggers that force an out-of-cycle
review: model or prompt change, vendor update, data source change, incident
or near-miss, complaint spike, regulatory change, expansion to new users or
geographies. Write the trigger list into the plan; "we'll know it when we
see it" misses things.

### 4. Track the metrics that matter

Minimum set per Tier 2+ use case: sample pass rate, incident/near-miss
count, reviewer catch rate (where human oversight exists), control-test
results, days since last review, open remediation items. Roll up to program
KPIs in Chapter 15.

### 5. Close the loop

Monitoring findings go to the monthly risk review (Chapter 1): re-score
risks, update controls, re-tier if needed. A finding that doesn't change a
risk score, a control, or a tier was either trivial or mishandled.

## Worked mini-example (illustrative)

*Meridian Logistics*, **ML-UC-007** monitoring plan: weekly sampling of 20
replies (pass = accurate, policy-correct, no PII leakage); alert if weekly
pass rate drops below 95% or any critical failure (wrong refund sent,
PII leak) occurs: alert goes to the support lead and the analyst within
one business day. Triggers: vendor model update → re-run the 30-scenario
eval set before accepting; new refund policy → re-test R-1 scenarios within
7 days. At month 4, sampling catches the vendor's silent prompt-template
change altering the greeting's legal disclaimer, caught by monitoring,
not by the vendor's changelog (which didn't mention it). Finding: add
"vendor change notification" to the contract at renewal (Chapter 12).

## Common pitfalls

- **Monitoring dashboards nobody reads.** Alerts need owners and SLAs;
  dashboards need a review forum. Otherwise it's wallpaper.
- **No baseline.** Without pre-deployment measurements, "drift" is a
  feeling.
- **Vendor changes invisible.** Most production AI changes come from the
  vendor's side. Contractual change notification (Chapter 12) plus your own
  regression evals.
- **Findings without consequences.** If monitoring never changes a risk
  score or triggers a control fix, it's compliance theater.

## Templates

- [`templates/monitoring-plan.md`](../templates/monitoring-plan.md)

## Repo tooling

- [`policy-violation-monitor/`](../../policy-violation-monitor/), automated
  output monitoring with human escalation.
- [`governance-dashboard/`](../../governance-dashboard/), risk register
  dashboard for rolling monitoring findings up to stakeholders.
- [`model-registry/`](../../model-registry/), version tracking so eval
  results stay tied to model versions.
