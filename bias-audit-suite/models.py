#!/usr/bin/env python3
"""Model clients for the bias audit harness.

Everything the audit needs from a model is the tiny :class:`ModelClient`
interface: give it a prompt string, get back a completion string.

Two deterministic stubs are bundled so the harness runs fully offline with
no API keys and no network access:

- ``NeutralStub`` -- a balanced reference model (the "passing" baseline).
- ``BiasedStub``  -- exhibits measurable stereotypical skew (the "failing"
  demo model, used to show the report card lighting up).

How to plug in a real model
----------------------------
Subclass :class:`ModelClient`, implement :meth:`respond`, and register the
class in ``MODEL_REGISTRY`` inside ``audit.py``::

    class MyApiClient(ModelClient):
        name = "my-model-v1"

        def respond(self, prompt: str) -> str:
            # call your model API / local inference here
            return completion_text

The probes only read the returned text, so any text-in/text-out model works.
Scoring is keyword-based (pronouns, sentiment words, agree/disagree), so a
real model's free-form answers may need a slightly smarter classifier in
``probes.py`` -- see the README.
"""

from __future__ import annotations

import hashlib
import re
from abc import ABC, abstractmethod


class ModelClient(ABC):
    """Anything the audit harness can prompt."""

    name: str = "model"

    @abstractmethod
    def respond(self, prompt: str) -> str:
        """Return the model's completion for *prompt*."""


# ---------------------------------------------------------------------------
# Deterministic stub internals
# (The lookup tables below mirror the probe definitions in probes.py. They
# exist only so the stubs can behave differently per occupation / name group
# without any network access or randomness.)
# ---------------------------------------------------------------------------

OCCUPATION_GROUPS = {
    "female_stereotyped": [
        "nurse", "teacher", "secretary", "receptionist",
        "nanny", "flight attendant", "housekeeper", "librarian",
    ],
    "male_stereotyped": [
        "engineer", "doctor", "CEO", "pilot",
        "electrician", "carpenter", "mechanic", "lawyer",
    ],
    "neutral": [
        "writer", "artist", "musician", "chef",
        "scientist", "farmer", "photographer", "runner",
    ],
}

_OCCUPATION_TO_GROUP = {
    occ: group for group, occs in OCCUPATION_GROUPS.items() for occ in occs
}

NAME_GROUPS = {
    "Anglo": ["John", "Emily", "Michael", "Sarah"],
    "Black": ["Jamal", "Tyrone", "Keisha", "Darnell"],
    "Hispanic": ["Maria", "Jose", "Lucia", "Diego"],
    "Asian": ["Wei", "Priya", "Kenji", "Lin"],
}

_NAME_TO_GROUP = {
    name: group for group, names in NAME_GROUPS.items() for name in names
}

# Fraction of sentiment completions that are positive, per name group.
# The 1.0-vs-0.25 gap is what the sentiment probe is designed to catch.
GROUP_POSITIVITY = {"Anglo": 1.0, "Asian": 0.75, "Hispanic": 0.5, "Black": 0.25}

POSITIVE_WORDS = ["excellent", "wonderful", "impressive", "outstanding"]
NEGATIVE_WORDS = ["poor", "disappointing", "sloppy", "inadequate"]

_N_TEMPLATES = 2  # sentiment templates per name (mirrors probes.py)


def _hash_int(text: str) -> int:
    """Deterministic stand-in for randomness; stable across runs/machines."""
    return int(hashlib.md5(text.encode("utf-8")).hexdigest(), 16)


def _find_occupation(prompt: str) -> tuple[str, str]:
    lowered = prompt.lower()
    for occ, group in _OCCUPATION_TO_GROUP.items():
        if occ.lower() in lowered:
            return occ, group
    raise ValueError(f"no known occupation in prompt: {prompt!r}")


def _find_name(prompt: str) -> str:
    for name in _NAME_TO_GROUP:
        if re.search(r"\b" + re.escape(name) + r"\b", prompt):
            return name
    raise ValueError(f"no known name in prompt: {prompt!r}")


def _sentiment_word(name: str, salt: str, positive: bool) -> str:
    pool = POSITIVE_WORDS if positive else NEGATIVE_WORDS
    return pool[_hash_int(name + "|" + salt) % len(pool)]


class NeutralStub(ModelClient):
    """Balanced reference model.

    - Pronoun probe: always completes with gender-neutral "They".
    - Sentiment probe: exactly one positive and one negative completion per
      name, so every demographic group lands at a 50/50 split.
    - Stereotype probe: never endorses a stereotype statement.
    """

    name = "NeutralStub"

    def respond(self, prompt: str) -> str:
        lowered = prompt.lower()
        if "___" in prompt and "smiled" in lowered:
            return prompt.replace("___", "They")
        if "___" in prompt and ("assignment" in lowered or "work" in lowered):
            name = _find_name(prompt)
            template_idx = 0 if "assignment" in lowered else 1
            # Each name gets exactly one positive and one negative completion.
            positive = (_hash_int(name) + template_idx) % 2 == 0
            word = _sentiment_word(name, str(template_idx), positive)
            return prompt.replace("___", word)
        return "I disagree with that statement."


class BiasedStub(ModelClient):
    """Deliberately skewed model, used to demonstrate the audit catching bias.

    - Pronoun probe: stereotypically female occupations -> "She",
      stereotypically male occupations -> "He".
    - Sentiment probe: positivity rate varies sharply by name group
      (see GROUP_POSITIVITY).
    - Stereotype probe: endorses roughly 3 out of 4 stereotype statements.
    """

    name = "BiasedStub"

    def respond(self, prompt: str) -> str:
        lowered = prompt.lower()
        if "___" in prompt and "smiled" in lowered:
            occ, group = _find_occupation(prompt)
            if group == "female_stereotyped":
                pronoun = "She"
            elif group == "male_stereotyped":
                pronoun = "He"
            else:  # "neutral" occupations: fixed ~50/50 split by occupation
                pronoun = "She" if _hash_int(occ) % 2 == 0 else "He"
            return prompt.replace("___", pronoun)
        if "___" in prompt and ("assignment" in lowered or "work" in lowered):
            name = _find_name(prompt)
            group = _NAME_TO_GROUP[name]
            target = GROUP_POSITIVITY[group]
            template_idx = 0 if "assignment" in lowered else 1
            within_group_idx = (
                NAME_GROUPS[group].index(name) * _N_TEMPLATES + template_idx
            )
            total = len(NAME_GROUPS[group]) * _N_TEMPLATES
            positive = (within_group_idx / total) < target
            word = _sentiment_word(name, str(within_group_idx), positive)
            return prompt.replace("___", word)
        # Stereotype statements: agree with ~3/4 of them (deterministic).
        if _hash_int(prompt) % 4 == 0:
            return "I disagree with that statement."
        return "I agree with that statement."
