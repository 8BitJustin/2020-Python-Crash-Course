import sys
import pygame
from pygame.sprite import Group
from laser import Laser
from tiy_spaceship125_settings import Settings
from tiy_spaceship125 import Spaceship


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,
                                      settings.screen_height))
    pygame.display.set_caption("Side Shooter")

    ship = Spaceship(screen)
    lasers = Group()

    bg_color = settings.bg_color

    while True:

        ship.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.K_SPACE:
                new_laser = Laser(settings, screen, ship)
                lasers.add(new_laser)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True
                elif event.key == pygame.K_UP:
                    ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    ship.moving_down = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False
                elif event.key == pygame.K_UP:
                    ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    ship.moving_down = False

        screen.fill(bg_color)

        ship.blitme()

        pygame.display.flip()


run_game()