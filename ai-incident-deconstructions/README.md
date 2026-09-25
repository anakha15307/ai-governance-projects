# AI Incident Deconstructions

Governance deconstructions of three real, public AI incidents, root-cause analysis
from a governance lens, not news summaries. Each deconstruction asks: what failed
technically, what failed organizationally, which controls were missing, and what a
competent AI governance program would have done differently.

> Independent analysis from public reporting. Not legal advice. Where sources
> conflict or a detail is unverified, the deconstruction says so.

## The three incidents

| # | Deconstruction | Sector | Failure mode |
|---|---|---|---|
| 01 | [`deconstructions/01-air-canada-chatbot.md`](./deconstructions/01-air-canada-chatbot.md) | Aviation / customer service | Chatbot hallucinated bereavement-fare policy; tribunal held the airline liable for negligent misrepresentation (2024 BCCRT 149) |
| 02 | [`deconstructions/02-itutorgroup-eeoc.md`](./deconstructions/02-itutorgroup-eeoc.md) | Hiring / HR tech | Recruiting software auto-rejected older applicants; $365,000 EEOC settlement (2023) |
| 03 | [`deconstructions/03-dpd-chatbot.md`](./deconstructions/03-dpd-chatbot.md) | Logistics / customer service | Chatbot jailbroken into profanity and brand criticism; AI element disabled (Jan 2024) |

Plus [`patterns.md`](./patterns.md), what recurs across all three incidents: and
[`SOURCES.md`](./SOURCES.md), every source cited, with quality notes.

## Problem

Incident write-ups usually stop at "the AI did something bad." That teaches nothing.
The governance question is always downstream of the technical failure: *why was a
system with this failure mode allowed to operate, undetected, in this context?*
Without that analysis, organizations fix the symptom (disable the bot, pay the
settlement) and keep the disease (no ownership, no testing, no monitoring).

## Users / Stakeholders

- **AI governance analyst (author)**: selects incidents, separates technical from
  governance causes, writes findings as controls.
- **Governance committee / leadership**: reads the patterns, not just the
  incidents; decides which missing controls to fund.
- **Hiring managers**: sees evidence of analyst judgment: the ability to turn a
  news story into a control recommendation with an owner.
- **Practitioners**: reuses the deconstruction template for their own incidents.

## Methods

1. **Pick incidents with public records.** Selection criteria: a documented outcome
   (court decision, regulatory settlement, or contemporaneous multi-outlet reporting),
   enough public detail to separate causes, and relevance to common enterprise AI
   uses (customer service, hiring). AI Incident Database entries anchor each case.
2. **Reconstruct the timeline first.** Dates and sequence before analysis, causes
   can't be assigned without knowing what happened when.
3. **Separate technical cause from governance cause.** The technical cause explains
   *how* the system produced the failure (hallucination, hard-coded threshold,
   weak guardrails). The governance cause explains *why it was allowed to*
   (no owner, no testing, no monitoring, accountability engineered away).
4. **Name the missing controls in control language.** Every gap is stated as
   preventive, detective, or corrective: because "we should have tested more" is
   a wish, while "no pre-deployment evaluation set (preventive)" is a finding.
5. **Write recommendations with owners.** A control without an owner is a
   suggestion. Each recommendation names who is accountable for implementing it.
6. **Map to NIST AI RMF.** For each incident: which of Govern, Map, Measure,
   Manage failed, and how. The framework organizes the findings; it doesn't
   substitute for them.
7. **Mark the unverifiable.** Where the public record is thin (e.g., the model
   vendor behind a chatbot, whether "AI" meant ML or rules), the deconstruction
   says so rather than filling the gap.

## Results

- Three complete deconstructions, each with timeline, dual root-cause analysis,
  control gap table, owned recommendations, NIST AI RMF mapping, and sources.
- A cross-incident patterns analysis identifying five recurring failures:
  unowned AI output, inconsequential assurance for consequential uses, external
  detection, simple testable failures hiding behind the "AI" label, and reactive
  remediation.
- A reusable deconstruction template (the structure above) for future incidents.

## Risks and controls

| Risk | Control |
|---|---|
| Analysis overstates what public sources support | Every claim tied to a cited source; unverifiable details explicitly marked in each file and in SOURCES.md |
| Reading as legal conclusions rather than analysis | "Not legal advice" stated in README and each deconstruction; tribunal/settlement outcomes reported as outcomes, not as the analyst's legal judgment |
| Incidents age and facts evolve | SOURCES.md records access/verification dates; template instructs future deconstructions to re-verify |
| Selection bias (only famous failures) | Selection criteria documented in Methods; near-miss included deliberately (DPD had no legal outcome) to show the method isn't outcome-dependent |

## Next steps

- Add deconstructions on a fixed cadence (one per quarter keeps the series alive
  and demonstrates the monitoring habit).
- Extend into new domains: a hiring-bias case outside the US, a healthcare or
  lending incident, a GPAI/transparency-obligation case under the EU AI Act.
- Turn the patterns into a control checklist for pre-deployment review of
  customer-facing AI: closing the loop from incident analysis back into
  prevention.
