# Model card: AI Governance Council experiment

## What this is

An experiment in multi-model oversight: three LLM seats independently
classify synthetic EU AI Act cases, deliberate on disagreements, and vote.
The council is the system under test; the "models" are the three seats plus
the voting procedure. This card describes the experiment, not a deployed
oversight body.

## System details

- **Seats:** Gemini 3.8 Flash (Google AI Studio), gpt-oss 120B (Groq),
  Ling 3.0 Flash (OpenRouter free tier). Model names and providers as of
  September 2026.
- **Procedure:** round 1 independent classification with confidence scores;
  round 2 deliberation on disagreements; majority vote with
  confidence-weighted tie-break.
- **Cases:** 8 synthetic EU AI Act use cases with my ground-truth tiers
  (`cases.json`).

## Results (summary)

- Council: 7/8 correct (87.5%), matching the best individual seat.
- Individuals: gpt-oss 7/8, Gemini 6/7 completed, Ling 4/5 completed.
- Only miss (case 7, AI product descriptions) is legally debatable under
  the AI Act's Art. 50(2) human-review exemption.
- Deliberation changed 1 vote across 5 deliberations.
- Confidence had no signal: 0.943 mean on correct votes vs 0.940 on wrong
  votes.
- Free-tier reliability was the binding constraint: Ling failed 8 of 16
  calls plus all 8 repair attempts; Groq was flawless; Gemini had one 429.

Full analysis: [`FINDINGS.md`](./FINDINGS.md). Every number reproduces from
`results.json` via `analyze.py`.

## Intended use of these results

To practice designing and reporting a multi-model oversight experiment
honestly, including the unflattering parts (free-tier flakiness, useless
confidence scores).

## Limitations

Eight synthetic cases, my own ground truth, one run, free-tier conditions
in September 2026. Not evidence that multi-model voting works in general.

## Out-of-scope uses

Do not cite this as proof that LLM councils are reliable classifiers, do
not use it for real EU AI Act determinations, and do not generalize the
reliability findings beyond the free tiers tested.
