import pygame
import random

class GameObject:
    def __init__(self, x, y, size, color):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class Player(GameObject):
    def __init__(self, x, y):
        #class constructor
        super().__init__(x, y, 50, (0, 255, 0))
        self.speed = 8

    def move(self, keys, screen_width):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x = self.rect.x - self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x = self.rect.x + self.speed

class Enemy(GameObject):
    def __init__(self, screen_width):
        size = 40
        x = random.randint(0, screen_width - size)
        y = -size
        super().__init__(x, y, size, (255, 0, 0))
        self.speed = random.randint(3, 7)

    def update(self):
        self.rect.y = self.rect.y + self.speed