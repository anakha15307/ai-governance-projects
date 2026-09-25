# EU AI Act Risk-Tier Classifier

A rule-based CLI that reads a "system card" describing an AI system and assigns
an EU AI Act risk tier: **Prohibited, High-Risk, Limited Risk, or Minimal Risk**, 
with matched categories, rationale, reviewer flags, and a tier-appropriate
obligations checklist.

Python 3.12, standard library only, fully offline, no API keys.

## Why governance teams care

Risk-tiering is the first question in any AI governance workflow: it decides
whether a system can be deployed at all (prohibited), needs a conformity
assessment and EU database registration (high-risk), needs transparency
disclosures (limited risk), or faces no mandatory duties (minimal risk).
This tool makes that triage step explicit, repeatable, and reviewable. The
kind of boring-but-critical infrastructure that turns "we do AI governance"
from a slogan into an auditable process.

## Quickstart

```bash
# Classify a single system card
python3 classify.py --card examples/cv_screener.json

# Machine-readable output
python3 classify.py --card examples/cv_screener.json --json

# Classify all examples with a summary table
python3 classify.py --demo
# or
./run_examples.sh
```

A system card is a JSON object with these fields:

```json
{
  "name": "HireLens CV Screener",
  "description": "Reads incoming job applications and ranks applicants...",
  "intended_use": "Shortlist and rank job applicants for interviews.",
  "deployer_type": "HR software vendor, used by hiring teams",
  "data_types": ["CV text", "employment history", "education records"],
  "capabilities": ["resume screening", "candidate ranking"]
}
```

## How it works

Rules match keywords/regex against all card fields. Precedence is strict:
**Prohibited > High-Risk > Limited Risk > Minimal Risk**: the most severe
matched tier wins. When matches span multiple tiers, the report raises a
"competing signals" reviewer flag so a human confirms which use case dominates.
Deliberately ambiguous cards (see `examples/call_center_voice.json`) carry
their own borderline flags explaining the nuance.

Covered categories (simplified):

- **Prohibited:** social scoring, real-time remote biometric identification in
  public spaces, manipulative/subliminal techniques, emotion inference in
  work or education, individual criminal-risk scoring, untargeted facial
  scraping
- **High-Risk (Annex III):** biometrics, critical infrastructure, education,
  employment, essential services, law enforcement, migration/border, justice
  and democratic processes
- **Limited Risk (transparency):** chatbots/AI interaction, emotion
  recognition, biometric categorisation, AI-generated content
- **Minimal Risk:** everything else (spam filters, video-game NPCs, …)

## Example output

```
================================================================
System: HireLens CV Screener
EU AI Act risk tier: HIGH-RISK
================================================================

Matched categories:
  * [High-Risk] Employment and workers management (Annex III, point 4)
      AI used in recruitment, or in decisions affecting work-related
      relationships such as promotion, termination or task allocation,
      is high-risk.

Obligations checklist:
  [ ] Implement a risk management system (Art. 9).
  [ ] Ensure data governance and quality of training/validation/test data (Art. 10).
  [ ] Prepare technical documentation and keep automatically generated logs (Art. 11-12).
  [ ] Provide transparency information and instructions for use to deployers (Art. 13).
  [ ] Design for effective human oversight (Art. 14).
  [ ] Ensure appropriate accuracy, robustness and cybersecurity (Art. 15).
  [ ] Complete a conformity assessment and affix CE marking (Art. 43).
  [ ] Register the system in the EU database (Art. 71).
  [ ] Run post-market monitoring and report serious incidents (Art. 72-73).
```

Full demo output for all six examples is checked in at
[`examples/sample_output.txt`](examples/sample_output.txt).

## Disclaimer

**This is an educational tool, not legal advice.** The keyword-to-tier mapping
is deliberately simplified relative to the actual regulation text, the real
EU AI Act has exceptions, definitional thresholds, and case-by-case
assessments that a regex cannot capture. Always verify real deployments
against the official regulation and consult qualified counsel.
