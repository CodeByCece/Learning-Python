import random

class Die:
    """represents sides of a dice"""

    def __init__(self, sides=6):
        """Initializes die attributes."""
        self.sides = sides

    def roll_die(self):
        """Prints randon number btw 1 and number on side of die."""
        if self.sides == 6:
            roll = random.randint(1,6)
            print(f"This is a {self.sides} sided die.")
            print(f"You just rolled a {roll}.")

            roll = random.randint(1,6)
            print(f"You just rolled a {roll}.")

            roll = random.randint(1,6)
            print(f"You just rolled a {roll}.")

            roll = random.randint(1,6)
            print(f"You just rolled a {roll}.")

            roll = random.randint(1,6)
            print(f"You just rolled a {roll}.")

            roll = random.randint(1,6)
            print(f"You just rolled a {roll}.")

            roll = random.randint(1,6)
            print(f"You just rolled a {roll}.")

            roll = random.randint(1,6)
            print(f"You just rolled a {roll}.")

            roll = random.randint(1,6)
            print(f"You just rolled a {roll}.")

            roll = random.randint(1,6)
            print(f"You just rolled a {roll}.\n")       

        elif self.sides == 10:
            roll_10 = random.randint(1,10)
            print(f"This is a {self.sides} sided die.")
            print(f"You just rolled a {roll_10}.")

            roll_10 = random.randint(1,10)
            print(f"You just rolled a {roll_10}.")

            roll_10 = random.randint(1,10)
            print(f"You just rolled a {roll_10}.")

            roll_10 = random.randint(1,10)
            print(f"You just rolled a {roll_10}.")

            roll_10 = random.randint(1,10)
            print(f"You just rolled a {roll_10}.")

            roll_10 = random.randint(1,10)
            print(f"You just rolled a {roll_10}.")

            roll_10 = random.randint(1,10)
            print(f"You just rolled a {roll_10}.")

            roll_10 = random.randint(1,10)
            print(f"You just rolled a {roll_10}.")

            roll_10 = random.randint(1,10)
            print(f"You just rolled a {roll_10}.")

            roll_10 = random.randint(1,10)
            print(f"You just rolled a {roll_10}.\n")

        elif self.sides == 20:
            roll_20 = random.randint(1,20)
            print(f"This is a {self.sides} sided die.")
            print(f"You just rolled a {roll_20}.")

            roll_20 = random.randint(1,20)
            print(f"You just rolled a {roll_20}.")

            roll_20 = random.randint(1,20)
            print(f"You just rolled a {roll_20}.")

            roll_20 = random.randint(1,20)
            print(f"You just rolled a {roll_20}.")

            roll_20 = random.randint(1,20)
            print(f"You just rolled a {roll_20}.")

            roll_20 = random.randint(1,20)
            print(f"You just rolled a {roll_20}.")

            roll_20 = random.randint(1,20)
            print(f"You just rolled a {roll_20}.")

            roll_20 = random.randint(1,20)
            print(f"You just rolled a {roll_20}.")

            roll_20 = random.randint(1,20)
            print(f"You just rolled a {roll_20}.")

            roll_20 = random.randint(1,20)
            print(f"You just rolled a {roll_20}.\n")

# Create instances
die_6 = Die()
die_6.roll_die()

die_10 = Die(sides=10)
die_10.roll_die()

die_20 = Die(sides=20)
die_20.roll_die()
