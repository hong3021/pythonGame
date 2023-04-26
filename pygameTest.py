import pygame
import os
from setting import *
from level import Level
from tiles import Tile

FPS = 60
WIDTH, HEIGHT = 1200, 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("kok adventure")
level = Level(level_map, screen)


def draw_window():
    screen.fill((135, 206, 235))
    level.run()
    pygame.display.update()


def main():

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()

    pygame.quit()


if __name__ == '__main__':
    main()