#!/usr/bin/env python3
"""
EU AI Act risk-tier classifier (educational, rule-based).

Reads a "system card" JSON describing an AI system and assigns an EU AI Act
risk tier -- Prohibited, High-Risk, Limited Risk, or Minimal Risk -- using a
simplified keyword/category mapping.

    python3 classify.py --card examples/cv_screener.json
    python3 classify.py --card examples/cv_screener.json --json
    python3 classify.py --demo

Standard library only. Runs fully offline. This is an educational tool, not
legal advice; the mapping below is deliberately simplified relative to the
actual regulation text (see README).
"""

import argparse
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Tier model
# ---------------------------------------------------------------------------

# Higher number = higher regulatory severity. Precedence: Prohibited wins over
# High-Risk, which wins over Limited Risk, which wins over Minimal Risk.
TIER_ORDER = {"Prohibited": 4, "High-Risk": 3, "Limited Risk": 2, "Minimal Risk": 1}

# ---------------------------------------------------------------------------
# Rules
# ---------------------------------------------------------------------------
# Each rule has:
#   id          short identifier
#   tier        one of TIER_ORDER keys
#   category    human-readable category label
#   require_any patterns (regex, case-insensitive); matches if ANY one hits
#   require_all groups of patterns; matches only if EVERY group has >=1 hit
#   rationale   why the match matters (shown in the report)
#   flag        optional reviewer note attached when the rule matches
#
# A rule fires when: (require_any empty OR any pattern hits) AND
#                    (require_all empty  OR every group has a hit).

