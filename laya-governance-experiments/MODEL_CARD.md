# Model card: Laya safety gate experiment

## What this is

An evaluation of Laya, a 421M-parameter open-source decision model, as a
candidate AI governance layer: a safety gate that classifies prompts as
benign or jailbreak attempts, a source of calibrated confidence scores, and
a demographically steady judge. This card describes the experiment, not a
deployed system.

## Model details

- **Model:** Laya (open-source decision model), 421M parameters.
- **Version:** pinned by SHA-256 in `report.md`; exact package versions and
  CPU (AMD EPYC 9D25) are recorded there.
- **Role tested:** ternary governance gate (allow / block / escalate),
  confidence calibration, bias probe.

## Intended use of these results

To learn how a small decision model behaves under governance-style testing,
and to practice reporting evaluation results honestly: point estimates with
confidence intervals, a baseline comparison, and stated limits.

## Results (summary)

- 85% accuracy on 60 hand-built prompts (Wilson 95% CI 0.739-0.919).
- 100% precision on benign prompts (CI 0.845-1.000).
- 70% recall on jailbreaks; 9 of 30 missed, all via roleplay or hypothetical
  framing (CI 0.521-0.833).
- Expected calibration error 0.125 (bootstrap 95% CI 0.055-0.217).
- Bias probe: zero decision flips, under 1% average probability shift across
  six paired scenarios.
- 15-keyword rules baseline on the same prompts: 70% accuracy, 40% recall
  (baseline tuned on the test prompts, which flatters it).

Full details, reproduction commands, and the monitoring plan are in
[`report.md`](./report.md).

## Limitations

Small hand-built prompt set; no held-out test set; single hardware and seed;
no multilingual or multi-turn attacks; narrow bias probe (six scenarios, no
intersectional groups). The report states explicitly that nothing here is
evidence of production readiness.

## Out-of-scope uses

Do not use these results to claim Laya is safe for deployment, to certify
any system, or as a substitute for testing the actual model you plan to ship.
