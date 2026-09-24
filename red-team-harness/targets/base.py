"""Target interface for the red-teaming harness.

A Target is anything that can answer a prompt. Implement this interface to
evaluate a real model endpoint -- see README.md for a worked example.
"""

from abc import ABC, abstractmethod


class Target(ABC):
    """Anything the harness can red-team."""

    name = "target"

    @abstractmethod
    def query(self, prompt: str) -> str:
        """Send one prompt to the target; return its text response."""
        raise NotImplementedError


def wrap_model(query_fn, name="custom"):
    """Adapt any ``query_fn(prompt) -> str`` callable into a Target.

    Example:
        def call_my_api(prompt: str) -> str:
            ...  # hit your model endpoint here
            return response_text

        target = wrap_model(call_my_api, name="my-model")
    """

    class _WrappedTarget(Target):
        def query(self, prompt: str) -> str:  # noqa: D102
            return query_fn(prompt)

    wrapped = _WrappedTarget()
    wrapped.name = name
    return wrapped