RULES = [
    # ============================ PROHIBITED (Art. 5) ============================
    {
        "id": "social-scoring",
        "tier": "Prohibited",
        "category": "Social scoring (Art. 5(1)(c))",
        "require_any": [
            r"social scor\w*",
            r"citizen scor\w*",
            r"trustworth\w* scor\w*",
            r"behavio[u]?r\w* scor\w*",
        ],
        "require_all": [],
        "rationale": (
            "The system evaluates or classifies people over time based on "
            "social behaviour or personal characteristics, and the resulting "
            "score leads to detrimental treatment in unrelated contexts."
        ),
        "flag": None,
    },
    {
        "id": "rbi-public-spaces",
        "tier": "Prohibited",
        "category": "Real-time remote biometric identification in public spaces (Art. 5(1)(h))",
        "require_any": [r"real[\s-]?time"],
        "require_all": [
            [
                r"facial recognition",
                r"face recognition",
                r"remote biometric identification",
                r"biometric identification",
            ],
            [
                r"public[\s-]?space",
                r"publicly accessible",
                r"\bstreet\b",
                r"cctv",
                r"surveillance",
            ],
        ],
        "rationale": (
            "Real-time remote biometric identification deployed in publicly "
            "accessible spaces for law-enforcement purposes is banned, subject "
            "to narrowly defined exceptions."
        ),
        "flag": None,
    },
    {
        "id": "manipulative-subliminal",
        "tier": "Prohibited",
        "category": "Manipulative or subliminal techniques (Art. 5(1)(a)-(b))",
        "require_any": [
            r"subliminal",
            r"manipulat\w+ (technique|vulnerable|behavio[u]?r)",
            r"exploit\w+ (vulnerab|children|elderly|disab)",
        ],
        "require_all": [],
        "rationale": (
            "The system deploys subliminal, manipulative or deceptive techniques, "
            "or exploits vulnerabilities of a person or group, materially "
            "distorting behaviour in a harmful way."
        ),
        "flag": None,
    },
    {
        "id": "emotion-work-education",
        "tier": "Prohibited",
        "category": "Emotion inference in work or education (Art. 5(1)(g))",
        "require_any": [r"emotion"],
        "require_all": [
            [
                r"workplace",
                r"employer",
                r"workforce",
                r"employee",
                r"\bworker\b",
                r"call[\s-]?center",
                r"school",
                r"student",
                r"classroom",
            ]
        ],
        "rationale": (
            "Inferring emotions of a natural person in work or education "
            "settings is a prohibited practice (medical/safety purposes "
            "excepted)."
        ),
        "flag": (
            "Borderline by design: the real provision has exceptions (e.g. "
            "medical or safety purposes). This simplified mapping treats all "
            "workplace/education emotion inference as prohibited -- get legal "
            "review before relying on this classification."
        ),
    },
    {
        "id": "predictive-policing",
        "tier": "Prohibited",
        "category": "Individual criminal-risk assessment (Art. 5(1)(d))",
        "require_any": [
            r"predict\w+ (polic|crime)",
            r"recidivism",
            r"risk scor\w* of (an? )?(individual|offender|suspect|criminal|person)",
            r"criminal risk",
        ],
        "require_all": [],
        "rationale": (
            "Assessing the risk of a natural person committing a criminal "
            "offence based solely on profiling or personality traits is banned."
        ),
        "flag": None,
    },
    {
        "id": "face-scraping",
        "tier": "Prohibited",
        "category": "Untargeted facial-image scraping (Art. 5(1)(e))",
        "require_any": [r"scrap\w+"],
        "require_all": [
            [r"\bface\b", r"facial", r"photo", r"image"],
            [r"database", r"internet", r"cctv"],
        ],
        "rationale": (
            "Creating or expanding facial-recognition databases through "
            "untargeted scraping of facial images from the internet or CCTV is "
            "prohibited."
        ),
        "flag": None,
    },
    # ============================ HIGH-RISK (Annex III) ============================
    {
        "id": "hr-biometrics",
        "tier": "High-Risk",
        "category": "Biometrics (Annex III, point 1)",
        "require_any": [
            r"biometric (verification|authentication|access control|categor)",
            r"fingerprint",
            r"iris[\s-]?scan",
            r"voiceprint",
        ],
        "require_all": [],
        "rationale": (
            "Biometric identification, verification or categorisation systems "
            "are high-risk (except where a prohibited practice applies)."
        ),
        "flag": None,
    },
    {
        "id": "hr-critical-infrastructure",
        "tier": "High-Risk",
        "category": "Critical infrastructure (Annex III, point 2)",
        "require_any": [
            r"critical infrastructure",
            r"power grid",
            r"energy (management|distribution)",
            r"water supply",
            r"traffic management",
            r"digital infrastructure",
        ],
        "require_all": [],
        "rationale": (
            "AI used as a safety component in the management and operation of "
            "critical infrastructure is high-risk."
        ),
        "flag": None,
    },
    {
        "id": "hr-education",
        "tier": "High-Risk",
        "category": "Education and vocational training (Annex III, point 3)",
        "require_any": [
            r"\beducation\b",
            r"vocational training",
            r"university admission",
            r"exam (scor|grad|assess)",
            r"student evaluat",
        ],
        "require_all": [],
        "rationale": (
            "AI determining access to education or evaluating learning outcomes "
            "is high-risk because it shapes a person's educational and "
            "professional trajectory."
        ),
        "flag": None,
    },
    {
        "id": "hr-employment",
        "tier": "High-Risk",
        "category": "Employment and workers management (Annex III, point 4)",
        "require_any": [
            r"recruit",
            r"hiring",
            r"\bcv\b",
            r"resume screen",
            r"job applicant",
            r"\bpromotion\b",
            r"termination",
            r"task allocat",
            r"performance monitor",
            r"shortlist",
        ],
        "require_all": [],
        "rationale": (
            "AI used in recruitment, or in decisions affecting work-related "
            "relationships such as promotion, termination or task allocation, "
            "is high-risk."
        ),
        "flag": None,
    },
    {
        "id": "hr-essential-services",
        "tier": "High-Risk",
        "category": "Essential private/public services (Annex III, point 5)",
        "require_any": [
            r"credit scor",
            r"\bloan\b",
            r"insurance",
            r"welfare",
            r"public benefit",
            r"\bhousing\b",
            r"healthcare triage",
            r"emergency dispatch",
        ],
        "require_all": [],
        "rationale": (
            "AI evaluating eligibility for public benefits or creditworthiness, "
            "or used in pricing/dispatch of essential services, is high-risk."
        ),
        "flag": None,
    },
    {
        "id": "hr-law-enforcement",
        "tier": "High-Risk",
        "category": "Law enforcement (Annex III, point 6)",
        "require_any": [
            r"law enforcement",
            r"\bpolice\b",
            r"crime analytics",
        ],
        "require_all": [],
        "rationale": (
            "AI assisting law enforcement in ways that can interfere with "
            "fundamental rights is high-risk (unless a prohibited practice "
            "applies)."
        ),
        "flag": None,
    },
    {
        "id": "hr-migration",
        "tier": "High-Risk",
        "category": "Migration, asylum and border control (Annex III, point 7)",
        "require_any": [
            r"migration",
            r"asylum",
            r"border control",
            r"\bvisa\b",
        ],
        "require_all": [],
        "rationale": (
            "AI used in migration, asylum or border-control management is "
            "high-risk given the vulnerability of the people affected."
        ),
        "flag": None,
    },
    {
        "id": "hr-justice-democracy",
        "tier": "High-Risk",
        "category": "Justice and democratic processes (Annex III, point 8)",
        "require_any": [
            r"judicial",
            r"\bcourt\b",
            r"sentencing",
            r"parole",
            r"legal decision",
            r"election",
            r"\bvoting\b",
            r"political campaign",
            r"referendum",
        ],
        "require_all": [],
        "rationale": (
            "AI assisting judicial authorities or influencing democratic "
            "processes (e.g. elections) is high-risk."
        ),
        "flag": None,
    },
    # ============================ LIMITED RISK (Art. 50) ============================
    {
        "id": "lr-chatbot",
        "tier": "Limited Risk",
        "category": "AI interaction / chatbot (Art. 50(1))",
        "require_any": [
            r"chatbot",
            r"conversational (ai|agent|assistant)",
            r"virtual assistant",
            r"customer service (agent|bot)",
        ],
        "require_all": [],
        "rationale": (
            "People interacting with the system must be informed they are "
            "interacting with AI. Transparency duties apply."
        ),
        "flag": None,
    },
    {
        "id": "lr-emotion-recognition",
        "tier": "Limited Risk",
        "category": "Emotion recognition system (Art. 50(3))",
        "require_any": [
            r"emotion recognition",
            r"emotion detection",
            r"emotion analysis",
        ],
        "require_all": [],
        "rationale": (
            "Deployers must inform people when an emotion-recognition system "
            "is operating (outside the prohibited work/education contexts)."
        ),
        "flag": None,
    },
    {
        "id": "lr-biometric-categorisation",
        "tier": "Limited Risk",
        "category": "Biometric categorisation (Art. 50(3))",
        "require_any": [r"biometric categor"],
        "require_all": [],
        "rationale": (
            "Deployers must inform people when a biometric-categorisation "
            "system is operating."
        ),
        "flag": None,
    },
    {
        "id": "lr-generated-content",
        "tier": "Limited Risk",
        "category": "AI-generated / synthetic content (Art. 50(2),(4))",
        "require_any": [
            r"deepfake",
            r"ai[\s-]?generated (image|video|text|content|audio)",
            r"synthetic media",
        ],
        "require_all": [],
        "rationale": (
            "AI-generated or manipulated content must be labelled as such in a "
            "machine-readable, visible manner."
        ),
        "flag": None,
    },
]

