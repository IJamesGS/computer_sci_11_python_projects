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
    """A representation of the Fibonacci sequence as a class."""

    def __init__(self) -> None:
        # See <https://docs.astral.sh/ruff/rules/mutable-class-default/>
        # for information about why this was defined in the `__init__`
        # function.
        self._sequence: list[int] = []
        self._generator_instance: Generator[int] = self._generator()

    @staticmethod
    def _generator() -> Generator[int]:
        last_two_numbers: tuple[int, int] = (0, 1)

        yield last_two_numbers[0]
        yield last_two_numbers[1]

        while True:
            last_two_numbers = (last_two_numbers[1], sum(last_two_numbers))
            yield last_two_numbers[1]

    def __getitem__(self, index: int | slice[int, int, int]) -> int | list[int]:
        gen_up_to: int = index.stop if isinstance(index, slice) else index
        while len(self._sequence) - 1 < gen_up_to:
            self._sequence.append(next(self._generator_instance))
        return self._sequence[index]


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
