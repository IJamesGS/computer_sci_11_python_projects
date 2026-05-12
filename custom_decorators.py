import sys
from collections.abc import Callable, Generator, Set


def generator_as_collection(generator: Callable[[], Generator[int]]):
    """Turn an int generator into a collection.

    Numbers are assumed to be generated from smallest to greatest. If they
    aren't, the `__contains__` function won't work correctly.
    """

    class _GenCol(Set):
        __iter__ = generator

        def __init__(self) -> None:
            # See <https://docs.astral.sh/ruff/rules/mutable-class-default/>
            # for information about why this was defined in the `__init__`
            # function.
            self._sequence: list[int] = []
            self._generator: Generator[int] = generator()

        def _generate_to_number(self, number: int) -> None:
            while len(self._sequence) - 1 < number:
                self._sequence.append(next(self._generator))

        def __len__(self) -> int:
            return sys.maxsize  # Nearest `int` representation of infinity.

        def __contains__(self, number) -> bool:
            if isinstance(number, int):
                self._generate_to_number(number)
                return number in self._sequence
            else:
                return False

        def __getitem__(self, index: int | slice[int, int, int]) -> int | list[int]:
            self._generate_to_number(index.stop if isinstance(index, slice) else index)

            return self._sequence[index]

    return _GenCol()
