"""
Fibonacci number stuff
"""


def fib(n):
    """
    Return the nth Fibonacci number
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
