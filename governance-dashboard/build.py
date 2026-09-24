#!/usr/bin/env python3
"""Build a static, fully self-contained AI governance dashboard from the risk register.

Usage:
    python3 build.py            Regenerate dashboard.html from data/risk_register.json
    python3 build.py --demo     Same as above (explicit demo mode)

The output file is a single HTML page with all CSS and JavaScript inlined, so it
renders offline when opened with file:// in any modern browser. No network
requests, no external fonts, no CDN dependencies.
"""

from __future__ import annotations

import datetime
import html
import json
import os
import sys

# --- Paths (relative to this script so the project is self-contained) ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "risk_register.json")
OUT_PATH = os.path.join(BASE_DIR, "dashboard.html")

# --- Domain constants ----------------------------------------------------------
TIER_ORDER = ["High-Risk", "Limited", "Minimal"]
CONTROL_STATUSES = ["compliant", "partial", "non-compliant"]
# Tier label -> (badge background, badge text color)
TIER_STYLES = {
    "High-Risk": ("#fde2e2", "#a31621"),
    "Limited": ("#fef3d8", "#92600a"),
    "Minimal": ("#ddf3e4", "#166b37"),
}
# Control status -> (bar/dot color, display label)
STATUS_STYLES = {
    "compliant": ("#1e8e4d", "Compliant"),
    "partial": ("#d9910c", "Partial"),
    "non-compliant": ("#d64545", "Non-compliant"),
}
ACTION_OPEN_STATUSES = {"open", "in-progress", "overdue"}


def parse_date(value: str) -> datetime.date | None:
    """Parse an ISO YYYY-MM-DD date string; return None if blank/invalid."""
    try:
        return datetime.date.fromisoformat(value.strip())
    except (AttributeError, ValueError):
        return None


def esc(value) -> str:
    """HTML-escape a value for safe embedding in the generated page."""
    return html.escape(str(value), quote=True)


def load_register(path: str) -> dict:
    """Load and lightly validate the risk register JSON."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if "systems" not in data or not isinstance(data["systems"], list):
        raise ValueError("risk_register.json must contain a 'systems' list")
    return data


def aggregate(data: dict, today: datetime.date) -> dict:
    """Compute summary statistics used by the dashboard cards and chart."""
    systems = data["systems"]
    tier_counts = {tier: 0 for tier in TIER_ORDER}
    status_counts = {s: 0 for s in CONTROL_STATUSES}
    actions = []  # flattened: (due_date, system_name, action)

    for system in systems:
        tier_counts[system.get("risk_tier", "Minimal")] = (
            tier_counts.get(system.get("risk_tier", "Minimal"), 0) + 1
        )
        for control in system.get("controls", []):
            status = control.get("status")
            if status in status_counts:
                status_counts[status] += 1
        for action in system.get("open_actions", []):
            if action.get("status") in ACTION_OPEN_STATUSES:
                actions.append(
                    {
                        "system": system.get("name", "?"),
                        "description": action.get("description", ""),
                        "owner": action.get("owner", ""),
                        "due_date": action.get("due_date", ""),
                        "status": action.get("status", ""),
                    }
                )

    total_controls = sum(status_counts.values())
    compliance_pct = (
        round(100 * status_counts["compliant"] / total_controls, 1)
        if total_controls
        else 0.0
    )
    overdue = [
        a for a in actions if (parse_date(a["due_date"]) or today) < today
    ]
    actions.sort(key=lambda a: a["due_date"] or "9999")

    return {
        "system_count": len(systems),
        "tier_counts": tier_counts,
        "status_counts": status_counts,
        "total_controls": total_controls,
        "compliance_pct": compliance_pct,
        "actions": actions,
        "overdue": overdue,
    }


# --- HTML rendering -------------------------------------------------------------
CSS = """
:root {
  --bg: #f5f7fa;
  --card: #ffffff;
  --ink: #1c2530;
  --muted: #66717f;
  --line: #e3e8ef;
  --accent: #1f5eff;
  --red: #d64545;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
               Helvetica, Arial, sans-serif;
  background: var(--bg);
  color: var(--ink);
}
header.topbar {
  background: #141c2b;
  color: #fff;
  padding: 28px 32px;
}
header.topbar h1 { margin: 0 0 6px; font-size: 24px; font-weight: 650; }
header.topbar p { margin: 0; color: #a9b4c4; font-size: 13px; }
main { max-width: 1080px; margin: 0 auto; padding: 28px 24px 64px; }
section { margin-bottom: 34px; }
h2.section-title { font-size: 17px; margin: 0 0 14px; font-weight: 650; }
.cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 14px; }
.card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 10px;
  padding: 18px;
}
.card .value { font-size: 30px; font-weight: 700; line-height: 1.1; }
.card .label { color: var(--muted); font-size: 13px; margin-top: 6px; }
.card.accent { border-top: 4px solid var(--accent); }
.card.red    { border-top: 4px solid var(--red); }
.card .value.red { color: var(--red); }
.chart { display: grid; gap: 10px; }
.chart-row { display: grid; grid-template-columns: 130px 1fr 60px; gap: 10px; align-items: center; font-size: 14px; }
.bar-track { background: var(--line); border-radius: 6px; height: 22px; overflow: hidden; }
.bar-fill { height: 100%; border-radius: 6px; }
.chart-row .count { text-align: right; color: var(--muted); font-variant-numeric: tabular-nums; }
table { width: 100%; border-collapse: collapse; background: var(--card); font-size: 14px;
        border: 1px solid var(--line); border-radius: 10px; overflow: hidden; }
