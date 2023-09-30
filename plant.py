import random  # Import the random module

from organism import Organism

class Plant(Organism):
    def __init__(self, name):
        super().__init__(name)

    def grow(self):
        self.health += random.randint(1, 5)

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.petal_color = "unknown"
        self.bloomed = False  # Add a flag to track if the flower has bloomed

    def grow(self):
        if not self.bloomed and self.health >= 150:
            self.bloom()
        elif self.bloomed:
            self.health -= 1
        else:
            super().grow()

    def bloom(self):
        self.bloomed = True
        self.name = "Bloomed Flower"  # Change the name when the flower blooms
        print(f"{self.name} with {self.petal_color} petals is blooming.")

    def is_alive(self):
        return self.health > 0


class Tree(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.height = 0

    def grow(self):
        super().grow()  # Call the base class's grow method
        self.height += random.randint(1, 3)

    def shade(self):
        # Tree-specific behavior
        print(f"{self.name} provides shade with a height of {self.height} meters.")
