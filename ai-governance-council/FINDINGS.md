# AI Governance Council: findings

**Experiment:** three LLM seats (Gemini 3.8 Flash via Google AI Studio,
gpt-oss 120B via Groq, Ling 3.0 Flash via OpenRouter free tier) independently
classify 8 synthetic AI use cases under EU AI Act risk tiers
(Unacceptable / High-Risk / Limited Risk / Minimal Risk), then deliberate on
disagreements. Council verdict = majority vote, ties broken by mean
confidence. Run 2026-09-27. All prompts are synthetic; free tiers may use
prompts for model improvement, so nothing sensitive was submitted.

## Headline results

| | Accuracy | 95% CI |
|---|---|---|
| Council (majority + confidence tie-break) | 7/8 (87.5%) | 0.53-0.98 |
| Gemini 3.8 Flash (round 1) | 6/7 completed (85.7%) | 0.49-0.97 |
| gpt-oss 120B (round 1) | 7/8 (87.5%) | 0.53-0.98 |
| Ling 3.0 Flash (round 1) | 4/5 completed (80.0%) | 0.38-0.96 |

The council matched the best individual seat (gpt-oss) and beat the other
two. With n=8, every interval is wide: this is a pilot, not a benchmark.

## The one miss: case 7

AI-generated product descriptions with human editorial review before
publication. Ground truth assigned: Limited Risk (transparency obligation).
Council verdict: Minimal Risk (1-1 tie between Gemini at 0.95 confidence and
gpt-oss at 0.78, broken toward the more confident vote).

This miss deserves an asterisk: it is legally ambiguous, not a clear model
error. Article 50(2) of the EU AI Act exempts AI-generated text from
machine-disclosure obligations where it has undergone human review with
editorial responsibility, which is exactly what the case describes. Gemini's
Minimal Risk vote cited that exemption explicitly. Reasonable analysts
disagree here, and the council surfaced a genuine ambiguity rather than
making a simple mistake. If the ground truth is debatable, the council is
arguably 8/8.

## Deliberation: what actually happened

Deliberation ran on 5 of 8 cases. Across all of them, exactly **one** vote
changed: Gemini on case 8, which had failed round 1 with a quota error and
used the deliberation round to cast its first real vote (High-Risk, correct).
No seat was ever persuaded to change a cast vote. Cases 5 and 7 ended in
1-1 ties settled by the confidence rule.

Two lessons: (1) with only 8 cases and high round-1 agreement, deliberation
had little room to matter; (2) the confidence-weighted tie-breaker is
double-edged. It saved case 5 (Unacceptable at 0.96 beat High-Risk at 0.88)
and sank case 7 (Minimal at 0.95 beat Limited at 0.78).

## Confidence carried no signal

Mean confidence on correct round-1 votes: 0.943 (n=17). Mean confidence on
wrong votes: 0.940 (n=3). The models were equally sure when right and when
wrong, and the most confident wrong vote in the experiment (0.95, case 7)
decided the council's only miss. Any aggregation rule that trusts stated
confidence, as this council's tie-breaker does, inherits that miscalibration.

## Free-tier reliability: the infrastructure story

This experiment's binding constraint was not model quality but free-tier
reliability. 9 of 24 seat-case round-1 slots failed in the original run
(37.5%), and all 9 repair re-attempts failed again:

| Seat | Failures (original) | Cause | Repairs recovered |
|---|---|---|---|
| gpt-oss 120B (Groq) | 0/16 calls | - | - |
| Gemini 3.8 Flash (Google) | 1/16 (case 8 r1) | HTTP 429 quota | 0 (still 429) |
| Ling 3.0 Flash (OpenRouter free) | 8/16 | empty / non-JSON responses | 0 of 8 |

Ling failed all 5 deliberation-round prompts in the original run and all 5
again on repair: 40 consecutive empty or unparseable responses across both
attempts for the longer round-2 prompt format. Groq was flawless across all
16 calls. Practical takeaway: on free tiers, output-format compliance varies
more than classification accuracy, and any multi-model design needs a
retry-and-quorum policy, not just a voting rule.

## Agreement

Pairwise round-1 agreement on completed votes: gpt-oss vs Ling 5/5, Gemini vs
gpt-oss 5/7, Gemini vs Ling 3/4. Cases 1, 2, 3 were unanimous in round 1.

## Limitations

- n=8 synthetic cases, written and labeled by one person (me). No held-out
  set, no independent labeling, single run.
- Ground truth for case 7 is debatable (see above).
- Free-tier failures mean Ling's individual accuracy rests on 5 completed
  votes, not 8.
- Confidence intervals are Wilson score; with n=8 they are wide by
  construction.

## Reproducibility

`cases.json` holds the 8 cases. `run_council.py` runs the experiment
(requires the provider CLI clients and stored credentials).
`repair_votes.py` re-runs failed votes without altering recorded verdicts.
`analyze.py` reproduces every number above from `results.json`.
