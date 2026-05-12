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

import sys
from collections.abc import Generator

from custom_decorators import generator_as_collection
from user_input import cast_input


@generator_as_collection
def fibonacci() -> Generator[int]:
    """A dynamic collection representing the Fibonacci sequence."""
    last_two_numbers: tuple[int, int] = (0, 1)

    yield last_two_numbers[0]
    yield last_two_numbers[1]

    while True:
        last_two_numbers = (last_two_numbers[1], sum(last_two_numbers))
        yield last_two_numbers[1]


def exponentiation(base: float, exponent: int) -> float:
    """Get the result of `base` to the power of `exponent`."""
    output: float = base

    for _ in range(exponent):
        output *= base

    return output


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


def int_or_str(x: str) -> int | str:
    try:
        return int(x)
    except ValueError:
        return x


if __name__ == "__main__":
    variables: dict[str, int] = {}

    while True:
        print("""
            What would you like to do?

            FYI, wherever you can enter a literal number, you can enter
            a variable name.

            Options:
                1: Set a variable.
                2: List variables.
                3: Get the nth number the fibonacci sequence.
                4: Get the first n numbers in the fibonacci sequence.
                5: Calculate an exponentiation problem.
                6: Get the factorial of a number.
                7: Calculate the GCF of two numbers.
                "exit" or Ctrl-C: Close the program.
        """)
        try:
            choice: int = cast_input(
                "Which option?: ", int,
                additional_conditions = {
                    "Number not within range, try again!":
                        lambda val: val >= 1 and val <= 7
                },
            )
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
            sys.exit()

        match choice:
            case 1:
                var_name: str = input("What variable should be set?: ")
                var_val: int | str = cast_input("What value should it have?: ", int_or_str)

                if isinstance(var_val, str):
                    var_val = variables[var_val]

                variables[var_name] = var_val

            case 2:
                for name, val in variables:
                    print(f"{name}: {val}")
            case 3:
                index: int | str = cast_input("n: ", int_or_str)
                if isinstance(index, str):
                    index = variables[index]

                output: int = fibonacci[index]

                print(f"Fibonacci number: {output}")

            case 4:
                index: int | str = cast_input("n: ", int)
                if isinstance(index, str):
                    index = variables[index]

                output: list[int] = fibonacci[0:index]

                print(f"Numbers: {output}")

            case 5:
                base: int | str = cast_input("base: ", int_or_str)
                if isinstance(base, str):
                    base = variables[base]

                exponent: int | str = cast_input("exponent: ", int_or_str)
                if isinstance(exponent, str):
                    exponent = variables[exponent]

                output: float = exponentiation(base, exponent)

                print(f"Result: {output}")

            case 6:
                user_in: int | str = cast_input("n: ", int)
                if isinstance(user_in, str):
                    user_in = variables[user_in]

                output: int = factorial(user_in)

                print(f"Factorial: {output}")

            case 7:
                num1: int | str = cast_input("base: ", int_or_str)
                if isinstance(num1, str):
                    num1 = variables[num1]

                num2: int | str = cast_input("exponent: ", int_or_str)
                if isinstance(num2, str):
                    num2 = variables[num2]

                output: int = greatest_common_factor(num1, num2)

                print(f"GCF: {output}")
