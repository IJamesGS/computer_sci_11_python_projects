from collections.abc import Callable
from typing import LiteralString


def cast_input[T](
    prompt: str,
    in_type: Callable[[str], T],
    cancel_str: str = "exit",
    additional_conditions: dict[str, Callable[[T], bool]] | None = None,
    error_message: str = "Invalid entry! Try again!",
) -> T | None:
    """Get input from the user, validating and casting it.

    Args:
        prompt: The prompt to display to the user on the terminal.
        in_type: The type that the input should be cast to.
        cancel_str: If the user input contains this string, the function
            returns ``None``.

            Defaults to "cancel".
        additional_conditions: Extra conditions to check the user input
            against. It is provided as a dictionary, with error messages
            as keys, and functions as values. These should follow the
            signature ``(T) -> bool``.
        error_message: The error message to show if the type cast failed.

    Returns:
        Input from the user, casted to the given (``in_type``) type, or
        ``None`` if the user cancelled.
    """
   # Loops until user gives a valid input.
    while True:
        try:
            # Get the user input, with the specified prompt.
            input_str = input(prompt)

            # Check if the string contains the cancel string, unless
            # it's an empty string.
            if cancel_str != "" and input_str.lower().find(cancel_str) != -1:
                return None

            # Cast to the specified type.
            input_val = in_type(input_str)

            success: bool = True

            # Check each of the user-provided conditions, if given.
            if additional_conditions is not None:
                for message, condition in additional_conditions.items():
                    if not condition(input_val):
                        print(message)
                        success = False

            # If the user-provided conditions passed, and no exceptions
            # were raised, the value can now be returned.
            if success:
                return input_val

        # User gave a value that failed to cast!
        except ValueError:
            print(error_message)


def cast_input_list[T](
    prompt: str,
    in_type: Callable[[str], T],
    num_val: int = -1,
    sep: LiteralString | None = None,
    cancel_str: str = "exit",
    additional_conditions: dict[str, Callable[[list[T]], bool]] | None = None,
    error_message: str = "Invalid entry! Try again!",
) -> list[T] | None:
    """Get input from user, validating and casting it to a list.

    Args:
        prompt: The prompt to display to the user on the terminal.
        in_type: The type that the input should be cast to.
        num_val: The size that the list should be, or -1 for any size---
            which is the default.
        sep: The separator used to split the string.

            When set to None (the default value), will split on any whitespace
            character (including \\n \\r \\t \\f and spaces) and will discard
            empty strings from the result.
        cancel_str: If the user enters this string, it returns ``None``.
        additional_conditions: A dictionary with keys as error messages, and
            callables that take in the ``list[in_type]`` type and return
            ``bool``, as keys; these are used as extra validation conditions.
        error_message: The error message to show if the type cast failed.

    Returns:
        Input from the user, casted to the given (``list[in_type]``) type,
        or ``None`` if the user cancelled.
    """
    # Loops until user gives a valid input.
    while True:
        try:
            # Get the user input, with the specified prompt.
            input_str = input(prompt)

            # Check if the string contains the cancel string, unless
            # it's an empty string.
            if cancel_str != "" and input_str.lower().find(cancel_str) != -1:
                return None

            # Split the input into a list, based on commas.
            input_str_list: list[str] = input_str.split(sep)

            # Ensure the size of the list is correct, unless the ``num_val``
            # is negative.
            if num_val >= 0 and len(input_str_list) != num_val:
                print("Wrong number of entries given! Try again.")
                continue

            # Cast each element to the specified type.
            input_val: list[T] = [in_type(x) for x in input_str_list]

            success: bool = True

            # Check each of the user-provided conditions, if given.
            if additional_conditions is not None:
                for message, condition in additional_conditions.items():
                    if not condition(input_val):
                        print(message)
                        success = False

            # If the user-provided conditions passed, and no exceptions
            # were raised, the value can now be returned.
            if success:
                return input_val

        # User gave a value that failed to cast!
        except ValueError:
            print(error_message)
