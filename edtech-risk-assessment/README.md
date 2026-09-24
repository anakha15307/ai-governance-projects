# Educational-AI Risk Assessment

A full, audit-ready risk assessment of a fictional AI tutoring assistant —
with EU AI Act tier classification, NIST AI RMF function mapping, a risk
register, controls, residual risk, and a monitoring plan. All names,
organizations, and figures are fictional; the EU AI Act analysis is an
illustrative simplification, not legal advice.

## Problem

Education is one of the highest-stakes domains for AI: the users are minors,
the system influences learning outcomes, and regulators treat educational AI
as high-risk. A governance analyst must be able to take an ambiguous product
description and produce a defensible classification, a structured risk
register, and a monitoring plan — before deployment, not after an incident.

## Users / Stakeholders

- **AI governance analyst** — authors and maintains the assessment.
- **Business owner / school district leadership** (fictional "Example School
  District") — accountable for the go/no-go decision.
- **Teachers and parents** — need to understand what the system does, its
  limits, and the oversight in place.
- **Legal, privacy, security** — review regulatory, data-protection, and
  technical controls.
- **Auditors / regulators** — read the assessment as evidence of a risk
  management process.

## Methods

- **System scoping** ([assessment §1](./edtech-ai-tutor-risk-assessment.md)):
  users, data, model, deployment, and human-oversight design documented first —
  classification follows from facts, not assumptions.
- **EU AI Act tiering** (§2): prohibited → high-risk → limited-risk
  transparency analysis, with reasoning recorded. Illustrative result:
  **High-Risk** (education — evaluation of learning outcomes), plus
  transparency obligations for the conversational interface.
- **NIST AI RMF mapping** (§3): Govern / Map / Measure / Manage functions and
  subcategories traced to assessment sections, so the document doubles as
  framework evidence.
- **Risk register** (§4): seven risks with likelihood, impact, mapped
  controls, and residual risk.
- **Pre-pilot evaluation gates** (§5): accuracy, fairness, red-teaming,
  privacy review, and teacher acceptance — the pilot does not start until all
  pass.
- **Monitoring plan** (§7): metrics, cadence, thresholds, and escalation
  paths for post-deployment oversight.

## Results

- A complete assessment artifact ([edtech-ai-tutor-risk-assessment.md](./edtech-ai-tutor-risk-assessment.md)):
  7 risks, 17 controls with named owners, residual-risk ratings, and a
  conditional pilot recommendation (limited pilot only after gates pass).
- Demonstrates the two frameworks employers ask for most: EU AI Act
  classification reasoning and NIST AI RMF mapping in a single document.
- The assessment is reusable as a template: replace §1's system description
  and re-run the §2–§8 structure for any education or employment AI use case.

## Risks and Controls

| Risk | Control |
|---|---|
| Misclassification of the EU AI Act tier | Reasoning documented step-by-step; legal review (C16) required before deployment |
| Assessment goes stale after deployment | §7 monitoring plan with quarterly governance review; material findings trigger a new dated version |
| Controls exist on paper only | Every control has a named owner and status; pre-pilot gates (§5) require evidence, not assertions |
| Teacher over-reliance on AI snapshots | Human-in-the-loop rule for interventions; snapshot uncertainty notes; teacher training (C11–C12) |

## Next Steps

- Validate the illustrative EU AI Act classification with counsel against
  current implementing guidance.
- Build the §5 evaluation question bank and red-team suite (methodology in
  [../red-team-harness/](../red-team-harness/)).
- If the pilot proceeds, publish the first quarterly monitoring report and
  version the assessment.
