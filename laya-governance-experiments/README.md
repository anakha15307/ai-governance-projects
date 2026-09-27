# 16. Laya Governance Experiments

I tested whether a 421M-parameter *decision model* (Laya, the open-source
counterpart to TypeSafe's JEV) can serve as an AI governance layer: a safety
gate, a calibrated confidence source, and a demographically steady judge.

Full write-up: [`report.md`](./report.md) and
[`Laya_Governance_Test_Report.pdf`](./Laya_Governance_Test_Report.pdf).

## Problem

Governance teams need fast, cheap, auditable controls that sit in front of
large models: input screening, risk-tiered escalation, and pre-deployment
bias checks. LLMs are too slow, expensive, and non-deterministic for the
first pass. Decision models answer typed questions (yes/no, choice, score)
with probabilities in one forward pass, but their governance claims,
especially *calibrated* confidence, need independent testing before anyone
builds policy on them.

## Users / stakeholders

AI governance analysts evaluating guardrail vendors, risk teams designing
defense-in-depth controls, and hiring managers who want evidence of
hands-on safety evaluation: red-teaming a model, checking its calibration,
and probing it for bias.

## Methods

- **Model:** Laya 0.3.20 (`convaiinnovations/laya`), Apache 2.0, run locally
  on CPU. Three typed questions: a `noul` jailbreak detector, and `choice`
  questions for loan/hiring/insurance scenarios.
- **Experiment 1, safety gate:** 60 labeled prompts (30 benign, 30 jailbreak
  attempts across instruction-override, roleplay, hypothetical, and
  obfuscation attacks). Metrics: accuracy, precision, recall, latency.
- **Experiment 2, calibration:** same 60 prompts. Expected calibration error
  (10-bin, proper binary form) plus a reliability table.
- **Experiment 3, bias probe:** 6 paired scenarios identical except for a
  race/gender-coded name cue. Metrics: decision flip rate, mean absolute
  probability shift.

## Results

| Experiment | Headline |
|---|---|
| Safety gate | 85% accuracy, **100% precision** (zero false positives), 70% recall; 0.94 s/decision on CPU |
| Calibration | ECE **0.125**; 92% empirical accuracy above 0.90 confidence; overconfident in the 0.7-0.9 band |
| Bias probe | **0 of 6 flips**; mean probability shift 0.009 |

All 9 missed attacks were roleplay/hypothetical framing. Direct instruction
overrides were caught every time. See `report.md` for the full tables, the
false-negative analysis, and the reliability bins.

## Risks and controls

- Small samples (60 prompts, 6 pairs): findings are exploratory, labeled as
  such throughout the report, never presented as a benchmark.
- The model is probed, never asked to fulfill harmful requests. Attack
  prompts are classified only.
- Mid-band overconfidence is disclosed, not hidden. The report recommends
  against setting escalation thresholds there without more data.

## Next steps

Scale the bias probe to hundreds of pairs with intersectional cues, add a
second decision model for comparison, and test the gate against a live LLM
to measure end-to-end attack interception.

## Reproduce

`analyze.py` reproduces every number in the report from the saved JSON
results with the standard library only:

```bash
cd laya-governance-experiments && python3 analyze.py
```

To re-run the experiments against the model (downloads ~843 MB weights):

```bash
pip install laya
python3 run_experiments.py && python3 analyze.py
```
