class GameSettings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings.
        self.ship_speed_factor = .5

        # Laser Settings.
        self.laser_speed_factor = 1
        self.laser_width = 12
        self.laser_height = 2
        self.laser_color = 60, 60, 60
        self.lasers_allowed = 5
