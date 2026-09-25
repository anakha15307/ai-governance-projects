# AI Governance Risk & Compliance Playbook

An end-to-end operating manual for standing up and running an AI governance
program at a mid-size organization. Written for the people who do the work, 
analysts and coordinators: in plain language, with step-by-step procedures,
worked examples, and fillable templates.

> Independent practitioner material. Illustrative examples are fictional and
> marked as such. Not legal advice, verify regulatory obligations against
> official texts and counsel.

## The problem this solves

Organizations adopt AI faster than they govern it. Most "governance" material
available to analysts is one of two things: high-level frameworks (NIST AI RMF,
ISO/IEC 42001) that say *what* to do but not *how*, or vendor whitepapers that
sell a platform. An analyst handed responsibility for AI governance typically
gets neither a charter, nor an intake process, nor a single template, and is
expected to produce audit-ready work anyway. This playbook is the missing
middle: the procedures, artifacts, and cadence that turn framework principles
into a running program.

## How to use it

**Two ways in:**

- **Read straight through** (chapters 1-16) when standing up a program from
  scratch. The chapters are ordered as a build sequence: charter → inventory →
  tiering → assessment → controls → policy → oversight → testing → deployment
  decisions → monitoring → incident response → vendor management → regulatory
  mapping → training → metrics → documentation.
- **Use templates standalone** when you need one artifact now. Each
  [`templates/`](./templates/) file is fillable on its own, with
  `[bracketed]` fields, and each chapter links the templates it uses.

**Cross-reference with this repo's builds.** Several playbook steps are
implemented as working projects elsewhere in this repository, use them
together:

| Playbook step | Implementation in this repo |
|---|---|
| Use-case intake & triage (Ch. 2) | [`ai-use-case-intake/`](../ai-use-case-intake/), intake form, scoring rubric, triage CLI |
| Risk tiering (Ch. 3) | [`eu-ai-act-risk-classifier/`](../eu-ai-act-risk-classifier/). EU AI Act tier classifier |
| Bias evaluation (Ch. 8) | [`bias-audit-suite/`](../bias-audit-suite/), bias probes + report cards |
| Red-teaming (Ch. 8) | [`red-team-harness/`](../red-team-harness/), adversarial evals |
| Oversight monitoring (Ch. 7, 10) | [`policy-violation-monitor/`](../policy-violation-monitor/), supervisor monitor with human escalation |
| Model registry (Ch. 2, 10) | [`model-registry/`](../model-registry/), registry with lineage + approvals |
| GenAI acceptable use (Ch. 6) | [`genai-usage-policy/`](../genai-usage-policy/), policy + exception template |
| Vendor assessment (Ch. 12) | [`vendor-ai-assessment/`](../vendor-ai-assessment/), checklist + worked example |
| Regulatory tracking (Ch. 13) | [`regulatory-tracker/`](../regulatory-tracker/), monthly brief template + scaffolding |
| Risk reporting (Ch. 15) | [`governance-dashboard/`](../governance-dashboard/), risk register dashboard |
| Incident review (Ch. 11) | [`ai-incident-deconstructions/`](../ai-incident-deconstructions/), real-incident deconstructions |

The playbook is the operating manual; those projects are the tooling. A new
analyst can read Chapter 2 and then run the intake triage CLI the same day.

## Chapters

