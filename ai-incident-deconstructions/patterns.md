# Patterns across the three incidents

Three different sectors (aviation, hiring, parcel delivery), three different countries,
three different failure modes — and the same governance failures underneath.

## What recurs

### 1. The AI spoke for the company, but nobody owned what it said
- **Air Canada** argued its chatbot was "a separate legal entity that is responsible
  for its own actions."
- **iTutorGroup** argued its tutors were contractors outside employment law, and let
  software make the rejection decisions.
- **DPD** attributed the failure to "an error occurred after a system update" — a
  cause without an owner.

In each case, the organizational posture was distance, not accountability. Courts and
regulators have now answered this the same way every time: **the deployer owns the
output.** (BCCRT: "It makes no difference whether the information comes from a static
page or a chatbot." EEOC: "Prohibitions on age discrimination do not stop at the
border.")

**Governance lesson:** Name the accountable owner for every AI system's outputs
*before* deployment. If your incident response starts with explaining why the AI
isn't really yours, the governance program has already failed.

### 2. Consequential uses with inconsequential assurance
- Air Canada's bot answered **fare and refund questions** (financial commitments).
- iTutorGroup's software made **hiring decisions** (livelihoods, protected class).
- DPD's bot was the **front door of customer service** (brand and revenue).

All three were treated as low-stakes automation. None received assurance
proportionate to the stakes: no policy-accuracy testing, no disparate-impact
analysis, no adversarial testing.

**Governance lesson:** Classify AI uses by consequence *before* deciding how much
assurance they need. The question is never "is it AI?" — it's "what happens when
it's wrong?"

### 3. Detection happened externally, not by a control
- Air Canada: discovered via a **tribunal filing**, months after the bad answer.
- iTutorGroup: discovered via a **complainant** who A/B-tested her own application.
- DPD: discovered via a **viral social media post**.

Not one of the three organizations detected its own failure through monitoring.
Detective controls were absent in all three cases.

**Governance lesson:** If your incident detection strategy is "wait for someone to
sue us or go viral," you don't have one. Production monitoring — sampled review,
anomaly flags, funnel analytics — is a governance requirement, not an engineering
nice-to-have.

### 4. The "AI" label obscured simple, testable failures
- Air Canada's failure was **contradiction with its own policy page** — catchable by
  any evaluation set built from company sources.
- iTutorGroup's failure was **programmed age cutoffs** — catchable by basic
  selection-rate analysis (the 4/5ths rule).
- DPD's failure was **trivial prompt manipulation** — catchable by a one-afternoon
  red-team pass.

None required exotic AI safety research to prevent. All three were failures of
ordinary diligence applied to AI systems.

**Governance lesson:** Most AI incidents are not alignment problems. They are
testing, monitoring, and accountability problems wearing an AI costume. A governance
program that does the basics — eval sets, funnel metrics, red-teaming, ownership —
prevents the majority of real-world incidents.

### 5. Remediation was reactive in all three cases
Air Canada promised to "update the chatbot" only after the dispute escalated; the
EEOC's non-monetary relief had to be *imposed* by consent decree; DPD disabled the
bot only after virality. Corrective controls existed nowhere as standing procedure.

**Governance lesson:** Write the incident runbook before the incident: detect →
assess → contain → remediate → retest → disclose. Rehearse the kill-switch.

## The one-line summary

> Every incident here was preventable with controls that already existed as standard
> practice — the organizations just hadn't applied them to their AI systems.

That is the core argument for AI governance as a discipline: it is not about novel
technology, but about extending accountability, testing, and monitoring to systems
that previously escaped them.
