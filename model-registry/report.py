#!/usr/bin/env python3
"""Generate a self-contained HTML lineage report from the model registry.

Reads data/registry.json and writes lineage-report.html in this directory.
All CSS is inline and there are no external requests, so the file can be
opened offline or attached to an audit packet.

Usage:
  python report.py [--out lineage-report.html]
"""

from __future__ import annotations

import argparse
import html
import json
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
STORE_PATH = BASE_DIR / "data" / "registry.json"


def esc(text: object) -> str:
    return html.escape(str(text) if text is not None else "")


STATUS_COLORS = {
    "draft": "#6b7280",
    "in-review": "#b45309",
    "approved": "#15803d",
    "rejected": "#b91c1c",
}

TIER_COLORS = {
    "Prohibited": "#7f1d1d",
    "High-Risk": "#b91c1c",
    "Limited": "#b45309",
    "Minimal": "#15803d",
}


def badge(text: str, color: str) -> str:
    return (
        f'<span class="badge" style="background:{color}20;color:{color};'
        f'border:1px solid {color}55">{esc(text)}</span>'
    )


def model_card(model: dict, datasets: dict) -> str:
    status = model.get("status", "?")
    tier = model.get("risk_tier", "?")
    key = f"{model['name']}@{model['version']}"

    lineage_rows = []
    for entry in model.get("datasets", []):
        dkey = entry.get("dataset", "?")
        d = datasets.get(dkey, {})
        lineage_rows.append(
            "<li>"
            f"<strong>{esc(dkey)}</strong> "
            f"<em>({esc(entry.get('relation', '?'))})</em><br>"
            f"<span class=\"muted\">source: {esc(d.get('source', 'unknown'))} · "
            f"license: {esc(d.get('license', 'unknown'))}</span>"
            "</li>"
        )
    lineage_html = (
        f"<ul class=\"lineage\">{''.join(lineage_rows)}</ul>"
        if lineage_rows else "<p class=\"muted\">No datasets linked.</p>"
    )

    history_rows = []
    for h in model.get("approval_history", []):
        actor = esc(h.get("actor") or "-")
        note = f" - <em>{esc(h['note'])}</em>" if h.get("note") else ""
        history_rows.append(
            f"<li><strong>{esc(h['action'])}</strong> by {actor} "
            f"({esc(h.get('from', '?'))} → {esc(h.get('to', '?'))}) · "
            f"<span class=\"muted\">{esc(h.get('timestamp', ''))}</span>{note}</li>"
        )
    history_html = (
        f"<ul class=\"history\">{''.join(history_rows)}</ul>"
        if history_rows else "<p class=\"muted\">No approval events recorded.</p>"
    )

    return f"""
    <section class="card">
      <div class="card-head">
        <h2>{esc(key)}</h2>
        <div class="badges">{badge(tier, TIER_COLORS.get(tier, '#333'))}
        {badge(status, STATUS_COLORS.get(status, '#333'))}</div>
      </div>
      <p><strong>Owner:</strong> {esc(model.get('owner', '-'))}</p>
      <p><strong>Intended use:</strong> {esc(model.get('intended_use', '-'))}</p>
      <h3>Dataset lineage</h3>
      {lineage_html}
      <h3>Approval history</h3>
      {history_html}
    </section>
    """


def build_html(store: dict) -> str:
    models = [store["models"][k] for k in sorted(store["models"])]
    datasets = store.get("datasets", {})
    counts = {}
    for m in models:
        counts[m.get("status", "?")] = counts.get(m.get("status", "?"), 0) + 1
    summary = " · ".join(f"{k}: {v}" for k, v in sorted(counts.items())) or "empty registry"
    cards = "\n".join(model_card(m, datasets) for m in models)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>AI Model Registry: Lineage &amp; Approvals Report</title>
<style>
  * {{ box-sizing: border-box; }}
  body {{ font-family: -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
         margin: 0; color: #1f2937; background: #f9fafb; }}
  header {{ background: #111827; color: #f9fafb; padding: 2rem 2.5rem; }}
  header h1 {{ margin: 0 0 .25rem; font-size: 1.6rem; }}
  header p {{ margin: .25rem 0; color: #9ca3af; }}
  main {{ max-width: 960px; margin: 0 auto; padding: 2rem 1.5rem 3rem; }}
  .card {{ background: #fff; border: 1px solid #e5e7eb; border-radius: 12px;
           padding: 1.5rem 1.75rem; margin-bottom: 1.5rem;
           box-shadow: 0 1px 2px rgba(0,0,0,.04); }}
  .card-head {{ display: flex; justify-content: space-between; align-items: center;
                gap: 1rem; flex-wrap: wrap; }}
  .card-head h2 {{ margin: 0; font-size: 1.25rem; font-family: ui-monospace, Menlo, monospace; }}
  .badges {{ display: flex; gap: .5rem; }}
  .badge {{ padding: .25rem .75rem; border-radius: 999px; font-size: .8rem; font-weight: 600; }}
  h3 {{ margin: 1.25rem 0 .5rem; font-size: 1rem; color: #374151; }}
  p {{ margin: .4rem 0; line-height: 1.5; }}
  .muted {{ color: #6b7280; }}
  ul.lineage, ul.history {{ margin: .25rem 0; padding-left: 1.25rem; line-height: 1.6; }}
  footer {{ text-align: center; color: #9ca3af; font-size: .8rem; padding: 1.5rem; }}
</style>
</head>
<body>
<header>
  <h1>AI Model Registry: Lineage &amp; Approvals Report</h1>
  <p>{esc(summary)} · {len(datasets)} datasets registered</p>
  <p>Generated offline from the registry JSON store. No external data sources.</p>
</header>
<main>
{cards if cards else "<p class=\"muted\">No models registered yet.</p>"}
</main>
<footer>AI governance portfolio project: model registry</footer>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate lineage-report.html from the registry.")
    parser.add_argument("--out", default="lineage-report.html",
                        help="output filename (written in the project directory)")
    args = parser.parse_args()

    if not STORE_PATH.exists():
        print(f"error: no registry found at {STORE_PATH} (run registry.py or seed.py first)",
              file=sys.stderr)
        sys.exit(1)
    store = json.loads(STORE_PATH.read_text(encoding="utf-8"))
    out = BASE_DIR / args.out
    out.write_text(build_html(store), encoding="utf-8")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
