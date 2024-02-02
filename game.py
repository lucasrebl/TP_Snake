import pygame
from snake import Snake
from food import Food

WHITE = (255, 255, 255)

class Game:
    def __init__(self, width, height):
        self.snake = Snake(width, height)
        self.food = Food(width, height)
        self.width = width
        self.score = 0
        
    def handle_key_event(self, event):
        from main import DIR_MAP
        if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
            self.snake.direction = DIR_MAP[event.key]
    
    def run(self, width, height, screen):
        clock = pygame.time.Clock()
        game_run = True
        
        while game_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_run = False
                elif event.type == pygame.KEYDOWN:
                    self.handle_key_event(event)
                    
            self.snake.update(width, height)
            self.collision(width, height)
            
            if self.snake.get_position_head_snake() == self.food.position:
                self.snake.longueur += 1
                self.food.randomize_position(width, height)
                self.score += 1
                    
            screen.fill(WHITE)
            self.food.render(screen)
            self.snake.render(screen)
            self.display_score(screen)
            pygame.display.flip()
            clock.tick(10)

        pygame.quit()
        quit()
        
    def collision(self, width, height):
        if self.snake.get_position_head_snake() in self.snake.position[1:]:
            self.snake.reset(width, height)
            self.score = 0
    
    def display_score(self, screen):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (0, 0, 0))
        screen.blit(score_text, (self.width - 150, 10))
