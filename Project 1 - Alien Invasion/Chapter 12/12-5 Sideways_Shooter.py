"""Make a game that begins with a rocket in the center of the screen. Allow
the player to move the rocket up, down, left, or right using the four arrow
keys. Make sure the rocket never moves beyond any edge of the screen."""

import sys
import pygame
from tiy_spaceship125 import Spaceship


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Side Shooter")

    ship = Spaceship(screen)

    bg_color = (135, 206, 235)

    while True:
        ship.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

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