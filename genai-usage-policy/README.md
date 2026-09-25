# GenAI Usage Policy

A complete, adoption-ready acceptable-use policy for generative AI, plus an
exception request template. Illustrative sample, not legal advice.

## Problem

Staff adopt GenAI tools faster than governance can review them. Without a
written policy there is no shared definition of acceptable use, no review
path for new tools, and no basis for enforcement when confidential data ends
up in a consumer chatbot.

## Users / Stakeholders

- **All staff and contractors**: need clear rules on what they may and may
  not do with GenAI.
- **Managers**: sponsor exception requests and ensure team awareness.
- **AI governance lead**: owns the approved-tool list and the review path.
- **Security, legal/privacy, internal audit**: review, advise, and verify
  compliance.

## Methods

- Drafted as a full policy document
  ([genai-acceptable-use-policy.md](./genai-acceptable-use-policy.md)): purpose,
  scope, definitions, roles, acceptable use, data rules, prohibited uses, a
  five-step review path for new tools, controls, exceptions, enforcement, and
  version history.
- The review path is wired into the rest of this portfolio: intake
  ([../ai-use-case-intake/](../ai-use-case-intake/)) feeds triage, triage
  feeds the [vendor AI assessment](../vendor-ai-assessment/), and Track C/D
  uses require committee or executive sign-off.
- [Exception request template](./exception-request-template.md) captures
  justification, risk description, compensating controls, approvals, and
  expiry review: exceptions are time-boxed, never open-ended.

## Results

- A policy an organization can adapt and adopt: twelve sections covering the
  full lifecycle from request to enforcement.
- "Shadow AI" is handled explicitly: a 30-day disclosure window and a defined
  path back into compliance, rather than an unenforceable ban.
- Every requirement maps to an owner and a control, so the policy is
  auditable rather than aspirational.

## Risks and Controls

| Risk | Control |
|---|---|
| Policy ignored because it is too restrictive | Acceptable-use section leads with permitted uses; exceptions process is fast and documented |
| Approved-tool list goes stale | Quarterly review of the list is a named control with an owner |
| Data leakage into unapproved tools | Data rules by classification; security monitoring for unapproved-tool traffic; 24-hour incident reporting |
| High-risk uses slip through as "productivity" | Risk-indicator checklist on the intake form; human-oversight requirement for decisions about people |

## Next Steps

- Pilot with one department; collect exception requests to find where the
  policy is too tight or too loose.
- Build role-specific training modules for high-risk uses (hiring, customer
  communications, code).
- Review annually and on material regulatory change (see
  [regulatory tracker](../regulatory-tracker/)).
