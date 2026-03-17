from __future__ import annotations
import pygame
import random

class GameObject:
    def __init__(self, x: int, y: int, size: int, color: tuple) -> None:
        self.rect = pygame.Rect(x, y, size, size)
        self.color = color

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.color, self.rect)

class Player(GameObject):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 50, (0, 255, 0))
        self.speed: int = 8

    def move(self, keys: any, screen_width: int) -> None:
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed

class Enemy(GameObject):
    def __init__(self, screen_width: int) -> None:
        x: int = random.randint(0, screen_width - 40)
        super().__init__(x, -50, 40, (255, 0, 0))
        self.speed: int = random.randint(4, 8)

    def update(self) -> None:
        self.rect.y += self.speed