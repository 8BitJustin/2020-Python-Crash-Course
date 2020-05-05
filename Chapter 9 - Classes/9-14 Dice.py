from random import randint


class Die:
    """
    Creates Die class with six sides.

    Parameters:
        sides - Defaulted to six (6), can be altered to represent a different
        numerical value.

    Returns:
        Method of roll_die() will print random number between 1 and 6 (by
        default).
    """
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print(x)


six_side = Die()
ten_side = Die(10)
twenty_side = Die(20)


def roll_die_alot(die, rolls=10):
    """
    Function to roll dice numerous times.

    Parameters:
        die - Takes in the variable created from the Die() class.
        rolls - How many times the dice will roll. Defaulted to 10, can be
        left blank or another numerical value can added.

    Returns:
        The printed output of the roll_die() method within the Die() class.
    """

    n = 0
    while True:
        n += 1
        print(f"Roll {n}: ")
        die.roll_die()
        if n == rolls:
            break

    print("Complete!\n")


roll_die_alot(six_side)
roll_die_alot(ten_side, 3)
roll_die_alot(twenty_side, 5)

print(Die.__doc__)
