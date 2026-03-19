import pygame
import random
from models import Player, Enemy

class GameEngine:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player(375, 520)
        self.enemies = []
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 24)

    def run(self):
        clock = pygame.time.Clock()
        running = True
        
        while running:
            # clear screen
            self.screen.fill((0, 0, 0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return self.score

            # player movement
            keys = pygame.key.get_pressed()
            self.player.move(keys, 800)

            if random.randint(1, 30) == 1:
                self.enemies.append(Enemy(800))

            # update enemies list
            for enemy in self.enemies[:]:
                enemy.update()
                
                # collision
                if enemy.rect.colliderect(self.player.rect):
                    return self.score
                
                #  update score
                if enemy.rect.y > 600:
                    self.enemies.remove(enemy)
                    self.score = self.score + 1
                
                enemy.draw(self.screen)

          
            self.player.draw(self.screen)
            
            # score board
            score_txt = "Score: " + str(self.score)
            score_img = self.font.render(score_txt, True, (255, 255, 255))
            self.screen.blit(score_img, (10, 10))
            
            pygame.display.flip()
            clock.tick(60)
            
        return self.score