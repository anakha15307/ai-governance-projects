# Vendor AI Assessment

A reusable vendor AI review checklist plus a completed illustrative
assessment of a well-known public AI tool, with findings, an overall
rating, and remediation.

## Problem

Most AI risk enters through vendors: a team adopts a tool, nobody checks
what happens to the data, and the organization discovers the terms only
during an incident or audit. Procurement reviews cover price and features;
they rarely cover model behavior, training-data use, or AI-specific
contract terms.

## Users / Stakeholders

- **AI governance analyst** — completes the checklist per tool.
- **Procurement** — runs the commercial process; needs the assessment to
  negotiate terms.
- **Legal / privacy / security** — own the DPA, attestation, and contract
  findings.
- **Business requestor** — waits on the rating before rollout.

## Methods

- **Checklist** ([vendor-ai-checklist.md](./vendor-ai-checklist.md)): six
  sections (vendor profile, data practices, model & AI safety, security,
  compliance & legal, operational), each item rated Pass / Conditional /
  Fail / N-A with cited evidence. Overall rating follows the worst material
  finding: Approved, Approved with conditions, or Not approved.
- **Completed sample** ([public-tool-review.md](./public-tool-review.md)):
  ChatGPT (OpenAI) assessed for an illustrative internal-productivity scope,
  based solely on publicly available information. Result: **Approved with
  conditions** — enterprise-tier DPA, no-training-on-data confirmation,
  SSO enforcement, and legal review of IP/indemnity terms required before
  rollout. Explicitly not approved for confidential data or decisions about
  individuals in this sample.
- The checklist plugs into the intake workflow: Track B+ use cases from
  [ai-use-case-intake](../ai-use-case-intake/) require a vendor review
  before approval.

## Results

- A procurement-ready checklist covering the AI-specific questions standard
  security questionnaires miss (training-data use, model versioning, EU AI
  Act role allocation, output IP).
- A worked example showing how to turn public information into a structured,
  caveated finding set — and how to write remediation with owners and dates
  instead of vague concerns.
- Clear scope discipline: the sample rates the tool for one defined use
  case, not as a blanket approval.

## Risks and Controls

| Risk | Control |
|---|---|
| Assessment based on marketing pages, not contracts | Checklist requires evidence citations; conditionals must close against executed agreements |
| Vendor terms change after approval | Annual re-review trigger; subprocessor-change and deprecation notice terms negotiated up front |
| Checklist treated as one-and-done | Re-assessment on material vendor change, new data classes, or expanded use case |
| Analyst lacks leverage to enforce remediation | Overall rating gates rollout; Track C/D reviews escalate to committee |

## Next Steps

- Run the checklist against the next real tool request and publish the
  (sanitized) result internally.
- Build a lightweight vendor re-review calendar (annual + event-driven).
- Add AI-specific clauses to the standard procurement intake so assessments
  start earlier.
