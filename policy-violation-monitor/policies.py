"""Policy rule definitions for the policy-violation monitor.

Each rule is a dict with:
  id          - stable identifier, e.g. "PII-001"
  name        - short human-readable name
  severity    - one of "high", "medium", "low"
  description - what the rule guards against
  check       - callable(text: str) -> list of evidence strings (empty = no hit)

Detection is deterministic regex/heuristics only, no network, no models.
To add a rule, append a dict with the same shape (see README for details).
"""

import re


def _regex_check(pattern, flags=0):
    """Build a check function that returns every match of a regex as evidence."""
    rx = re.compile(pattern, flags)

    def check(text):
        return [m.group(0) for m in rx.finditer(text)]

    return check


def _injection_check(text):
    """Heuristic: known prompt-injection / jailbreak phrasing appearing in
    tool output or model output text."""
    patterns = [
        r"ignore\s+(all\s+)?(previous|prior|above)\s+instructions?",
        r"disregard\s+(all\s+)?(previous|prior|above)\s+instructions?",
        r"you\s+are\s+now\s+(dan|an?\s+\w+\s+assistant)",
        r"developer\s+mode\s+(enabled|on)",
        r"jailbreak\s+mode",
        r"do\s+anything\s+now",
        r"as\s+an\s+ai\s*,?\s*you\s+must\s+comply",
        r"reveal\s+(your\s+)?system\s+prompt",
        r"repeat\s+(your\s+)?(system|initial)\s+instructions?",
    ]
    hits = []
    for p in patterns:
        for m in re.finditer(p, text, re.IGNORECASE):
            hits.append(m.group(0))
    return hits


def _disallowed_content_check(text):
    """Heuristic markers for content categories a deployment policy forbids.
    These are deliberately simple keyword-family markers for a demo."""
    categories = {
        "weapons": [r"\bbuild\s+a\s+(bomb|missile|bioweapon)\b", r"\bmake\s+napalm\b"],
        "self-harm": [r"\bhow\s+to\s+(kill\s+myself|commit\s+suicide)\b"],
        "csam": [r"\bchild\s+porn\b", r"\bcsam\b"],
    }
    hits = []
    for category, patterns in categories.items():
        for p in patterns:
            for m in re.finditer(p, text, re.IGNORECASE):
                hits.append(f"[{category}] {m.group(0)}")
    return hits


POLICIES = [
    {
        "id": "PII-001",
        "name": "PII leakage: email addresses",
        "severity": "high",
        "description": "Output contains an email address, which may expose a "
                       "real person's contact information.",
        "check": _regex_check(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    },
    {
        "id": "PII-002",
        "name": "PII leakage: phone numbers",
        "severity": "high",
        "description": "Output contains a phone number pattern, which may "
                       "expose personal contact information.",
        "check": _regex_check(r"(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"),
    },
    {
        "id": "PII-003",
        "name": "PII leakage: ID-like numbers",
        "severity": "high",
        "description": "Output contains an SSN-like or national-ID-like "
                       "number (###-##-#### pattern).",
        "check": _regex_check(r"\b\d{3}-\d{2}-\d{4}\b"),
    },
    {
        "id": "SEC-001",
        "name": "Secrets leakage: API keys/tokens",
        "severity": "high",
        "description": "Output contains something shaped like a secret: "
                       "high-entropy token assignments or known key prefixes.",
        "check": _regex_check(
            r"(?:sk-[A-Za-z0-9]{16,}|AKIA[0-9A-Z]{16}|"
            r"(?:api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_\-./+=]{16,}['\"]?)",
            re.IGNORECASE,
        ),
    },
    {
        "id": "INJ-001",
        "name": "Prompt-injection attempt in output/tool text",
        "severity": "medium",
        "description": "Output or quoted tool text contains known "
                       "prompt-injection or jailbreak phrasing, e.g. "
                       "'ignore previous instructions'.",
        "check": _injection_check,
    },
    {
        "id": "DIS-001",
        "name": "Disallowed content markers",
        "severity": "high",
        "description": "Output contains markers of content categories that "
                       "deployment policy forbids (weapons instructions, "
                       "self-harm instructions, CSAM references).",
        "check": _disallowed_content_check,
    },
]


SEVERITY_RANK = {"low": 1, "medium": 2, "high": 3}


def evaluate(text):
    """Run every policy against text.

    Returns a list of (policy, evidence) tuples for the policies that fired.
    """
    results = []
    for policy in POLICIES:
        evidence = policy["check"](text)
        if evidence:
            results.append((policy, evidence))
    return results


def worst_severity(triggered):
    """Highest severity among triggered policies; 'low' if none triggered."""
    if not triggered:
        return "low"
    return max((p["severity"] for p, _ in triggered),
               key=lambda s: SEVERITY_RANK[s])
