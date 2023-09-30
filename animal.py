import random
from organism import Organism

class Animal(Organism):
    def __init__(self, name):
        super().__init__(name)

    def hunt(self):
        prey = random.randint(1, 10)
        self.health += prey
