# AI Governance Council

A real multi-model experiment: three LLM seats (Gemini 3.8 Flash via Google
AI Studio, gpt-oss 120B via Groq, Ling 3.0 Flash via OpenRouter's free tier)
independently classify 8 synthetic AI use cases under EU AI Act risk tiers,
then deliberate on disagreements. Council verdicts use majority vote with a
confidence-weighted tie-breaker.

**Result:** council 7/8 correct (87.5%), matching the best individual seat.
The full analysis, including a reliability story about free-tier API
flakiness mattering more than model quality, is in [FINDINGS.md](./FINDINGS.md).

## Contents

| File | What it is |
|---|---|
| `cases.json` | The 8 synthetic EU AI Act cases with ground-truth tiers |
| `run_council.py` | Runs round 1 (independent votes) + round 2 (deliberation on disagreement) |
| `repair_votes.py` | Re-runs failed votes with identical prompts; never alters recorded verdicts |
| `analyze.py` | Reproduces every number in FINDINGS.md from `results.json` |
| `results.json` | All votes, justifications, confidences, and failures (repaired votes flagged) |
| `FINDINGS.md` | Results, the case-7 ambiguity, deliberation analysis, reliability findings |

All prompts are synthetic. Free tiers may use prompts for model improvement,
so nothing sensitive was submitted. Running `run_council.py` requires the
provider CLI clients and stored credentials used in the original setup.
