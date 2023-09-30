import random
import time
from plant import Plant, Flower, Tree
from animal import Animal

# Initialize 'days' before the main function
days = 0

# ANSI escape codes for text colors
GREEN = "\033[92m"  # Green
RED = "\033[91m"    # Red
RESET = "\033[0m"   # Reset to default color

def main():
    global days  # Declare 'days' as a global variable

    terrarium = []
    for _ in range(5):
        plant = Plant("Plant")
        terrarium.append(plant)

    for _ in range(3):
        flower = Flower("Flower")
        flower.petal_color = "red"  # Set a specific petal color
        terrarium.append(flower)

    for _ in range(2):
        tree = Tree("Tree")
        terrarium.append(tree)

    while True:
        # Add a double space before printing each day
        print("\nDay", days, ":")

        # Store daily updates in a list
        daily_updates = []

        for organism in terrarium:
            if isinstance(organism, Plant):
                organism.grow()
                daily_updates.append(f"{GREEN}{organism.name} grew.{RESET}")
            elif isinstance(organism, Animal):
                organism.move()
                if random.random() < 0.2:
                    organism.hunt()
                    daily_updates.append(f"{GREEN}{organism.name} hunted and ate.{RESET}")

            if organism.is_alive():
                daily_updates.append(f"{organism.name} (Health: {organism.health})")
            else:
                terrarium.remove(organism)
                daily_updates.append(f"{RED}{organism.name} has died.{RESET}")

        # Print the daily updates with color
        for update in daily_updates:
            print(update)

        if not terrarium:
            print("All organisms have died. Simulation over.")
            break

        days += 1
        time.sleep(2)  # Delay for 60 seconds (1 minute)

if __name__ == "__main__":
    main()
