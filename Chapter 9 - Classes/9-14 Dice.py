from random import randint


class Die():
    """
    Creates Die class with default of six sides (can be altered if another
    parameter is provided.
    """
    def __init__(self, sides=6):
        self.sides = sides

    """
    This will roll the die, and give a random number from 1 to 6.
    """

    def roll_die(self):
        x = randint(1, self.sides)
        print(x)


"""
Variables for 6, 10, and 20 sided-die created.
"""
six_side = Die()
ten_side = Die(10)
twenty_side = Die(20)


def roll_die(die, rolls=10):
    """
    Function to roll die 10 times. Takes variable of created die.
    """

    n = 0
    while True:
        """
        F string is used, prints which roll and number provided. Once 11 is hit,
        the loop closes.
        """

        n += 1
        print(f"Roll {n}: ")
        die.roll_die()
        if n == rolls:
            break

    print("Complete!\n")


roll_die(six_side)
roll_die(ten_side,3)
roll_die(twenty_side,5)
