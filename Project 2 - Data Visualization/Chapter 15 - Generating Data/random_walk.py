from random import choice

class RandomWalk:
    """A class to generate random walk."""

    def __init__(self, num_points):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

