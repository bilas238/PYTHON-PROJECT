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

            keys = pygame.key.get_pressed()
            self.player.move(keys, 800)

            if random.randint(1, 30) == 1:
                self.enemies.append(Enemy(800))

            for enemy in self.enemies[:]:
                enemy.update()
                if enemy.rect.colliderect(self.player.rect):
                    return self.score
                if enemy.rect.y > 600:
                    self.enemies.remove(enemy)
                    self.score += 1
                enemy.draw(self.screen)

            self.player.draw(self.screen)
            score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            self.screen.blit(score_text, (10, 10))
            pygame.display.flip()
            clock.tick(60)
        return self.score
