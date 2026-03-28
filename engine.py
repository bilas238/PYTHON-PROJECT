import pygame
import time
from models import Player, Enemy

class GameEngine:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player(375, 520)
        self.enemies = []
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 32)
        self.WHITE = (255, 255, 255)

    def show_message(self, text, y_offset=0):
        msg = self.font.render(text, True, self.WHITE)
        rect = msg.get_rect(center=(400, 300 + y_offset))
        self.screen.blit(msg, rect)

    def run(self):
        clock = pygame.time.Clock()
        running = True
        
        while running:
            self.screen.fill((0, 0, 0))

            # BLACK tuple
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return self.score

            keys = pygame.key.get_pressed()
            self.player.move(keys, 800)

            if pygame.time.get_ticks() % 60 == 0: 
                
                # Simple spawn timer
                self.enemies.append(Enemy(800))

            for enemy in self.enemies[:]:
                enemy.update()
                if enemy.rect.colliderect(self.player.rect):
                   
                   # GAME OVER SCREEN 
                    
                 if enemy.rect.colliderect(self.player.rect):
            # GAME OVER SCREEN
            self.screen.fill((50, 0, 0)) 
            
            # Dark Red background
            
            self.show_message("GAME OVER!", -30)
            self.show_message(f"Final Score: {self.score}", 30)
            pygame.display.flip()
            time.sleep(2) 
            # Pause 2 seconds
            
            return self.score   
                  return self.score
                
                if enemy.rect.y > 600:
                    self.enemies.remove(enemy)
                    self.score += 1
                enemy.draw(self.screen)

            self.player.draw(self.screen)
            score_img = self.font.render(f"Score: {self.score}", True, self.WHITE)
            self.screen.blit(score_img, (15, 15))
            
            pygame.display.flip()
            clock.tick(60)