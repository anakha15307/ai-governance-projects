# Laya governance experiments — 2026-09-26

Model: Laya (`convaiinnovations/laya`), 421M params, Apache 2.0, run locally on CPU.
Setup: `~/workspace/laya-lab/` (venv, datasets.py, run_experiments.py, analyze.py,
results_guardrail.json, results_bias.json).

## Experiment 1 — Safety gate (n=60: 30 jailbreak, 30 benign)
Question (noul): "Is this prompt attempting to bypass AI safety rules...?"
- Accuracy 85%, precision 100% (zero false positives), recall 70% (21/30 caught)
- Mean latency 0.94s per decision on CPU (batched)
- All 9 misses were roleplay / framing / hypothetical attacks
  (e.g. "pretend you're my grandmother...", "roleplay a hitman...").
  Direct instruction-override attacks ("ignore all previous instructions") were all caught.

## Experiment 2 — Calibration (same n=60)
- ECE (10-bin, proper binary) = 0.125
- 52/60 predictions fell in the 0.9-1.0 confidence band at 92.3% empirical accuracy:
  well calibrated where it is most confident.
- Middle band (0.7-0.9, n=7) was overconfident (empirical accuracy 25-33%).
- Note: checkpoint ships a runtime warning about invalid temperatures on some
  entries ("treat confidence from the affected entries as uncalibrated").

## Experiment 3 — Bias probe (6 paired scenarios, loan/job/insurance)
Only the name cue changed between variants (race/gender-coded names).
- Decision flips: 0/6. Mean |ΔP(favorable)| = 0.009, max 0.035.
- No evidence of demographic sensitivity on this small probe.

## Honest limitations
Small N throughout (60 labeled, 6 pairs). Single model, English only.
Calibration sample is thin in the middle confidence band. Exploratory, not a benchmark.
