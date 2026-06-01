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
    "ABBA": "Brown",
    "ABBB": "Yellow",
    "BAAA": "Lime",
    "BAAB": "Green",
    "BABA": "Cyan",
    "BABB": "Blue",
    "BBAA": "Indigo",
    "BBAB": "Purple",
    "BBBA": "Violet",
    "BBBB": "Black",
}

animal_heights = {"AA": 1, "AB": 2, "BA": 3, "BB": 4}

animal_weights = {"AA": 5, "AB": 10, "BA": 15, "BB": 20}


class Animal:
    def __init__(self, looking: bool, genetics: str):
        self.looking = looking
        self.genetics = genetics

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

    def set_looking(self, look: bool) -> None | bool:
        old_looking = self.looking
        self.looking = look
        return old_looking

    def multiply(self, other):
        new_genetics = ""

        for i in range(len(self.genetics)):
            inheritance = random.randint(1, 11)
            if inheritance <= 5:
                new_genetics += self.genetics[i]
            elif inheritance <= 10:
                new_genetics += other.genetics[i]
            elif inheritance == 11:
                mutation = random.randint(1, 2)
                if mutation == 1:
                    new_genetics += "A"

                elif mutation == 2:
                    new_genetics += "B"

        return Animal(False, new_genetics)


if __name__ == "__main__":
    import time

    tick_time = 1 / 5
    last_tick = time.time()

    animals: list[Animal] = []

    sim_length = float(input("Enter run time (seconds): "))

    animals.append(Animal(True, "AAAAAAAAAA"))
    animals.append(Animal(True, "BBBBBBBBBB"))

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
            for i, animal in enumerate(animals):
                print(f"Animal #{i}, Genetics: {animal.genetics}")
            raise SystemExit

        lucky_guy = random.choice(animals)
        lucky_guy.set_looking(True)

        for i, animal in enumerate(animals):
            if animal.looking:
                for j, other in enumerate(animals):
                    if other.looking and i != j:
                        animal.set_looking(False)
                        other.set_looking(False)
                        new_animal = animal.multiply(other)
                        print(f"new genes: {new_animal.genetics}")
                        animals.append(new_animal)
                        break

            rand_val = random.randint(1, 99)
            if rand_val == 17:
                del animal
