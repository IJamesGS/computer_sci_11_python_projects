"""Recursive algorithms.

A collection of recursive algorithms created to satisfy the curricular
requirements of the BC Computer Science 12 course.

Algorithms:
- Fibonacci sequence
- Exponentiation (repeated multiplication)
- Factorials
- Palindromes
- Combinations
- Greatest common factor
"""


class Fibonacci:
    """Class that represents the fibbonacci sequence."""

    _sequence: list[int] = []

    def __getitem__(n: int) -> int:
        return 1


def exponentiation(base: float, exponent: int) -> int:
    """Get the result of `base` to the power of `exponent`."""


def factorial(n: int) -> int:
    """Get the factorial of `n`."""
    if n == 0:
        return 1

    accumulator: int = 1

    for i in range(2, n + 1):
        accumulator *= i

    return accumulator


if __name__ == "__main__":
    # The script is being run directly
    pass
