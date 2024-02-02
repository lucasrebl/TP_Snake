import pygame
import random

Red = (255, 0, 0)

GRID_SIZE = 20
SNAKE_SIZE = 20

class Food:
    def __init__(self, width, height):
        self.position = (0, 0)
        self.color = Red
        self.randomize_position(width, height)
        
    def randomize_position(self, width, height):
        self.position = (random.randint(0, (width // GRID_SIZE) -1) * GRID_SIZE, random.randint(0, (height // GRID_SIZE) -1) * GRID_SIZE)
        
    def render(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], SNAKE_SIZE, SNAKE_SIZE))