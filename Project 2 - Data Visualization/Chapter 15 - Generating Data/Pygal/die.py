from random import randint


class Die:
    """A class representing a single die."""

    def __init__(self, sides=6):
        """Six-sided die by default."""
        self.sides = sides

    def roll(self):
        """Returns random int between 1 and the side of die (default 6)."""
        return randint(1, self.sides)

