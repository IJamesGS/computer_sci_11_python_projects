"""Class Exercises

A collection of exercises involving the programming and usage of class-based code

"""

import sys
from typing import Literal

# Source - https://stackoverflow.com/a/8315566
# Posted by kindall, modified by community. See post 'Timeline' for change history
# Retrieved 2026-05-27, License - CC BY-SA 4.0


def tracefunc(frame, event, arg, indent=[0]):
    if event == "call":
        indent[0] += 2
        if indent[0] == 0:
            print("-" * indent[0] + "> call function", frame.f_code.co_name)
    elif event == "return":
        if indent[0] == 2:
            print("<" + "-" * indent[0], "exit function", frame.f_code.co_name)
        indent[0] -= 2
    return tracefunc


sys.setprofile(tracefunc)

# ===================== Exercise 1: Triangle class =====================

# - [x] Create a class, Triangle. Its `__init__()` method should take
#       `self`, `angle1`, `angle2`, and `angle3` as arguments. Make sure
#       to set these appropriately in the body of the `__init__()`
#       method.
# - [x] Create a variable named `number_of_sides` and set it equal to `3`.
# - [x] Create a method named `check_angles()`. It should return `True`
#       if the sum of `self.angle1`, `self.angle2`, and `self.angle3` is
#       equal to `180`, and `False` otherwise.
# - [x] Create a variable named `my_triangle` and set it equal to a new
#       instance of your `Triangle` class. Pass it three angles that sum
#       to `180` (e.g. `90`, `30`, `60`).
# - [x] Print out `my_triangle.number_of_sides` and print out
#       `my_triangle.check_angles()`.


class Triangle:
    number_of_sides: Literal[3] = 3

    def __init__(self, angle1: float, angle2: float, angle3: float) -> None:
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self) -> bool:
        return self.angle1 + self.angle2 + self.angle3 == 180


# ------------ Manual testing code ------------

if __name__ == "__main__":
    print("Testing `Triangle`...", end="\n\n")

    my_triangle = Triangle(30, 60, 90)
    print(my_triangle.number_of_sides)
    print(my_triangle.check_angles())

# ====================== Exercise 2: Songs class =======================

# - [x] Define a class called `Songs`; it will show the lyrics of a song.
#       Its `__init__()` method should have two arguments: `self` and
#       `lyrics`. `lyrics` is a list.
# - [x] Inside your class create a method called `sing_me_a_song` that
#       prints each element of `lyrics` on his own line. Define a variable:
#       ```python
#       happy_bday = Song(["May god bless you, ",
#         "Have a sunshine on you,",
#         "Happy Birthday to you !"]
#       )
#       ```
# - [x] Call the `sing_me_song` method on this variable.


class Song:
    def __init__(self, lyrics: list[str]) -> None:
        self.lyrics = lyrics

    def sing_me_a_song(self) -> None:
        for index in range(len(self.lyrics)):
            print(self.lyrics[index])


# ------------ Manual testing code ------------

if __name__ == "__main__":
    print("Testing `Songs`...", end="\n\n")

    happy_bday = Song(
        ["May god bless you, ", "Have a sunshine on you,", "Happy Birthday to you !"]
    )
    happy_bday.sing_me_a_song()

# ==================== Exercise 3: Rectangle class ====================-

# - [x] Write a `Rectangle` class in Python language, allowing you to
#       build a rectangle with `length` and `width` attributes.
# - [x] Create a `perimeter()` method to calculate the perimeter of the
#       rectangle and `area()` method to calculate the area of the
#       rectangle.
# - [x] Create a method called `display()` that displays the `length`,
#       `width`, `perimeter()` and `area()` of an object created using
#       as an instantiation of the `Rectangle` class.
# - [x] Create a `Parallelepipede` child class inheriting from the
#       `Rectangle` class and with a `height` attribute and another
#       `volume()` method to calculate the volume of the `Parallelepiped`.


class Rectangle:
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def perimeter(self) -> float:
        return (self.length * 2) + (self.width * 2)

    def area(self) -> float:
        return self.length * self.width

    def display(self) -> None:
        print(f"length: {self.length}")
        print(f"width: {self.width}")
        print(f"perimeter: {self.perimeter()}")
        print(f"area: {self.area()}")


