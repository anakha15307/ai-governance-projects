# Chapter 1: Program Setup

**Purpose:** Establish who owns AI governance, what authority they have, and
how the program runs week to week — before any use case is assessed.

**When to use it:** First, when standing up the program; revisit annually or
after a reorganization.

## Procedure

### 1. Draft the governance charter (1–2 pages)

The charter is the program's founding document. It must answer five questions:

1. **Scope** — which AI uses are governed? (Recommendation: all AI that makes
   or influences decisions affecting people, handles personal data, or
   represents the company externally — including procured tools and "shadow
   AI" pilots. Explicitly exclude nothing by accident: say what is *out* of
   scope, e.g., spellcheck.)
2. **Authority** — what can governance stop? The program must be able to pause
   a deployment pending review. A governance body that can only advise will be
   routed around.
3. **Roles** — who does what (see §3).
4. **Cadence** — the operating rhythm (see §4).
5. **Escalation** — what happens when a use-case owner disagrees with a
   finding (see step 4).

Keep it short. A ten-page charter won't be read; a two-page charter gets
signed.

### 2. Define the roles

| Role | Accountable for | Typical holder |
|---|---|---|
| Executive sponsor | Funding, authority, final call on tier-4 decisions | CTO / COO / Chief Risk Officer |
| Program owner | Charter, committee agenda, program metrics | Head of risk, compliance, or responsible-AI lead |
| AI governance coordinator | Runs the cadence: triage meetings, review scheduling, training logistics, metrics | Dedicated coordinator or senior analyst |
| AI governance analyst | Intake reviews, risk assessments, test design, register maintenance | Analyst (this playbook's primary reader) |
| Use-case owner | The business/technical owner of each AI use; implements controls | Product manager, engineering lead |
| Control owners | Individual controls assigned in the controls library | Named per control (security, data, legal, eng) |

Analyst vs. coordinator vs. owner is the distinction that matters most:
the **analyst** produces findings, the **coordinator** runs the process, the
**owner** fixes things. One person can wear analyst and coordinator hats in a
small program, but never let the use-case owner be their own assessor.

### 3. Stand up the RACI

Use [`templates/raci-chart.md`](../templates/raci-chart.md). Minimum viable
RACI covers: intake triage, risk assessment, control assignment, deployment
decision, incident response, and policy exception. Fill it in a workshop with
the actual people — a RACI written by one person in a vacuum is fiction.

### 4. Set the operating cadence

| Forum | Frequency | Attendees | Decides |
|---|---|---|---|
| Intake triage | Weekly (30 min) | Coordinator, analyst, rotating eng/product | Tier assignment, assessment scoping |
| Risk review | Monthly (60 min) | Program owner, analysts, control owners | Assessment findings, control gaps, remediation |
| Governance committee | Quarterly (90 min) | Executive sponsor, program owner, legal, security | Tier-3/4 deployment decisions, policy changes, program metrics |
| Board / exec update | Quarterly or semi-annual | Sponsor → board | Program KPIs, material risks, incidents |

### 5. Record the disagreement path

Disagreements are normal: an owner will dispute a tier, a finding, a timeline.
The charter should state: analyst findings stand unless overturned in writing
by the program owner (tiers 1–2) or the governance committee (tiers 3–4),
with the rationale recorded in the decision log. Silent overrides are how
programs die.

## Worked mini-example (illustrative)

*Meridian Logistics* (fictional mid-size freight company, ~800 employees) is
standing up governance after a sales team pilots an AI chatbot without review.
The COO signs a two-page charter: scope covers all customer-facing AI and any
model touching employee or customer personal data; the program owner (Head of
Risk) can pause deployments pending review; cadence is weekly triage, monthly
risk review, quarterly committee. The chatbot pilot's owner — the sales
director — becomes the use-case owner and must submit a retroactive intake
(Chapter 2). The first RACI workshop takes 45 minutes and surfaces that nobody
owns model monitoring — which becomes the program's first gap to close.

## Common pitfalls

- **Governance without stop authority.** If the program can't pause a
  deployment, it is a documentation exercise.
- **The committee that meets annually.** Quarterly minimum; tier-3/4 decisions
  can't wait a year.
- **Analyst = owner.** The person building the model cannot be the person
  signing off its risk assessment.
- **Charter bloat.** If it needs a table of contents, it's too long.

## Templates

- [`templates/raci-chart.md`](../templates/raci-chart.md)
