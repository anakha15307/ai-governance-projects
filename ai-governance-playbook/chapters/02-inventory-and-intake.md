# Chapter 2: Inventory and Intake

**Purpose:** Know what AI the organization actually has, and make sure new AI
enters the governance program through one front door.

**When to use it:** Continuously. Inventory is a living register; intake runs
on every new, changed, or discovered use case.

## Procedure

### 1. Define what counts as an AI use case

A use case = one AI system + one purpose + one deployment context. "Our
support chatbot" and "the same model summarizing internal meetings" are two
use cases — different people affected, different risks. Record each
separately.

### 2. Build the initial inventory (weeks 1–4)

You will not find everything by asking. Combine:

1. **Survey** engineering, product, data science, marketing, HR, support —
   "what tools with AI features did you adopt or build in the last 12 months?"
2. **Procurement records** — search for AI/ML/copilot/chatbot/assistant in
   vendor contracts and expense reports.
3. **IT/SaaS audit** — browser extensions, SaaS marketplaces, API keys.
4. **Interviews** — the survey misses shadow AI; 5–6 conversations with team
   leads surface what surveys don't.

Minimum inventory fields: use-case ID, name, owner, description, tier
(Chapter 3), data types, people affected, vendor or build, status
(proposed / in assessment / deployed / retired), last review date.

### 3. Run the intake process for every new use case

1. **Owner submits** [`templates/use-case-intake.md`](../templates/use-case-intake.md).
2. **Coordinator triages weekly:** completeness check → assign tier
   (Chapter 3) → scope the assessment.
3. **Analyst assesses** per the tier's requirements (Chapters 3–4).
4. **Register updated** — nothing is "in the program" until it's in the
   inventory with an owner and a tier.

### 4. Scope the use case and its boundaries

Before assessing, write down what the use case *is and isn't*:

- **In scope:** the model, the data it touches, the interface, the people
  affected, the decisions it influences.
- **Out of scope:** adjacent uses explicitly excluded (e.g., "this assessment
  covers the support chatbot; it does not cover the same vendor's sales
  forecasting module").
- **Assumptions:** what you're taking as given (e.g., "vendor's SOC 2 report
  accepted as evidence of infrastructure controls, not of model behavior").

Scope creep is the assessment-killer: if the boundary isn't written down, the
assessment quietly expands until it's never finished — or quietly shrinks
until it misses the actual risk.

### 5. Handle shadow AI

Discovered-but-unregistered uses get a retroactive intake with a 30-day
clock: submit the form, accept a tier, complete the tier's minimum
requirements. Make the path to compliance easy and the alternative (operating
outside governance) visibly riskier for the owner. Punishing discovery
teaches people to hide things.

## Worked mini-example (illustrative)

*Meridian Logistics* inventories 14 AI uses in three weeks; 6 are SaaS
features nobody had registered (meeting summarizers, an HR resume screener —
immediately tiered high, Chapter 3). The sales chatbot ("Relay") gets use-case
ID **ML-UC-007**. Scoping for Relay: *in scope* — the vendor chatbot drafting
customer replies in the support queue, the ticket text it reads, the agents
who approve drafts; *out of scope* — the vendor's analytics dashboard and any
future voice deployment; *assumption* — vendor's uptime and infrastructure
claims accepted, model behavior claims not accepted without testing.

## Common pitfalls

- **Inventory as a one-time project.** If nobody owns updates, it's stale in a
  quarter. Tie updates to intake (new), monitoring (changed), and an annual
  re-survey.
- **Use case defined by tool, not purpose.** "ChatGPT Enterprise" is not a
  use case; the six things people do with it are.
- **No owner, no entry.** Every inventory row needs a named human owner.
- **Treating discovery as misconduct.** You'll learn about shadow AI only if
  reporting it is safe.

## Templates

- [`templates/use-case-intake.md`](../templates/use-case-intake.md)

## Repo tooling

- [`ai-use-case-intake/`](../../ai-use-case-intake/) — intake form, triage
  rubric, and triage CLI implementing this chapter's process.
- [`model-registry/`](../../model-registry/) — registry with lineage and
  approval workflow for the inventory's model layer.
