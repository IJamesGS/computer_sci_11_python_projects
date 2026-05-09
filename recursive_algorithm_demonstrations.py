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

from collections.abc import Callable, Generator


def generator_as_collection[T](generator: Callable[[], Generator[T]]):
    """Turn a generator into a collection."""

    class Collection:
        def __init__(self) -> None:
            # See <https://docs.astral.sh/ruff/rules/mutable-class-default/>
            # for information about why this was defined in the `__init__`
            # function.
            self._sequence: list[T] = []
            self._generator: Generator[T] = generator()

        def __getitem__(self, index: int | slice[int, int, int]) -> T | list[T]:
            gen_up_to: int = index.stop if isinstance(index, slice) else index
            while len(self._sequence) - 1 < gen_up_to:
                self._sequence.append(next(self._generator))
            return self._sequence[index]

    return Collection()


@generator_as_collection
def fibonacci() -> Generator[int]:
    """A representation of the Fibonacci sequence as a class."""
    last_two_numbers: tuple[int, int] = (0, 1)

    yield last_two_numbers[0]
    yield last_two_numbers[1]

    while True:
        last_two_numbers = (last_two_numbers[1], sum(last_two_numbers))
        yield last_two_numbers[1]


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


def greatest_common_factor(a: int, b: int) -> int:
    """Gets the greatest common factor of two positive integers

    Implementation uses the Euclidean Algorithm: the bigger number is
    continuously divided (modulo) by the smaller number, until the smaller
    number equals 0, and then the greater number will be the GCF.
    """
    # Source: https://www.geeksforgeeks.org/dsa/program-to-find-gcd-or-hcf-of-two-numbers/
    # Approach 4 (Optimized Euclidean Algorithm by Checking Remainder) was used.
    if a < 0 or b < 0:
        raise ValueError("GCF function doesn't support negative numbers.")

    while True:
        a, b = b % a, a

        if a == 0:
            return b


if __name__ == "__main__":
    # The script is being run directly
    pass
