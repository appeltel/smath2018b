"""
Tests for the fib module
"""
from smath2018b.fib import fib


def test_fib_zero():
    assert fib(0) == 0


def test_fib_eight():
    assert fib(8) == 21