th, td { text-align: left; padding: 10px 14px; border-bottom: 1px solid var(--line); vertical-align: top; }
th { background: #eef1f6; font-size: 12px; text-transform: uppercase; letter-spacing: .05em; color: var(--muted); }
tr:last-child td { border-bottom: none; }
tr.overdue td { background: #fdecec; color: #a31621; font-weight: 600; }
tr.overdue td .due-flag { display: inline-block; background: var(--red); color: #fff;
  font-size: 11px; font-weight: 700; border-radius: 4px; padding: 2px 7px; margin-left: 8px; }
.badge { display: inline-block; font-size: 12px; font-weight: 700; border-radius: 20px; padding: 3px 12px; }
.dot { display: inline-block; width: 10px; height: 10px; border-radius: 50%; margin-right: 7px; vertical-align: 1px; }
.system { background: var(--card); border: 1px solid var(--line); border-radius: 12px;
          padding: 20px 22px; margin-bottom: 18px; }
.system h3 { margin: 0 0 4px; font-size: 18px; display: inline-block; }
.system .meta { color: var(--muted); font-size: 13px; margin: 8px 0 14px; }
.system table { margin-top: 10px; }
.system h4 { font-size: 14px; margin: 18px 0 8px; }
.system .no-actions { color: var(--muted); font-size: 13px; font-style: italic; }
.filters { margin-bottom: 16px; }
.filters button {
  border: 1px solid var(--line); background: var(--card); color: var(--ink);
  border-radius: 20px; padding: 7px 16px; margin-right: 8px; font-size: 13px; cursor: pointer;
}
.filters button.active { background: #141c2b; color: #fff; border-color: #141c2b; }
.note { color: var(--muted); font-size: 13px; }
footer { color: var(--muted); font-size: 12px; text-align: center; padding-bottom: 40px; }
"""

JS = """
// Tiny inline behavior: filter the per-system cards by risk tier.
(function () {
  var buttons = document.querySelectorAll('.filters button');
  buttons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      buttons.forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      var want = btn.getAttribute('data-tier');
      document.querySelectorAll('.system').forEach(function (card) {
        card.style.display =
          (want === 'All' || card.getAttribute('data-tier') === want) ? '' : 'none';
      });
    });
  });
})();
"""


def badge(tier: str) -> str:
    """Render a colored risk-tier badge."""
    bg, fg = TIER_STYLES.get(tier, ("#e8ebf0", "#333"))
    return (
        f'<span class="badge" style="background:{bg};color:{fg}">{esc(tier)}</span>'
    )


def status_cell(status: str) -> str:
    """Render a control status with its color dot."""
    color, label = STATUS_STYLES.get(status, ("#999", esc(status)))
    return f'<span class="dot" style="background:{color}"></span>{esc(label)}'


def render(data: dict, stats: dict, today: datetime.date) -> str:
    """Render the complete dashboard HTML page."""
    parts: list[str] = []

    # ---- Header ----
    as_of = esc(data.get("as_of", str(today)))
    parts.append(
        """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AI Governance Dashboard</title>
