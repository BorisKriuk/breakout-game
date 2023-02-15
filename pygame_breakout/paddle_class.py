import pygame
from utils import SCREEN_WIDTH, SCREEN_HEIGHT, COLS, PADDLE_COL, PADDLE_OUTLINE


class Paddle:
    def __init__(self, screen):
        self.reset(screen)

    def move(self):
        # reset movement direction
        self.direction = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.direction = -1
        if key[pygame.K_RIGHT] and self.rect.left < SCREEN_WIDTH - self.width:
            self.rect.x += self.speed
            self.direction = 1

    def draw(self):
        pygame.draw.rect(self.screen, PADDLE_COL, self.rect)
        pygame.draw.rect(self.screen, PADDLE_OUTLINE, self.rect, 3)

    def reset(self, screen):
        # define paddle variables
        self.screen = screen
        self.height = 20
        self.width = SCREEN_WIDTH / COLS
        self.x = SCREEN_WIDTH / 2 - self.width / 2
        self.y = SCREEN_HEIGHT - self.height * 2
        self.speed = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.direction = 0