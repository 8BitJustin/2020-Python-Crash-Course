import sys
import pygame


def make_star():

    pygame.init()

    screen = pygame.display.set_mode((500, 500))

    pygame.display.set_caption("Star!")

    bg = (200, 200, 200)

    star = pygame.image.load('images/star01.png')

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg)

        screen.blit(star, (0, 0))

        pygame.display.flip()


make_star()