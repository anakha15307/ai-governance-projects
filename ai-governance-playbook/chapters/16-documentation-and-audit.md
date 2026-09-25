# Chapter 16: Documentation and Audit

**Purpose:** Keep records that prove the program ran, so an auditor, a
regulator, or a future you can reconstruct what was decided, on what
evidence, and by whom.

**When to use it:** Always. Documentation is produced as work happens, not
reconstructed afterward.

## What to keep (the record set)

| Record | Produced in | Retention (illustrative) |
|---|---|---|
| Charter, RACI, policies | Ch. 1, 6 | Life of program + 3 years |
| Inventory register | Ch. 2 | Life of program + 3 years |
| Intake forms, tiering worksheets | Ch. 2, 3 | Life of use case + 3 years |
| Risk assessments | Ch. 4 | Life of use case + 3 years |
| Eval / red-team / control-test results | Ch. 8 | Life of use case + 3 years |
| Deployment decision records | Ch. 9 | Life of use case + 5 years |
| Monitoring plans and findings | Ch. 10 | 3 years |
| Incident records and post-incident reviews | Ch. 11 | 5 years |
| Vendor assessments and contracts | Ch. 12 | Life of relationship + 5 years |
| Training records | Ch. 14 | 3 years |
| Metrics and board reports | Ch. 15 | 5 years |

Retention periods are illustrative: align with your organization's
records schedule and legal counsel.

## Evidence quality standards

Not all records are equal. Tag evidence by quality:

- **Level 1: Direct:** test results, logs, signed records, observed
  behavior. Strongest.
- **Level 2: Corroborated:** vendor claims backed by independent evidence
  (audit report, trial observation, reference customer).
- **Level 3: Asserted:** vendor or owner claims without corroboration.
  Usable for scoping; never the sole basis for a Tier 3-4 decision.

The Chapter 4 evidence discipline (claim vs. observation vs. recommendation)
is how this gets applied in practice. An assessment built on Level-3
evidence is an opinion with formatting.

## Audit-readiness checklist

For any use case, an auditor should be able to answer in under an hour:

- [ ] Is it in the inventory with an owner and a tier?
- [ ] Does the tier match the rubric (or is the override recorded)?
- [ ] Is there a signed deployment decision with residual risks stated?
- [ ] Are required controls assigned to owners with effectiveness tests?
- [ ] Do monitoring and review records exist for the current period?
- [ ] Are incidents/near-misses logged with post-incident reviews?
- [ ] Can every factual claim in the assessment be traced to Level 1-2 evidence?

If any answer is no, that's a program finding: fix it before the auditor
does.

## Procedure

1. **File as you go:** every artifact lands in the program repository at
   creation, named `[use-case-id]-[artifact]-[date]`.
2. **Version everything:** assessments, eval sets, and policies carry
   version numbers; superseded versions are retained, not overwritten.
3. **Quarterly hygiene:** coordinator runs the audit-readiness checklist
   on a sample of use cases; gaps become remediation items in the risk
   review.

## Worked mini-example (illustrative)

*Meridian Logistics* prepares for its first internal audit of the program.
The coordinator pulls **ML-UC-007**'s file: intake form, tiering worksheet
(Tier 2, score 8), light assessment with evidence-tagged register, control
selections with owners, 60-day sampling results (91% catch rate), signed
conditional-go decision record with conditions tracked to closure, monitoring
plan with weekly findings, one SEV-2 record with post-incident review, and
the vendor assessment. The auditor's one finding: training records show 4
agents completed the reviewer briefing a week *after* go-live, a sequencing
gap, remediated by tying training completion to the deployment checklist
(Chapter 9). The program passes because the records existed, not because
anyone scrambled.

## Common pitfalls

- **Reconstructing records for the audit.** If it wasn't written when it
  happened, it's not evidence: it's creative writing.
- **Overwriting instead of versioning.** "Final_v2" chaos destroys the
  decision trail. Version and retain.
- **Evidence laundering.** A vendor claim copied into three documents is
  still Level 3.
- **Keeping everything forever.** Retention without deletion is a breach
  waiting to happen: follow the schedule.

## Templates

All eleven templates in [`templates/`](../templates/) are documentation
artifacts; filed completed, they *are* the audit trail.
