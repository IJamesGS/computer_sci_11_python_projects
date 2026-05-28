""" """

import random


class Animal:
    def __init__(self, looking: bool, height: int):
        self.looking = looking
        self.height = height

    def multiply(self, other):
        return Animal(False, (self.height * other.height) / 2 + random.uniform(-1, 1))

    def set_looking(self, looking: bool) -> bool:
        old_looking = self.looking

        self.looking = looking

        return old_looking


class Carnivore(Animal):
    def __init__(self, a, b, has_eaten: bool):
        super.__init__(a, b)
        self.has_eaten = has_eaten

    def eat(self, other):
        del other
        self.has_eaten = True


class Herbivore(Animal):
    def __init__(self, a, b):
        super.__init__(a, b)


if __name__ == "__main__":
    import time

    tick_time = 1 / 20
    last_tick = time.time()

    animals: list[Animal] = []

    for i in range(6):
        animals.append(Carnivore(False, random.uniform(100, 200), False))

    for i in range(12):
        animals.append(Herbivore(False, random.uniform(100, 200)))

    sim_length = float(input("Enter run time (seconds): "))
    start_time = time.time()

    while True:
        extra_time = (last_tick + tick_time) - time.time()
        if extra_time > 0:
            time.sleep(extra_time)
        last_tick = time.time()

        if time.time() > start_time + sim_length:
            break

        for i, animal in enumerate(animals):
            rand_val = random.randint(1, 99)
            if rand_val > 95:
                animal.set_looking(True)

                for j, other in enumerate(animals):
                    if other.looking and j != i and type(animal) == type(other):
                        animal.multiply(other)

            if rand_val == 1:
                del animal
