# AI Governance Dashboard

A static, fully self-contained HTML dashboard generated from a JSON risk
register. It is the "ship a live product" project of the AI governance
portfolio: a compliance dashboard with a real risk register, control tracking,
and overdue-action reporting that works offline when opened with `file://`.

## What the dashboard shows

- **Summary cards**: number of AI systems tracked, counts by risk tier
  (High-Risk / Limited / Minimal), overall control-compliance percentage, and
  the number of overdue actions.
- **Controls by status**: a pure-CSS bar chart breaking all controls across
  every system into Compliant / Partial / Non-compliant.
- **Open actions table**: every open action sorted by due date. Rows past
  their due date are highlighted red with an `OVERDUE` flag.
- **Per-system detail**: each system gets its own card with a colored
  risk-tier badge, owner team, deployment status, a controls table
  (with status dots), and its open actions. Buttons at the top filter the
  cards by risk tier (JavaScript is inlined, so filtering works offline).

## Risk register schema (`data/risk_register.json`)

Top-level fields:

| Field | Meaning |
| --- | --- |
| `as_of` | Report snapshot date (`YYYY-MM-DD`). Actions due before this date are flagged overdue. |
| `generated_note` | Free text; ignored by the build. |
| `systems` | List of AI systems. |

Each system:

| Field | Meaning |
| --- | --- |
| `name` | System name (string). |
| `owner_team` | Team responsible (string). |
| `risk_tier` | One of `High-Risk`, `Limited`, `Minimal`. |
| `deployment_status` | e.g. `Production`, `Pilot`, `In Development`. |
| `controls` | List of control objects. |
| `open_actions` | List of action objects. |

Each control: `name` (string), `owner` (string), `due_date` (`YYYY-MM-DD`),
`status`, one of `compliant`, `partial`, `non-compliant`.

Each open action: `description` (string), `owner` (string),
`due_date` (`YYYY-MM-DD`), `status`, one of `open`, `in-progress`,
`overdue`.

Example:

```json
{
  "name": "LoanAssist",
  "owner_team": "Consumer Lending",
  "risk_tier": "High-Risk",
  "deployment_status": "Production",
  "controls": [
    { "name": "Pre-deployment bias audit", "owner": "M. Okafor",
      "due_date": "2026-07-15", "status": "compliant" }
  ],
  "open_actions": [
    { "description": "Complete conformity assessment",
      "owner": "L. Tran", "due_date": "2026-10-01", "status": "in-progress" }
  ]
}
```

## How to update the data and regenerate

1. Edit `data/risk_register.json`, add systems, update control statuses,
   close actions by removing them from `open_actions` (or setting a status
   outside the open set). Dates must be `YYYY-MM-DD`.
2. Run `python3 build.py` (or `python3 build.py --demo`; both do the same, 
   regenerate from the sample data).
3. Open `dashboard.html` in a browser. No server or internet needed.

Only the Python standard library is used (`json`, `html`, `datetime`), so no
packages need installing and the build runs fully offline.

## Files

| File | Purpose |
| --- | --- |
| `data/risk_register.json` | Sample data: 7 fictional AI systems. |
| `build.py` | Reads the JSON, writes `dashboard.html`. |
| `dashboard.html` | Generated output: all CSS/JS inline, no external requests. |
| `README.md` | This file. |
