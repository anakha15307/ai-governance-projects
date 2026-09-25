# Regulatory Tracker

A monthly regulatory-brief habit: one concise page per month on EU AI Act
implementation and US state AI-law developments, built from a reusable
template with a scaffolding script. A September 2026 sample brief
(illustrative) is included.

## Problem

Policy-oriented governance roles expect analysts to translate law into
internal guidance. That requires a visible, sustained tracking habit, not a
one-time literature review. Hiring managers can spot the difference: a
candidate who publishes a monthly brief has demonstrably done the work.

## Users / Stakeholders

- **AI governance analyst**: researches and authors each brief.
- **Legal / compliance**: validate implications and own follow-up actions.
- **Governance committee**: receive the brief as a standing agenda input.
- **Policy-minded hiring managers**: read the archive as proof of a
  regulatory-tracking habit.

## Methods

- **Template** ([monthly-brief-template.md](./monthly-brief-template.md)):
  method note with sources, EU AI Act section (changes, upcoming
  obligations, implications), US state section (new/amended laws,
  enforcement, implications), program implications with owners and dates,
  and a next-month watchlist. Illustrative placeholders are explicitly
  marked and must be resolved before publishing.
- **Sample brief** ([briefs/2026-09-september.md](./briefs/2026-09-september.md)):
  September 2026, clearly labeled **illustrative sample**, demonstrates
  the format, the EU/high-risk framing, and how findings connect back to
  the intake rubric, vendor checklist, and edtech assessment in this
  portfolio.
- **Scaffold script** (`new_brief.py`, stdlib only): generates the next
  month's file from the template, pre-filled with date, author, and a link
  to the previous brief.

```bash
cd regulatory-tracker
python3 new_brief.py          # scaffold current month
python3 new_brief.py 2026 10  # scaffold October 2026
```

## Results

- A repeatable monthly cadence: ~30 minutes of research a week, one page a
  month, archived in [briefs/](./briefs/).
- Each brief ends in **implications with owners and due dates**, tracking
  without action items is just reading.
- The sample shows the key analyst move: connecting a regulatory
  development to a concrete program change (e.g., "high-risk documentation
  gap → inventory use cases against high-risk criteria").

## Risks and Controls

| Risk | Control |
|---|---|
| Brief presents stale or wrong law as fact | Method note requires official sources; illustrative items must be resolved; legal reviews implications |
| Tracking becomes performative | Every brief carries action items with owners and due dates; committee reviews them |
| Scope creep (every jurisdiction, every week) | Fixed scope: EU AI Act + US state laws monthly; other jurisdictions only when material |
| Sample brief mistaken for real advice | Banner labels it illustrative; no source links presented as verified |

## Next Steps

- Publish the first real brief next month from primary sources.
- Add the brief as a standing governance-committee agenda item.
- Build a one-page "regulatory change → control update" log linking briefs
  to policy and assessment revisions.
