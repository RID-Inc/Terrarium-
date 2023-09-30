class Organism:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def eat(self, food):
        self.health += food

    def move(self):
        self.health -= 1

    def is_alive(self):
        return self.health > 0
