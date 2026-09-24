# Chapter 11: Incident Response

**Purpose:** When AI causes harm — or nearly does — respond quickly, contain
it, learn from it, and improve the program. Speed matters; so does the
record.

**When to use it:** On any AI incident or near-miss; tabletops run on a
schedule (Tier 3–4 at least annually).

## Severity levels

| Level | Definition | Example | Response lead |
|---|---|---|---|
| SEV-4 | Near-miss, caught by controls | Planted bad draft caught in sampling | Analyst |
| SEV-3 | Limited real impact | Wrong reply sent to one customer, corrected | Use-case owner + analyst |
| SEV-2 | Significant impact or pattern | PII leak to multiple customers; repeated policy misstatements | Program owner |
| SEV-1 | Severe harm, legal/regulatory exposure, press | Discriminatory hiring outputs; safety-critical failure | Executive sponsor + legal |

When in doubt, escalate one level. Downgrading is cheap; under-responding
isn't.

## The runbook

Use [`templates/incident-runbook.md`](../templates/incident-runbook.md).
Standard sequence:

1. **Detect & declare** — anyone can declare; the coordinator confirms
   severity within 4 hours (SEV-1: 1 hour).
2. **Contain** — stop the bleeding: pause the use case, roll back the
   change, disable the feature. Containment authority is pre-delegated —
   don't convene a committee while harm continues.
3. **Assess** — scope: who was affected, for how long, what data was
   involved. Preserve logs and evidence immediately.
4. **Notify** — internal (per severity), then external as obligations
   require: affected individuals, regulators, vendors. Legal reviews
   external communications. Know your notification clocks *before* the
   incident (Chapter 13).
5. **Remediate** — fix the technical cause *and* the governance cause
   (Chapter 5's control language: which preventive/detective/corrective
   controls failed or were missing?).
6. **Learn** — post-incident review within 10 business days: timeline,
   root causes (technical + governance), control gaps, program changes.
   File it; feed patterns into training (Chapter 14).

## Tabletop exercises

Annually for Tier 3–4 (recommended for the program overall): pick a
scenario ("the chatbot tells 200 customers about a refund policy that
doesn't exist"), gather the actual responders, and walk the runbook —
who declares, who contains, who notifies, what breaks. Tabletops find the
gaps that documents hide: the runbook says "notify legal," but nobody has
legal's after-hours number.

## Worked mini-example (illustrative)

*Meridian Logistics*: monitoring (Chapter 10) flags that Relay sent 14
customers a refund amount double the policy limit — a vendor prompt change
interacted with a stale policy snippet. Declared **SEV-2**. Containment:
Relay paused within 2 hours (pre-delegated authority — no meeting needed).
Assessment: 14 customers affected over 6 days; no PII involved. Notification:
support lead contacts all 14 with corrections; program owner briefs the COO.
Remediation: technical — pin prompt version, add amount-range validation
(new preventive control); governance — vendor change notification was
missing from the contract (Chapter 12 gap), added at renewal; monitoring
alert threshold tightened. Post-incident review filed; the pattern ("vendor
silent change + stale context") added to analyst training.

## Common pitfalls

- **No pre-delegated containment authority.** "Should we pause it?"
  debated while harm continues.
- **Fixing the technical cause only.** The model bug gets fixed; the
  missing change-management control that let it ship doesn't.
- **Skipping the post-incident review.** The most valuable artifact —
  and the first thing dropped when everyone's tired.
- **Treating near-misses as non-events.** SEV-4s are free lessons. Log
  them, review them quarterly.

## Templates

- [`templates/incident-runbook.md`](../templates/incident-runbook.md)

## Repo tooling

- [`ai-incident-deconstructions/`](../../ai-incident-deconstructions/) —
  real-incident deconstructions demonstrating the technical-vs-governance
  root-cause method used in post-incident reviews.