# ---------------------------------------------------------------------------
# Obligations per tier (simplified checklists)
# ---------------------------------------------------------------------------

OBLIGATIONS = {
    "Prohibited": [
        "Do NOT place on the market, put into service, or use in the EU -- the practice is banned.",
        "Decommission or redesign the system to remove the prohibited functionality.",
        "Document the prohibition analysis and legal review trail.",
        "Note: fines up to EUR 35M or 7% of worldwide annual turnover.",
    ],
    "High-Risk": [
        "Implement a risk management system (Art. 9).",
        "Ensure data governance and quality of training/validation/test data (Art. 10).",
        "Prepare technical documentation and keep automatically generated logs (Art. 11-12).",
        "Provide transparency information and instructions for use to deployers (Art. 13).",
        "Design for effective human oversight (Art. 14).",
        "Ensure appropriate accuracy, robustness and cybersecurity (Art. 15).",
        "Complete a conformity assessment and affix CE marking (Art. 43).",
        "Register the system in the EU database (Art. 71).",
        "Run post-market monitoring and report serious incidents (Art. 72-73).",
    ],
    "Limited Risk": [
        "Inform users they are interacting with an AI system (Art. 50(1)).",
        "Clearly label AI-generated or manipulated content (Art. 50(2),(4)).",
        "Inform users when emotion recognition or biometric categorisation is in use (Art. 50(3)).",
        "Make disclosures timely, clear and distinguishable.",
    ],
    "Minimal Risk": [
        "No mandatory AI Act obligations for this tier.",
        "Consider voluntary codes of conduct (Art. 95).",
        "If you provide a general-purpose AI model, check the separate provider obligations (Art. 51-55).",
        "Keep basic documentation of intended use as good practice.",
    ],
}

DISCLAIMER = (
    "Educational tool only -- not legal advice. The rule mapping is simplified "
    "relative to the official regulation text. Verify any real deployment "
    "against the EU AI Act itself and consult qualified counsel."
)

# ---------------------------------------------------------------------------
# Classifier
# ---------------------------------------------------------------------------


