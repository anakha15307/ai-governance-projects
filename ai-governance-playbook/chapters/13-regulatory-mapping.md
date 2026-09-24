# Chapter 13: Regulatory Mapping

**Purpose:** Show how the program's controls map to the frameworks and laws
that matter — NIST AI RMF, ISO/IEC 42001, and the EU AI Act — and keep that
mapping current as the landscape moves.

> Illustrative crosswalk, not legal advice. Framework versions and legal
> texts evolve; verify every obligation against official sources and counsel
> before relying on it.

**When to use it:** When building the program (to avoid reinventing
requirements), when leadership asks "are we compliant with X," and on a
quarterly change-review cadence.

## The crosswalk (high level, illustrative)

The three instruments answer different questions: **NIST AI RMF** is a
voluntary risk-management framework (Govern, Map, Measure, Manage);
**ISO/IEC 42001** is a certifiable management-system standard (plan-do-
check-act for AI); the **EU AI Act** is binding law with risk tiers and
obligations. The playbook's controls satisfy all three at once — here's how
the chapters line up:

| Playbook chapter | NIST AI RMF | ISO/IEC 42001 (illustrative) | EU AI Act (illustrative) |
|---|---|---|---|
| 1 Program setup | GOVERN 1–2 (culture, roles) | Leadership, roles & responsibilities (Cl. 5) | Provider/deployer governance expectations |
| 2 Inventory & intake | MAP 1 (context established) | Context of the organization (Cl. 4) | Foundation for risk classification |
| 3 Risk tiering | MAP 2 (categorization) | Risk assessment process (Cl. 6) | Risk-tier determination (prohibited / high-risk / limited / minimal) |
| 4 Risk assessment | MAP 3–5 (risks characterized) | AI risk assessment & treatment | High-risk: risk management system (Art. 9) |
| 5 Controls library | GOVERN 4, MANAGE 1–2 | Controls in Annex A | Technical documentation & record-keeping duties |
| 7 Human oversight | MAP 3, MANAGE 3 | Human oversight considerations | Human oversight (Art. 14, high-risk) |
| 8 Testing & evaluation | MEASURE 1–3 | Monitoring, measurement, analysis (Cl. 9) | Accuracy, robustness, cybersecurity (Art. 15) |
| 10 Monitoring | MEASURE 4, MANAGE 4 | Post-deployment monitoring | Post-market monitoring (Art. 72) |
| 11 Incident response | MANAGE 3–4 | Nonconformity & corrective action (Cl. 10) | Serious incident reporting (Art. 73) |
| 12 Vendor management | GOVERN 6 (third-party risk) | Supplier relationships | Value-chain obligations (Arts. 25, 53–55 for GPAI) |
| 16 Documentation | GOVERN 4 | Documented information (Cl. 7.5) | Technical documentation (Art. 11), logging (Art. 12) |

Two notes on reading this table: first, it maps *program activities to
framework functions*, not clause-by-clause compliance — treat it as an
orientation map, not a certification checklist. Second, the EU AI Act column
describes obligations that depend heavily on your role (provider vs.
deployer), use case, and jurisdiction — the Act phases in over 2024–2027
and guidance is still maturing.

## Procedure: change tracking

Regulations move; the program must move with them. Quarterly:

1. **Scan:** regulatory briefs (see repo tooling), official registers
   (EU AI Act implementation updates, NIST publications, ISO amendments),
   enforcement actions.
2. **Assess impact:** for each development — does it change a tier
   definition, add an obligation, or alter a notification clock? Map it to
   affected chapters and use cases.
3. **Decide:** program owner determines whether controls, policies, or the
   crosswalk need updates; record the decision even when the answer is "no
   change."
4. **Communicate:** changes go into the next training cycle (Chapter 14)
   and the board update (Chapter 15) when material.

## Worked mini-example (illustrative)

*Meridian Logistics* operates in the US but serves EU customers. The
quarterly scan flags new EU guidance on general-purpose AI model
obligations. Impact assessment: Relay is a deployer-use of a GPAI-based
vendor product — obligations fall mostly on the vendor, but Meridian's
transparency duties (informing customers they're interacting with AI) and
incident-reporting awareness need checking. Decision: update the Chapter 6
acceptable-use policy's disclosure rule and add a vendor-evidence request
(Chapter 12) for the vendor's GPAI compliance documentation. Recorded in
the change log; no control changes needed this quarter.

## Common pitfalls

- **Treating the crosswalk as compliance.** Mapping is not meeting the
  obligation — especially for the AI Act, where role determination and
  conformity assessment are legal questions.
- **US-only blind spot.** Even US companies can be in scope for the EU AI
  Act via EU users or deployment.
- **Freezing the mapping.** A crosswalk written in 2025 and never revisited
  is a liability, not an asset.
- **Chasing every headline.** Most "AI regulation news" changes nothing for
  your program. The impact assessment step exists to say so.

## Repo tooling

- [`regulatory-tracker/`](../../regulatory-tracker/) — monthly brief
  template, sample brief, and scaffolding script implementing the
  change-tracking procedure.
- [`eu-ai-act-risk-classifier/`](../../eu-ai-act-risk-classifier/) —
  educational EU AI Act tier classifier.
