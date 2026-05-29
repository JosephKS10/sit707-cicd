"""
Calculator module — business logic for the SIT707 CI/CD demo.

This module deliberately ships with a bug in `divide`:
it does not guard against division by zero. The accompanying
test `test_divide_by_zero` will fail until the bug is fixed.

The two-commit story:
    Commit 1 ("broken"): this file as-is + tests including the
                         zero-division test => pipeline FAILS at the
                         test step. Cloud Build never reaches the
                         deploy step. Screenshot the failed run.

    Commit 2 ("fix"):    replace `divide` with the guarded version
                         shown at the bottom of this file. All tests
                         pass, container builds, deploys to Cloud Run.
                         Screenshot the green run + the live URL.
"""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# --- Fix to apply for Commit 2 (replace the function above with this) -------
#
# def divide(a: float, b: float) -> float:
#     if b == 0:
#         raise ValueError("Cannot divide by zero")
#     return a / b
#
# ---------------------------------------------------------------------------
