# Deconstruction 02 — EEOC v. iTutorGroup: automated age screening in hiring

**Incident:** U.S. Equal Employment Opportunity Commission enforcement action —
*EEOC v. iTutorGroup, Inc., et al.*, Civil Action No. 1:22-cv-02565 (E.D.N.Y.)
**Outcome:** Consent decree approved 8 September 2023 — $365,000 to 200+ rejected
applicants plus non-monetary relief
**Analyst note:** Independent analysis from public reporting and EEOC releases.
The EEOC's complaint described programmed age thresholds; how much "AI" versus
hard-coded rules the software contained is unclear from public sources (see note).
Not legal advice.

---

## What happened — timeline

| Date | Event |
|---|---|
| 2020 | iTutorGroup — three integrated companies providing online English-language tutoring to students in China, hiring U.S.-based tutors — allegedly programmed its online tutor-application software to **automatically reject female applicants aged 55 or older and male applicants aged 60 or older**. |
| 2020 | Charging party Wendy Picus applied, indicating an age over 55, and was rejected. She resubmitted an otherwise identical application with a more recent date of birth — and was offered an interview. |
| 5 May 2022 | After its conciliation process failed, the EEOC filed suit in the U.S. District Court for the Eastern District of New York, alleging violations of the Age Discrimination in Employment Act (ADEA). The agency alleged 200+ qualified U.S.-based applicants were rejected based on age. |
| 9 Aug 2023 | The parties filed a joint notice of settlement / consent decree. |
| 8 Sep 2023 | The court approved the decree: **$365,000** distributed to the affected applicant class, plus non-monetary relief — anti-discrimination policies and training, an injunction, an opportunity for rejected applicants to reapply, and ongoing reporting to the EEOC on hiring outcomes. |

iTutorGroup argued its tutors were independent contractors, not employees covered by the
ADEA. The EEOC's position — accepted in the resolution — was that the companies' close
control over how remote tutors performed their work made them employees protected by
federal anti-discrimination law. (Sources: EEOC press release, Sep 2023;
Foley & Lardner, Aug 2023; Jackson Lewis, Aug 2023; Mondaq/Lexology, Sep 2023.)

**Terminology note:** Commentators called this the EEOC's "first AI-based
antidiscrimination settlement." The public record is thinner than the label: the EEOC's
allegations describe *programmed* age cutoffs in application software — which reads as
deterministic rules, not a learned model. Whether machine learning was involved at all
is not established in the sources reviewed. The governance lessons below apply to both,
but this analysis does not claim the system was an ML model.

---

## Root cause analysis

### Technical cause
The application software encoded explicit age-and-sex thresholds that automatically
disqualified candidates before any human review. Whether implemented as hard-coded
rules or model features, the effect was identical: a protected characteristic
functioned as an automated knockout criterion with no human in the loop and,
allegedly, no adverse-impact analysis.

### Governance cause
1. **No fairness review of an employment decision system.** A tool that makes or
   heavily influences hiring decisions is about as high-stakes as enterprise AI gets.
   There is no public evidence of any pre-deployment bias or disparate-impact
   assessment.
2. **No monitoring of selection rates.** The 4/5ths rule and basic funnel analytics
   would have surfaced the age pattern immediately — 200+ auto-rejections on a single
   demographic dimension is not subtle. Nobody was watching the funnel.
3. **Accountability engineered away, twice.** First via the contractor-classification
   argument (the workers aren't employees, so employment law doesn't apply); second via
   automation itself (the *software* rejected them). Both are versions of the same
   governance failure: structuring the operation so no one is answerable for outcomes.
4. **Vendor/algorithm opacity as a shield.** The "AI" framing — whatever the technology
   actually was — functioned as cover for what the EEOC alleged was straightforward
   programmed discrimination. Governance programs must be able to answer "what logic
   actually made this decision?" for every automated employment screen.

---

## Controls that failed or were missing