| # | Chapter | Question it answers |
|---|---|---|
| 01 | [`01-program-setup.md`](./chapters/01-program-setup.md) | Who owns AI governance, and how do we run it week to week? |
| 02 | [`02-inventory-and-intake.md`](./chapters/02-inventory-and-intake.md) | What AI do we actually have, and how does new AI enter the program? |
| 03 | [`03-risk-tiering.md`](./chapters/03-risk-tiering.md) | How much governance does each use case need? |
| 04 | [`04-risk-assessment.md`](./chapters/04-risk-assessment.md) | How do we assess a use case rigorously and reach a risk rating? |
| 05 | [`05-controls-library.md`](./chapters/05-controls-library.md) | Which controls exist, and which tier gets which? |
| 06 | [`06-policy-suite.md`](./chapters/06-policy-suite.md) | What rules do people follow day to day? |
| 07 | [`07-human-oversight.md`](./chapters/07-human-oversight.md) | Where must a human stay in the loop? |
| 08 | [`08-testing-and-evaluation.md`](./chapters/08-testing-and-evaluation.md) | How do we test before and after deployment? |
| 09 | [`09-deployment-decisions.md`](./chapters/09-deployment-decisions.md) | Who decides go / conditional-go / no-go, and how is it recorded? |
| 10 | [`10-monitoring.md`](./chapters/10-monitoring.md) | How do we know a deployed system is still behaving? |
| 11 | [`11-incident-response.md`](./chapters/11-incident-response.md) | What do we do when AI causes harm or almost does? |
| 12 | [`12-vendor-management.md`](./chapters/12-vendor-management.md) | How do we govern AI we buy instead of build? |
| 13 | [`13-regulatory-mapping.md`](./chapters/13-regulatory-mapping.md) | How do our controls map to NIST AI RMF, ISO/IEC 42001, and the EU AI Act, and how do we track change? |
| 14 | [`14-training.md`](./chapters/14-training.md) | Who needs to know what, and how do we teach it? |
| 15 | [`15-metrics-and-reporting.md`](./chapters/15-metrics-and-reporting.md) | Is the program working, and what does leadership need to see? |
| 16 | [`16-documentation-and-audit.md`](./chapters/16-documentation-and-audit.md) | What do we keep, and would it survive an audit? |

## Users / Stakeholders

- **AI governance analyst (primary reader)**: runs intake, writes assessments,
  designs tests, maintains the register. Chapters 2-5, 8, 10, 16 are daily
  tools.
- **AI governance coordinator**: runs the cadence: triage meetings, review
  boards, training logistics, metrics. Chapters 1, 9, 14, 15 are the operating
  rhythm.
- **Executive sponsor / governance committee**: approves the charter, makes
  tier-3/4 deployment decisions, receives board reporting. Chapters 1, 9, 15.
- **Use-case owners (business & engineering)**: submit intakes, implement
  controls, respond to findings. Chapters 2, 5, 6.
- **Hiring managers**: each chapter reads as a work sample of analyst judgment.

## Methods

The playbook was built by working backward from what junior AI governance
postings actually ask for (intake/triage, risk assessment, policy drafting,
vendor review, regulatory tracking, stakeholder coordination, incident review):

1. **One running example.** Every chapter's worked example uses the same
   fictional company - *Meridian Logistics*, a mid-size freight firm: and the
   same use case: a customer-support chatbot ("Relay") that drafts replies a
   human agent reviews before sending. Following one use case through 16
   chapters shows how the pieces connect.
2. **Procedures, not principles.** Each chapter has numbered steps an analyst
   can execute, with named artifacts at each step.
3. **Proportionate by design.** The tiering system (Chapter 3) is the load-bearing
   wall: everything downstream, controls, testing depth, decision authority,
   monitoring frequency: scales with tier. Governance that costs the same for
   a meeting-summarizer and a hiring model will be ignored for both.
4. **Evidence discipline everywhere.** The vendor-claims vs. analyst-observations
   vs. recommendations split (from this repo's case studies) is baked into
   assessment, vendor review, and documentation chapters.
5. **Templates carry the detail.** Chapters teach the method; the eleven
   fillable templates in [`templates/`](./templates/) are what actually get
   filled in during real work.

## Results

- 16 chapters covering the full lifecycle: stand-up → intake → assessment →
  controls → deployment → monitoring → incident → reporting → audit.
- 11 fillable templates with `[bracketed]` fields, usable standalone.
- Cross-references to 11 working projects in this repo that implement
  playbook steps as runnable tooling.
- A consistent fictional worked example (Meridian Logistics / Relay chatbot)
  threaded through every chapter.

## Risks and controls

| Risk | Control |
|---|---|
| Playbook read as legal advice | "Not legal advice" stated here and in regulatory chapters; crosswalk marked illustrative; instructs verification against official texts |
| One-size-fits-all application | Tiering chapter forces proportionate application; pitfalls sections warn against over-governing low-risk uses |
| Fictional example mistaken for real | Meridian Logistics / Relay explicitly marked fictional and illustrative in every chapter |
| Playbook goes stale as regulations evolve | Chapter 13 includes a change-tracking method; regulatory tracker project provides the monthly mechanism |

## Next steps

- Work the templates against a real or realistic use case; file the completed
  artifacts as the program's first records.
- Pair each chapter with its referenced repo project (e.g., read Chapter 2,
  then run the intake triage CLI).
- Revisit Chapter 13 quarterly: the regulatory crosswalk is the section most
  likely to need updates.
