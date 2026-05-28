"""
Unit tests for the calculator module.

Run locally:
    pytest -v

The test `test_divide_by_zero_raises_value_error` is the one that
fails until the bug in calculator.divide is fixed.
"""
import pytest
from app.calculator import add, subtract, multiply, divide


# --- Passing tests (cover happy paths) -------------------------------------

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(0, 0) == 0

def test_subtract_positive():
    assert subtract(10, 4) == 6

def test_subtract_negative_result():
    assert subtract(2, 5) == -3

def test_multiply_positive():
    assert multiply(3, 4) == 12

def test_multiply_by_zero():
    assert multiply(5, 0) == 0

def test_multiply_negative():
    assert multiply(-3, 4) == -12

def test_divide_simple():
    assert divide(10, 2) == 5

def test_divide_float_result():
    assert divide(7, 2) == 3.5

def test_divide_negative():
    assert divide(-10, 2) == -5


# --- The deliberately failing test (until calculator.divide is fixed) -------

def test_divide_by_zero_raises_value_error():
    """
    Specification: divide(a, 0) should raise a ValueError with a clear
    message, NOT Python's default ZeroDivisionError. This is the contract
    the Flask route depends on (it catches ValueError and returns HTTP 400).

    On Commit 1 (broken), calculator.divide does not implement this guard,
    so this test fails with ZeroDivisionError. This is the evidence of
    pipeline failure to capture in the report.

    Fix: add `if b == 0: raise ValueError(...)` to calculator.divide.
    """
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
