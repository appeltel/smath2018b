"""
Fibonacci number stuff
"""
import sys

def fib(n):
    """
    Return the nth Fibonacci number
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_cli():
    """
    Command line entry point for fib

    Expects the number as a command line argument,
    or prompts the user
    """
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = int(input('Enter a positive integer: '))

    print(fib(n))
    sys.exit(0)
