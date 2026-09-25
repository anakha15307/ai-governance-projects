#!/usr/bin/env python3
"""Model Registry CLI: dataset lineage and approval workflow for AI governance.

A tiny, offline model registry backed by a single JSON file. It answers two
questions every AI governance program must be able to answer at audit time:

  1. "Which datasets was this model trained on?" (dataset lineage / provenance)
  2. "Who approved this model for production, and on what basis?" (oversight)

State machine (models):  draft --submit--> in-review --approve--> approved
                                            in-review --reject--> rejected
                                          rejected --submit--> in-review (resubmission)

Usage examples:
  python registry.py register-model --name cv-screener --version 1.2 \\
      --owner "Talent Platform" --intended-use "Screen CVs for recruiters" \\
      --risk-tier High-Risk
  python registry.py register-dataset --name resumes --version 2024.1 \\
      --source "Internal portal exports" --license "Proprietary"
  python registry.py link --model cv-screener --version 1.2 \\
      --dataset resumes --dataset-version 2024.1 --relation trained-on
  python registry.py submit --model cv-screener --version 1.2
  python registry.py approve --model cv-screener --version 1.2 \\
      --reviewer "M. Okafor" --note "Bias audit passed."
  python registry.py list
  python registry.py show --model cv-screener --version 1.2
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
STORE_PATH = DATA_DIR / "registry.json"

RISK_TIERS = ["Prohibited", "High-Risk", "Limited", "Minimal"]
STATUSES = ["draft", "in-review", "approved", "rejected"]

# (from_status, to_status) -> action that performs the transition
VALID_TRANSITIONS = {
    ("draft", "in-review"): "submit",
    ("rejected", "in-review"): "submit",   # allow resubmission after rejection
    ("in-review", "approved"): "approve",
    ("in-review", "rejected"): "reject",
}

RELATIONS = ["trained-on", "fine-tuned-on", "evaluated-on"]


# --------------------------------------------------------------------------
# Store helpers
# --------------------------------------------------------------------------

def _now() -> str:
    """Current UTC time as an ISO-8601 string."""
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def model_key(name: str, version: str) -> str:
    return f"{name}@{version}"


def dataset_key(name: str, version: str) -> str:
    return f"{name}@{version}"


def load_store() -> dict:
    """Load the registry, creating an empty one if needed."""
    if not STORE_PATH.exists():
        return {"models": {}, "datasets": {}}
    with open(STORE_PATH, "r", encoding="utf-8") as fh:
        return json.load(fh)


def save_store(store: dict) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    tmp = STORE_PATH.with_suffix(".json.tmp")
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(store, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    tmp.replace(STORE_PATH)


def die(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    sys.exit(1)


def require_model(store: dict, name: str, version: str) -> dict:
    key = model_key(name, version)
    model = store["models"].get(key)
    if model is None:
        die(f"no such model: {key!r} (register it first with register-model)")
    return model


def require_dataset(store: dict, name: str, version: str) -> dict:
    key = dataset_key(name, version)
    dataset = store["datasets"].get(key)
    if dataset is None:
        die(f"no such dataset: {key!r} (register it first with register-dataset)")
    return dataset


# --------------------------------------------------------------------------
# Commands
# --------------------------------------------------------------------------

def cmd_register_model(args: argparse.Namespace) -> None:
    store = load_store()
    key = model_key(args.name, args.version)
    if key in store["models"]:
        die(f"model {key!r} already exists")
    store["models"][key] = {
        "name": args.name,
        "version": args.version,
        "owner": args.owner,
        "intended_use": args.intended_use,
        "risk_tier": args.risk_tier,
        "status": "draft",
        "datasets": [],            # list of {"dataset": key, "relation": ...}
        "approval_history": [],    # list of {"action","actor","timestamp","note"}
        "created_at": _now(),
        "updated_at": _now(),
    }
    save_store(store)
    print(f"registered model {key} (draft, risk tier: {args.risk_tier})")


def cmd_register_dataset(args: argparse.Namespace) -> None:
    store = load_store()
    key = dataset_key(args.name, args.version)
    if key in store["datasets"]:
        die(f"dataset {key!r} already exists")
    store["datasets"][key] = {
        "name": args.name,
        "version": args.version,
        "source": args.source,
        "license": args.license,
        "created_at": _now(),
    }
    save_store(store)
    print(f"registered dataset {key}")


def cmd_link(args: argparse.Namespace) -> None:
    store = load_store()
    model = require_model(store, args.model, args.version)
    require_dataset(store, args.dataset, args.dataset_version)
    dkey = dataset_key(args.dataset, args.dataset_version)
    if any(entry["dataset"] == dkey for entry in model["datasets"]):
        die(f"model {model_key(args.model, args.version)!r} is already linked to {dkey!r}")
    model["datasets"].append({"dataset": dkey, "relation": args.relation})
    model["updated_at"] = _now()
    save_store(store)
    print(f"linked {dkey} -> {model_key(args.model, args.version)} ({args.relation})")


def _transition(store: dict, model: dict, to_status: str, actor: str | None, note: str | None) -> None:
    from_status = model["status"]
    action = VALID_TRANSITIONS.get((from_status, to_status))
    if action is None:
        die(
            f"cannot move model {model_key(model['name'], model['version'])!r} "
            f"from {from_status!r} to {to_status!r} "
            f"(valid: draft -> submit -> in-review -> approve/reject)"
        )
    model["status"] = to_status
    model["updated_at"] = _now()
    model["approval_history"].append({
        "action": action,
        "actor": actor,
        "from": from_status,
        "to": to_status,
        "timestamp": _now(),
        "note": note,
    })
    save_store(store)
    key = model_key(model["name"], model["version"])
    past_tense = {"submit": "submitted", "approve": "approved", "reject": "rejected"}[action]
    print(f"{past_tense} {key}: {from_status} -> {to_status}")


def cmd_submit(args: argparse.Namespace) -> None:
    store = load_store()
    model = require_model(store, args.model, args.version)
    _transition(store, model, "in-review", actor=args.by or model["owner"], note=args.note)


def cmd_approve(args: argparse.Namespace) -> None:
    store = load_store()
    model = require_model(store, args.model, args.version)
    _transition(store, model, "approved", actor=args.reviewer, note=args.note)


def cmd_reject(args: argparse.Namespace) -> None:
    store = load_store()
    model = require_model(store, args.model, args.version)
    _transition(store, model, "rejected", actor=args.reviewer, note=args.note)


def cmd_list(_args: argparse.Namespace) -> None:
    store = load_store()
    rows = []
    for key in sorted(store["models"]):
        m = store["models"][key]
        datasets = ", ".join(d["dataset"] for d in m["datasets"]) or "-"
        rows.append([m["name"], m["version"], m["risk_tier"], m["status"],
                     m["owner"], datasets])
    if not rows:
        print("no models registered")
        return
    headers = ["Model", "Version", "Risk tier", "Status", "Owner", "Datasets"]
    widths = [max(len(headers[i]), max(len(r[i]) for r in rows)) for i in range(len(headers))]
    line = "  ".join(h.ljust(widths[i]) for i, h in enumerate(headers))
    print(line)
    print("-" * len(line))
    for r in rows:
        print("  ".join(r[i].ljust(widths[i]) for i in range(len(headers))))


def cmd_show(args: argparse.Namespace) -> None:
    store = load_store()
    model = require_model(store, args.model, args.version)
    print(f"Model:   {model['name']} {model['version']}")
    print(f"Owner:   {model['owner']}")
    print(f"Use:     {model['intended_use']}")
    print(f"Risk:    {model['risk_tier']}")
    print(f"Status:  {model['status']}")
    print(f"Created: {model['created_at']}")
    print("\nDataset lineage:")
    if not model["datasets"]:
        print("  (none)")
    for entry in model["datasets"]:
        d = store["datasets"].get(entry["dataset"], {})
        print(f"  - {entry['dataset']} [{entry['relation']}]")
        if d:
            print(f"      source: {d['source']} | license: {d['license']}")
    print("\nApproval history:")
    if not model["approval_history"]:
        print("  (none)")
    for h in model["approval_history"]:
        actor = h["actor"] or "-"
        note = f" - {h['note']}" if h["note"] else ""
        print(f"  - {h['timestamp']}: {h['action']} by {actor} ({h['from']} -> {h['to']}){note}")


# --------------------------------------------------------------------------
# CLI wiring
# --------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="registry.py",
        description="Model registry: dataset lineage + approval workflow (offline, JSON-backed).",
    )
    sub = p.add_subparsers(dest="command", required=True)

    s = sub.add_parser("register-model", help="register a new model (starts as draft)")
    s.add_argument("--name", required=True)
    s.add_argument("--version", required=True)
    s.add_argument("--owner", required=True)
    s.add_argument("--intended-use", required=True)
    s.add_argument("--risk-tier", required=True, choices=RISK_TIERS)
    s.set_defaults(func=cmd_register_model)

    s = sub.add_parser("register-dataset", help="register a new dataset")
    s.add_argument("--name", required=True)
    s.add_argument("--version", required=True)
    s.add_argument("--source", required=True)
    s.add_argument("--license", required=True)
    s.set_defaults(func=cmd_register_dataset)

    s = sub.add_parser("link", help="record dataset lineage for a model")
    s.add_argument("--model", required=True)
    s.add_argument("--version", required=True, help="model version")
    s.add_argument("--dataset", required=True)
    s.add_argument("--dataset-version", required=True)
    s.add_argument("--relation", default="trained-on", choices=RELATIONS)
    s.set_defaults(func=cmd_link)

    s = sub.add_parser("submit", help="submit a model for review (draft/rejected -> in-review)")
    s.add_argument("--model", required=True)
    s.add_argument("--version", required=True)
    s.add_argument("--by", default=None, help="submitter (defaults to model owner)")
    s.add_argument("--note", default=None)
    s.set_defaults(func=cmd_submit)

    s = sub.add_parser("approve", help="approve a model in review")
    s.add_argument("--model", required=True)
    s.add_argument("--version", required=True)
    s.add_argument("--reviewer", required=True)
    s.add_argument("--note", default=None)
    s.set_defaults(func=cmd_approve)

    s = sub.add_parser("reject", help="reject a model in review")
    s.add_argument("--model", required=True)
    s.add_argument("--version", required=True)
    s.add_argument("--reviewer", required=True)
    s.add_argument("--note", default=None)
    s.set_defaults(func=cmd_reject)

    s = sub.add_parser("list", help="list all models")
    s.set_defaults(func=cmd_list)

    s = sub.add_parser("show", help="show full model record incl. lineage and approvals")
    s.add_argument("--model", required=True)
    s.add_argument("--version", required=True)
    s.set_defaults(func=cmd_show)

    return p


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
