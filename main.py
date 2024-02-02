import pygame
from game import Game

WIDTH = 600
HEIGHT = 400

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

DIR_MAP = {
    pygame.K_UP: UP,
    pygame.K_DOWN: DOWN,
    pygame.K_LEFT: LEFT,
    pygame.K_RIGHT: RIGHT
}

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.update()
pygame.display.set_caption('Snake game par lucas')

if __name__ == "__main__":
    game = Game(WIDTH, HEIGHT)
    game.run(WIDTH, HEIGHT, screen)