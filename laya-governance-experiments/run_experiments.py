"""Run all three Laya AI-governance experiments and save raw results."""
import json, time, sys
sys.path.insert(0, "/home/hatch/workspace/laya-lab")
from datasets import GUARDRAIL_ITEMS, CALIBRATION_EXTRA_ITEMS, GUARDRAIL_QUESTION, BIAS_PAIRS
import laya

LAB = "/home/hatch/workspace/laya-lab"
agent = laya.load(f"{LAB}/laya-model")
print("model loaded", flush=True)

# ---------- Experiment 1+2: guardrail + calibration (same binary task) ----------
items = GUARDRAIL_ITEMS + CALIBRATION_EXTRA_ITEMS  # 60 labeled items
states = [text for text, _ in items]
labels = [label for _, label in items]
questions = {"risk": {"type": "noul", "instructions": GUARDRAIL_QUESTION}}

t0 = time.time()
results = agent.predict_batch(states, questions, batch_size=8)
elapsed = time.time() - t0

probs, preds = [], []
for r, (text, label) in zip(results, items):
    p = r["answers"]["risk"]["noul"]
    probs.append(p)
    preds.append(1 if p >= 0.5 else 0)

with open(f"{LAB}/results_guardrail.json", "w") as f:
    json.dump([{"text": t, "label": l, "p_jailbreak": p, "pred": pr}
               for (t, l), p, pr in zip(items, probs, preds)], f, indent=1)

tp = sum(1 for pr, l in zip(preds, labels) if pr == 1 and l == 1)
tn = sum(1 for pr, l in zip(preds, labels) if pr == 0 and l == 0)
fp = sum(1 for pr, l in zip(preds, labels) if pr == 1 and l == 0)
fn = sum(1 for pr, l in zip(preds, labels) if pr == 0 and l == 1)
acc = (tp + tn) / len(labels)
prec = tp / (tp + fp) if tp + fp else 0
rec = tp / (tp + fn) if tp + fn else 0
ece = laya.ece_score(__import__("numpy").array(probs),
                     __import__("numpy").array([p == l for p, l in zip(preds, labels)]).astype(float),
                     bins=10)
print(f"EXP1 n={len(labels)} acc={acc:.3f} prec={prec:.3f} rec={rec:.3f} "
      f"tp={tp} tn={tn} fp={fp} fn={fn} mean_latency={elapsed/len(labels):.2f}s ECE={ece:.3f}", flush=True)

# reliability bins for exp2
import numpy as np
probs_a = np.array(probs)
correct_a = np.array([p == l for p, l in zip(preds, labels)], dtype=float)
print("reliability (bin_lo-hi: n, mean_p, emp_acc):", flush=True)
for lo in [0.5, 0.6, 0.7, 0.8, 0.9]:
    m = (probs_a >= lo) & (probs_a < lo + 0.1) if lo < 0.9 else (probs_a >= lo)
    if m.sum():
        print(f"  {lo:.1f}-{lo+0.1:.1f}: n={m.sum()} mean_p={probs_a[m].mean():.3f} emp_acc={correct_a[m].mean():.3f}", flush=True)

# ---------- Experiment 3: bias probe ----------
bias_raw = []
for i, (template, cue_a, cue_b, question, options) in enumerate(BIAS_PAIRS):
    q = {"decision": {"type": "choice",
                      "instructions": question,
                      "criteria": {o: o for o in options}}}
    states = [template.format(cue=cue_a), template.format(cue=cue_b)]
    t0 = time.time()
    rs = agent.predict_batch(states, q, batch_size=2)
    dt = time.time() - t0
    bias_raw.append({"pair": i, "question": question, "options": options,
                     "cue_a": cue_a, "cue_b": cue_b,
                     "result_a": rs[0]["answers"]["decision"],
                     "result_b": rs[1]["answers"]["decision"],
                     "latency": dt})
    if i == 0:
        print("RAW choice answer (variant A):", json.dumps(rs[0]["answers"]["decision"], default=str)[:800], flush=True)

with open(f"{LAB}/results_bias.json", "w") as f:
    json.dump(bias_raw, f, indent=1, default=str)
print("done", flush=True)
