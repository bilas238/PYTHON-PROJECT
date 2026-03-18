import pygame
import random
from models import Player, Enemy

class GameEngine:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.player = Player(375, 520)
        self.enemies: list[Enemy] = []
        self.score: int = 0
        self.font = pygame.font.SysFont("Arial", 24)

    def run(self) -> int:
        clock = pygame.time.Clock()
        running = True
        while running:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return self.score
          
            pygame.display.flip()
            clock.tick(60)
        return self.score