def _haystack(card):
    """Combine the system-card fields into one searchable text blob."""
    parts = [
        card.get("name", ""),
        card.get("description", ""),
        card.get("intended_use", ""),
        card.get("deployer_type", ""),
    ]
    parts.extend(card.get("data_types") or [])
    parts.extend(card.get("capabilities") or [])
    return " ".join(str(p) for p in parts)


def _rule_matches(rule, text):
    """A rule fires when require_any hits (or is empty) AND every
    require_all group has at least one hit."""
    if rule["require_any"]:
        if not any(re.search(p, text, re.IGNORECASE) for p in rule["require_any"]):
            return False
    for group in rule["require_all"]:
        if not any(re.search(p, text, re.IGNORECASE) for p in group):
            return False
    return True


def classify(card):
    """Classify a system card. Returns a result dict."""
    text = _haystack(card)
    matches = []
    flags = []
    for rule in RULES:
        if _rule_matches(rule, text):
            matches.append(
                {
                    "id": rule["id"],
                    "tier": rule["tier"],
                    "category": rule["category"],
                    "rationale": rule["rationale"],
                }
            )
            if rule["flag"]:
                flags.append(rule["flag"])

    # Precedence: the most severe matched tier wins.
    tier = "Minimal Risk"
    for m in matches:
        if TIER_ORDER[m["tier"]] > TIER_ORDER[tier]:
            tier = m["tier"]

    # Competing signals: matches from tiers other than the winning one are
    # genuinely ambiguous and deserve human review.
    other_tiers = sorted({m["tier"] for m in matches if m["tier"] != tier})
    if other_tiers:
        flags.append(
            "Competing signals detected from tier(s) "
            + ", ".join(other_tiers)
            + " -- precedence resolved to "
            + tier
            + ", but a human reviewer should confirm which use case dominates."
        )

    return {
        "name": card.get("name", "(unnamed system)"),
        "tier": tier,
        "matches": matches,
        "flags": flags,
        "obligations": OBLIGATIONS[tier],
    }


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------


def format_report(result):
    """Render a human-readable classification report."""
    lines = []
    lines.append("=" * 64)
    lines.append("System: " + result["name"])
    lines.append("EU AI Act risk tier: " + result["tier"].upper())
    lines.append("=" * 64)
    lines.append("")
    if result["matches"]:
        lines.append("Matched categories:")
        for m in result["matches"]:
            lines.append("  * [%s] %s" % (m["tier"], m["category"]))
            lines.append("      " + m["rationale"])
    else:
        lines.append(
            "Matched categories: none -- no prohibited, high-risk or "
            "limited-risk signals found. Default: Minimal Risk."
        )
    lines.append("")
    if result["flags"]:
        lines.append("Reviewer flags:")
        for f in result["flags"]:
            lines.append("  ! " + f)
        lines.append("")
    lines.append("Obligations checklist:")
    for ob in result["obligations"]:
        lines.append("  [ ] " + ob)
    lines.append("")
    lines.append("Disclaimer: " + DISCLAIMER)
    return "\n".join(lines)


def run_demo(examples_dir):
    """Classify every example card and print a summary table + reports."""
    cards = sorted(examples_dir.glob("*.json"))
    if not cards:
        print("No example cards found in %s" % examples_dir)
        return 1
    results = []
    for path in cards:
        with open(path, encoding="utf-8") as f:
            card = json.load(f)
        result = classify(card)
        results.append((path.name, result))

    print("EU AI ACT RISK CLASSIFIER -- DEMO")
    print("-" * 64)
    print("%-36s %s" % ("SYSTEM", "TIER"))
    print("-" * 64)
    for fname, r in results:
        print("%-36s %s" % (r["name"][:34], r["tier"]))
    print("-" * 64)
    print("")
    for fname, r in results:
        print(format_report(r))
        print("")
    return 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="EU AI Act risk-tier classifier (educational, simplified)."
    )
    parser.add_argument("--card", help="Path to a system-card JSON file.")
    parser.add_argument(
        "--json", action="store_true", help="Emit the result as JSON."
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Classify all example cards in examples/ and print a summary table.",
    )
    args = parser.parse_args(argv)

    base = Path(__file__).resolve().parent

    if args.demo:
        return run_demo(base / "examples")

    if not args.card:
        parser.error("supply --card <file.json> or use --demo")

    with open(args.card, encoding="utf-8") as f:
        card = json.load(f)

    result = classify(card)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(format_report(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