| Control | Type | Status |
|---|---|---|
| Pre-deployment bias / adverse-impact assessment of hiring screening logic (e.g., 4/5ths rule analysis by age, sex, race) | Preventive | **Missing** — no evidence any assessment was performed |
| Documented inventory of automated employment decision tools with their decision logic | Preventive (governance) | **Missing** — the logic only surfaced through litigation |
| Ongoing monitoring of applicant funnel selection rates by protected characteristic | Detective | **Missing** — 200+ rejections accumulated undetected |
| Human review before final rejection of candidates (no fully automated knockouts on protected characteristics) | Preventive | **Missing** — rejection was automatic |
| Legal/compliance review of screening criteria against ADEA and Title VII before deployment | Preventive | **Missing/failed** |
| Complaint and anomaly investigation workflow (Picus's two applications were the detection mechanism — by accident) | Detective | **Missing** — detection happened via a complainant, not a control |

---

## What a competent AI governance program would have done differently

| # | Recommendation | Owner |
|---|---|---|
| 1 | Maintain a register of every automated employment decision tool: what it decides, what inputs it uses, who owns it, when it was last assessed. No hiring automation operates off-register. | AI Governance + HR Technology |
| 2 | Run a disparate-impact analysis (selection rates by age, sex, race — 4/5ths rule as a floor, not a ceiling) **before** any screening tool goes live, and document the results. | AI Governance + Employment Counsel |
| 3 | Prohibit fully automated rejection on the basis of — or highly correlated with — protected characteristics. Every auto-screened-out candidate above a risk threshold gets human review. | Talent Acquisition + Legal |
| 4 | Monitor hiring-funnel selection rates by protected characteristic on a fixed cadence (e.g., monthly); define the threshold that triggers investigation and pause. | HR Analytics + AI Governance |
| 5 | Require employment counsel to sign off on screening criteria and on any vendor's "AI" claims — including asking the vendor to demonstrate *what the model actually does* versus marketing language. | Legal + Procurement |
| 6 | After any finding: remediate affected candidates (reconsideration, as the decree required), retrain, and report — the consent decree's non-monetary terms are a usable template for a corrective-action plan. | Legal + HR |

---

## NIST AI RMF mapping — where it failed

| Function | Failure |
|---|---|
| **GOVERN** | No policies, roles, or accountability for automated hiring decisions. The contractor-classification argument shows governance was oriented around avoiding responsibility rather than assigning it. |
| **MAP** | The deployment context — employment decisions affecting a protected class under the ADEA — was never mapped as a high-risk use case requiring heightened scrutiny. |
| **MEASURE** | No measurement of disparate impact at any point: not before deployment, not during two years of operation. The "measure" function was entirely absent. |
| **MANAGE** | No monitoring, no response to the accumulating pattern of rejections, no remediation until a federal enforcement action. Risk was unmanaged until it became liability. |

---

## Key sources

- EEOC press release, "iTutorGroup to Pay $365,000 to Settle EEOC Discriminatory Hiring
  Suit," Sep 2023
  (https://www.eeoc.gov/newsroom/itutorgroup-pay-365000-settle-eeoc-discriminatory-hiring-suit)
- Foley & Lardner, "EEOC Targets AI-Based Hiring Practices in Landmark Settlement,"
  Aug 2023
  (https://www.foley.com/insights/publications/2023/08/eeoc-ai-based-hiring-practices-landmark-settlement/)
- Jackson Lewis, "EEOC Files for Consent Decree Settlement in AI Discrimination Case,"
  Aug 2023
  (https://www.jacksonlewis.com/insights/eeoc-files-consent-decree-settlement-ai-discrimination-case)
- Mondaq/Lexology, "EEOC Settles Over Recruiting Software in Possible First Ever
  AI-related Case," Sep 2023
  (http://www.mondaq.com/unitedstates/employee-rights-labour-relations/1369086/eeoc-settles-over-recruiting-software-in-possible-first-ever-ai-related-case)
- CDF Labor Law LLP summary of the settlement, Sep 2023
  (https://www.cdflaborlaw.com/blog/employer-paying-six-figure-settlement-based-on-eeoc-claims-that-ai-software-discriminated-against-older-applicants)

**Could not verify:** whether the screening software used machine learning or was
entirely rules-based — public sources, including the EEOC's own releases, describe
programmed age thresholds without technical detail. The "first AI settlement" framing
comes from commentators, not from a technical finding. Exact filing/approval dates
vary by a day across secondary sources; the decree was filed on or about 9 Aug 2023
and approved/announced 8 Sep 2023.
