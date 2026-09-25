# Chapter 12: Vendor Management

**Purpose:** Govern AI you buy instead of build, assess it, contract for
it, and keep watching it, because vendor AI is where most organizations'
actual exposure lives.

**When to use it:** Before procuring or piloting any third-party AI
(Chapter 6 procurement policy enforces this); re-assess on vendor model
updates and at renewal.

## Procedure

### 1. Assess before you buy

Run the vendor through [`templates/vendor-assessment.md`](../templates/vendor-assessment.md)
, the same evidence discipline as Chapter 4: vendor claims tagged as
claims, your observations (trial, docs, references) tagged as observations.
Minimum evidence to request:

- What the model does and doesn't do (capabilities and limitations in
  writing: not marketing copy)
- Data practices: what data trains the model, whether *your* data trains
  *their* model, retention, sub-processors
- Security posture: SOC 2 or equivalent, pen-test summary, incident history
- Testing: what evaluations the vendor ran, on what data, with what results
- Change management: how and when you're notified of model updates

No evidence = no procurement for Tier 3-4. For Tier 2, missing evidence
becomes a conditional-go condition (Chapter 9).

### 2. Contract the governance you need

Non-negotiable terms for Tier 2+ vendor AI:

- **Data use limits:** customer data not used for training without explicit
  opt-in; defined retention and deletion.
- **Change notification:** advance notice of model/material changes with
  the right to re-test before acceptance.
- **Audit rights:** proportionate, from documentation requests to
  assessment cooperation.
- **Incident notification:** vendor notifies you of incidents affecting
  your deployment within a defined SLA.
- **DPA / data-processing terms:** where personal data is involved,
  standard data-processing addendum terms (purpose limitation, sub-processor
  notice, deletion on termination). Not legal advice, involve counsel.

### 3. Monitor the vendor relationship

Vendor AI changes without asking you (Chapter 10's Meridian example: the
silent prompt change). Controls: contractual change notification, your own
regression evals on vendor updates, renewal re-assessment. A vendor
assessment is a snapshot; the relationship needs the movie.

### 4. Plan the exit

Know before signing: how you export your data, how the vendor deletes it,
what happens to integrations. Exit planning during procurement is cheap;
during a dispute it's impossible.

## Worked mini-example (illustrative)

*Meridian Logistics* procures Relay from a vendor. Assessment findings:
vendor claims "enterprise-grade accuracy" (claim, no eval data provided);
trial observation, 3 of 40 test drafts misstated policy (observation);
vendor confirms customer data is *not* used for training (claim,
corroborated by DPA language: accepted). Contract gaps found: no model
change notification clause, no incident notification SLA. Negotiated in:
30-day advance notice of material model changes, 72-hour incident
notification. Six months later the vendor pushes a silent prompt-template
change: caught by Meridian's monitoring, not the vendor's notice, 
becoming a SEV-2 (Chapter 11) and a renewal negotiation lever.

## Common pitfalls

- **Accepting the vendor's risk assessment as your own.** Their assessment
  serves their liability; yours serves your customers.
- **Pilots that bypass procurement.** "It's just a trial" with production
  data is production.
- **Negotiating price, forgetting governance.** The DPA and change
  notification cost nothing compared to the incident they prevent.
- **One-and-done vendor review.** Re-assess at renewal and on major
  version changes.

## Templates

- [`templates/vendor-assessment.md`](../templates/vendor-assessment.md)

## Repo tooling

- [`vendor-ai-assessment/`](../../vendor-ai-assessment/), reusable vendor
  checklist plus a completed public-tool assessment.