<style>""" + CSS + """</style>
</head>
<body>
<header class="topbar">
  <h1>AI Governance Dashboard</h1>
  <p>Risk register snapshot as of """ + as_of + """</p>
</header>
<main>
"""
    )

    # ---- Summary cards ----
    parts.append('<section><h2 class="section-title">Summary</h2><div class="cards">\n')
    parts.append(
        f'<div class="card"><div class="value">{stats["system_count"]}</div>'
        '<div class="label">AI systems tracked</div></div>\n'
    )
    for tier in TIER_ORDER:
        n = stats["tier_counts"].get(tier, 0)
        parts.append(
            f'<div class="card"><div class="value">{n}</div>'
            f'<div class="label">{esc(tier)} systems</div></div>\n'
        )
    parts.append(
        f'<div class="card accent"><div class="value">{stats["compliance_pct"]}%</div>'
        f'<div class="label">Controls compliant ({stats["status_counts"]["compliant"]}/'
        f'{stats["total_controls"]})</div></div>\n'
    )
    overdue_n = len(stats["overdue"])
    parts.append(
        f'<div class="card red"><div class="value red">{overdue_n}</div>'
        '<div class="label">Overdue actions</div></div>\n'
    )
    parts.append("</div></section>\n")

    # ---- Controls breakdown bar chart (pure CSS) ----
    parts.append(
        '<section><h2 class="section-title">Controls by Status</h2><div class="chart">\n'
    )
    total = stats["total_controls"] or 1  # avoid division by zero
    for status in CONTROL_STATUSES:
        count = stats["status_counts"][status]
        pct = round(100 * count / total, 1)
        color, label = STATUS_STYLES[status]
        parts.append(
            f'<div class="chart-row"><span>{esc(label)}</span>'
            f'<div class="bar-track"><div class="bar-fill" '
            f'style="width:{pct}%;background:{color}"></div></div>'
            f'<span class="count">{count} ({pct}%)</span></div>\n'
        )
    parts.append("</div></section>\n")

    # ---- Actions table (overdue highlighted red) ----
    parts.append(
        '<section><h2 class="section-title">Open Actions (by due date)</h2>\n'
        '<table><thead><tr><th>System</th><th>Action</th><th>Owner</th>'
        "<th>Due date</th><th>Status</th></tr></thead><tbody>\n"
    )
    if stats["actions"]:
        for action in stats["actions"]:
            due = parse_date(action["due_date"])
            is_overdue = (due or today) < today
            row_class = ' class="overdue"' if is_overdue else ""
            due_html = esc(action["due_date"])
            if is_overdue:
                due_html += '<span class="due-flag">OVERDUE</span>'
            parts.append(
                f"<tr{row_class}><td>{esc(action['system'])}</td>"
                f"<td>{esc(action['description'])}</td>"
                f"<td>{esc(action['owner'])}</td>"
                f"<td>{due_html}</td>"
                f"<td>{esc(action['status'])}</td></tr>\n"
            )
    else:
        parts.append(
            '<tr><td colspan="5" class="note">No open actions. All clear.</td></tr>\n'
        )
    parts.append("</tbody></table></section>\n")

    # ---- Per-system detail ----
    filter_buttons = (
        '<button class="active" data-tier="All">All</button>'
        + "".join(
            f'<button data-tier="{esc(t)}">{esc(t)}</button>' for t in TIER_ORDER
        )
    )
    parts.append(
        '<section><h2 class="section-title">Systems</h2>'
        '<div class="filters">' + filter_buttons + "</div>\n"
    )
    for system in data["systems"]:
        name = esc(system.get("name", "?"))
        tier = system.get("risk_tier", "Minimal")
        parts.append(
            f'<div class="system" data-tier="{esc(tier)}">'
            f"<h3>{name}</h3> {badge(tier)}"
            f'<div class="meta">Owner: {esc(system.get("owner_team", "—"))}'
            f' &nbsp;·&nbsp; Status: {esc(system.get("deployment_status", "—"))}</div>\n'
        )
        # Controls table
        parts.append(
            "<h4>Controls</h4>\n<table><thead><tr><th>Control</th><th>Owner</th>"
            "<th>Due date</th><th>Status</th></tr></thead><tbody>\n"
        )
        for control in system.get("controls", []):
            parts.append(
                f"<tr><td>{esc(control.get('name', ''))}</td>"
                f"<td>{esc(control.get('owner', ''))}</td>"
                f"<td>{esc(control.get('due_date', ''))}</td>"
                f"<td>{status_cell(control.get('status', ''))}</td></tr>\n"
            )
        parts.append("</tbody></table>\n")
        # Open actions
        open_actions = [
            a
            for a in system.get("open_actions", [])
            if a.get("status") in ACTION_OPEN_STATUSES
        ]
        parts.append("<h4>Open actions</h4>\n")
        if open_actions:
            parts.append("<table><thead><tr><th>Action</th><th>Owner</th>"
                         "<th>Due date</th><th>Status</th></tr></thead><tbody>\n")
            for action in open_actions:
                due = parse_date(action.get("due_date", ""))
                flag = ' class="overdue"' if (due or today) < today else ""
                parts.append(
                    f"<tr{flag}><td>{esc(action.get('description', ''))}</td>"
                    f"<td>{esc(action.get('owner', ''))}</td>"
                    f"<td>{esc(action.get('due_date', ''))}</td>"
                    f"<td>{esc(action.get('status', ''))}</td></tr>\n"
                )
            parts.append("</tbody></table>\n")
        else:
            parts.append('<p class="no-actions">No open actions.</p>\n')
        parts.append("</div>\n")
    parts.append("</section>\n")

    parts.append(
        """</main>
<footer>Generated by build.py from data/risk_register.json &mdash; static, offline-capable.</footer>
<script>""" + JS + """</script>
</body>
</html>
"""
    )
    return "".join(parts)


def build(demo: bool = False) -> str:
    """Load the register, render the dashboard, write it to disk."""
    data = load_register(DATA_PATH)
    # Snapshot date from the register keeps overdue math stable per report.
    as_of = parse_date(data.get("as_of", "")) or datetime.date.today()
    stats = aggregate(data, as_of)
    page = render(data, stats, as_of)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(page)
    mode = "demo " if demo else ""
    print(f"{mode}dashboard written to {OUT_PATH}")
    print(
        f"  {stats['system_count']} systems, "
        f"{stats['total_controls']} controls "
        f"({stats['compliance_pct']}% compliant), "
        f"{len(stats['overdue'])} overdue actions"
    )
    return OUT_PATH


def main(argv: list[str]) -> int:
    args = set(argv[1:])
    if args - {"--demo"}:
        print("Usage: python3 build.py [--demo]", file=sys.stderr)
        return 2
    build(demo="--demo" in args)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
