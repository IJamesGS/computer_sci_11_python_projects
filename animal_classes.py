""" """

import random

# example gene: AA - AAAA - AA - AA
#               type-color-height-weight
#               Dog - White - short(1) - light(5)
animal_types = {"AA": "Dog", "BB": "Cat", "AB": "Dog-Cat", "BA": "Cat-Dog"}

animal_colors = {
    "AAAA": "White",
    "AAAB": "Pink",
    "AABA": "Red",
    "AABB": "Peach",
    "ABAA": "Orange",
    "ABAB": "Lemon",
    "ABBB": "Yellow",
    "BAAA": "Lime",
    "BAAB": "Green",
    "BABA": "Cyan",
    "BABB": "Blue",
    "BBAA": "Indigo",
    "BBAB": "Purple",
    "BBBB": "Black",
}

animal_heights = {"AA": 1, "AB": 2, "BA": 3, "BB": 4}

animal_weights = {"AA": 5, "AB": 10, "BA": 15, "BB": 20}


class Animal:
    def __init__(self, looking: bool, genetics: str):
        self.looking = looking
        self.genetics = genetics

    def set_looking(self, look: bool) -> None | bool:
        old_looking = self.looking
        self.looking = look
        return old_looking

    def multiply(self, other):
        new_genetics = ""

        for i in range(len(self.genetics)):
            inheritance = random.randint(1, 2)
            if inheritance == 1:
                new_genetics += self.genetics[i]
            else:
                new_genetics += other.genetics[i]

        return Animal(False, new_genetics)

    def read_genetics(self):
        type_gene = ""
        color_gene = ""
        height_gene = ""
        weight_gene = ""

        for index, gene in enumerate(self.genetics):
            if index <= 1:
                type_gene += gene

            elif index <= 5 and index >= 2:
                color_gene += gene

            elif index <= 7 and index >= 6:
                height_gene += gene

            elif index <= 9 and index >= 8:
                weight_gene += gene

        self.type = animal_types[type_gene]
        self.color = animal_colors[color_gene]
        self.height = animal_heights[height_gene]
        self.weight = animal_weights[weight_gene]


if __name__ == "__main__":
    import time

    tick_time = 1 / 5
    last_tick = time.time()

    animals: list[Animal] = []

    sim_length = float(input("Enter run time (seconds): "))
    start_time = time.time()
    cycle = 0

    while True:
        cycle += 1
        print(f"cycle: {cycle}")
        extra_time = (last_tick + tick_time) - time.time()
        if extra_time > 0:
            time.sleep(extra_time)
        last_tick = time.time()

        if time.time() > start_time + sim_length:
            break

        for i, animal in enumerate(animals):
            rand_val = random.randint(1, 99)
            if rand_val > 80:
                animal.set_looking(True)
                for j, other in enumerate(animals):
                    if other.looking:
                        new_animal = animal.multiply(other)
                        new_animal.read_genetics()
                        animals.append(new_animal)
                        print(animals)

            if rand_val == 1:
                del animal