class Parallelepipede(Rectangle):
    def __init__(self, length: float, width: float, height: float) -> None:
        super().__init__(length, width)
        self.height = height

    def volume(self) -> float:
        return self.length * self.width * self.height


# ------------ Manual testing code ------------

if __name__ == "__main__":
    print("Testing `Rectangle`...", end="\n\n")

    rocky = Rectangle(2, 5)
    rocky.display()

    adrian = Parallelepipede(2, 5, 7)
    print(f"volume: {adrian.volume()}")

# =================== Exercise 4: Computation class ====================

# - [x] Create a `Computation` class with a default constructor (without
#       parameters) allowing to perform various calculations on integers
#       numbers.
# - [x] Create a method called `factorial()` which allows to calculate
#       the factorial of an integer.
#       - Test the method by instantiating the class.
# - [x] Create a method called `sum_numbers_up_to()` allowing to
#       calculate the sum of the first n integers 1 + 2 + 3 + .. + n.
#       - Test this method.
# - [x] Create a method called `test_prime()` in the `Computation` class
#       to test the primality of a given integer.
#       - Test this method.
# - [x] Create a method called `test_primes()` allowing to test if two
#       numbers are prime between them.
# - [x] Create a `table_mult()` method which creates and displays the
#       multiplication table of a given integer.
# - [x] Then create an `all_tables_mult()` method to display all the
#       integer multiplication tables: 1, 2, 3, ..., 9.
# - [x] Create a static `list_div()` method that gets all the divisors
#       of a given integer on new list called `l_div`.
# - [x] Create another `list_div_prime()` method that gets all the prime
#       divisors of a given integer.


class Computation:
    TABLE_MULT_SIZE: Literal[9] = 9
    TABLE_MULT_RANGE: range[int] = range(TABLE_MULT_SIZE)

    @staticmethod
    def factorial(num: int) -> int:
        if num == 0:
            return 1

        accumulator: int = 1

        for i in range(2, num + 1):
            accumulator *= i

        return accumulator

    @staticmethod
    def sum_numbers_up_to(num: int) -> int:
        accumulator: int = 0

        for i in range(1, num + 1):
            accumulator += i

        return accumulator

    @staticmethod
    def is_prime(num: int) -> bool:
        if num == 2:
            return True

        if num % 2 == 0 or num <= 1:
            return False

        for i in range(3, int(num / 2), 2):
            if num % i == 0:
                return False

        return True

    @staticmethod
    def test_coprimality(num1: int, num2: int) -> bool:
        if num1 < num2:
            num1, num2 = num2, num1

        if num1 == num2:
            raise ValueError("Two different numbers required")

        for i in range(2, num1 + 1):
            if num1 % i == 0 and num2 % i == 0:
                return False

        return True

    @staticmethod
    def table_mult(num: int) -> None:
        for i in Computation.TABLE_MULT_RANGE:
            print(i * num, end=" ")

        print()  # End the line.

    @staticmethod
    def all_tables_mult() -> None:
        for index in Computation.TABLE_MULT_RANGE:
            Computation.table_mult(index + 1)

    @staticmethod
    def list_div(num: int) -> list[int]:
        l_div: list[int] = [1]
        for i in range(2, int(num / 2)):
            if num % i == 0:
                l_div.append(i)

        l_div.append(num)

        return l_div

    @staticmethod
    def list_div_prime(num: int) -> list[int]:
        l_primdiv: list[int] = []
        for i in range(2, int(num / 2)):
            if Computation.is_prime(i) and num & i == 0:
                l_primdiv.append(i)

        return l_primdiv


# ------------ Manual testing code ------------

if __name__ == "__main__":
    print("Testing `Computation`...", end="\n\n")

    print(Computation.factorial(5))
    print(Computation.sum_numbers_up_to(5))
    print(Computation.is_prime(5))
    print(Computation.is_prime(6))
    print(Computation.test_coprimality(2, 5))
    print(Computation.test_coprimality(2, 6))
    Computation.table_mult(5)
    Computation.all_tables_mult()
    print(Computation.list_div(3))
    print(Computation.list_div_prime(100))
