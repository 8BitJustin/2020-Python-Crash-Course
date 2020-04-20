import pygame
from pygame.sprite import Group
from tiy_spaceship125_settings import GameSettings
from tiy_spaceship125 import Spaceship
import tiy_spaceship125_events as vents


def run_game():
    pygame.init()
    settings = GameSettings()
    screen = pygame.display.set_mode((settings.screen_width,
                                      settings.screen_height))
    pygame.display.set_caption("Side Shooter")

    ship = Spaceship(settings, screen)
    lasers = Group()

    while True:
        vents.check_events(settings, screen, ship, lasers)
        ship.update()
        lasers.update()
        vents.update_lasers(lasers)
        vents.update_screen(settings, screen, ship, lasers)


run_game()