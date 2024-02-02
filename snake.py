import pygame
import random

Blue = (0, 0, 255)

GRID_SIZE = 20
SNAKE_SIZE = 20

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self, width, height):
        self.longueur = 1
        self.color = Blue
        self.position = [[width // 2, height // 2]]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        
    def get_position_head_snake(self):
        return self.position[0]
    
    def update(self, width, height):
        current_position = self.get_position_head_snake()
        horizontal, vertical = self.direction
        new_position = (((current_position[0] + (horizontal * GRID_SIZE)) % width), (current_position[1] + (vertical * GRID_SIZE)) % height)
        if len(self.position) > 2 and new_position in self.position[2:]:
            self.reset()
        else:
            self.position.insert(0, new_position)
            if len(self.position) > self.longueur:
                self.position.pop()
    
    def render(self, surface):
        for position in self.position:
            pygame.draw.rect(surface, self.color, (position[0], position[1], SNAKE_SIZE, SNAKE_SIZE))
    
    def reset(self, width, height):
        self.longueur = 1
        self.position = [[width // 2, height // 2]]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])