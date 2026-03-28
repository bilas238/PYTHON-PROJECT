import pygame
import time
from models import Player, Enemy

class GameEngine:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player(375, 520)
        self.enemies = []
        self.score = 0
        # Font for score and messages
        self.font = pygame.font.SysFont("Arial", 32)
        self.WHITE = (255, 255, 255)

    # Function to display messages on screen
    def show_message(self, text, y_offset=0):
        msg = self.font.render(text, True, self.WHITE)
        rect = msg.get_rect(center=(400, 300 + y_offset))
        self.screen.blit(msg, rect)

    def run(self):
        clock = pygame.time.Clock()
        running = True
        
        while running:
            # Clear screen with black
            self.screen.fill((0, 0, 0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return self.score

            # Player movement
            keys = pygame.key.get_pressed()
            self.player.move(keys, 800)

            # Enemy spawning logic
            if pygame.time.get_ticks() % 60 == 0:
                self.enemies.append(Enemy(800))

            for enemy in self.enemies[:]:
                enemy.update()
                
                # Check for collision
                if enemy.rect.colliderect(self.player.rect):
                    # Show Game Over screen
                    self.screen.fill((50, 0, 0))
                    self.show_message("GAME OVER!", -30)
                    self.show_message(f"Final Score: {self.score}", 30)
                    pygame.display.flip()
                    # Pause for 2 seconds
                    time.sleep(2)
                    return self.score
                
                # Update score and remove enemy
                if enemy.rect.y > 600:
                    self.enemies.remove(enemy)
                    self.score += 1
                
                enemy.draw(self.screen)

            self.player.draw(self.screen)
            
            # Draw score board
            score_img = self.font.render(f"Score: {self.score}", True, self.WHITE)
            self.screen.blit(score_img, (15, 15))
            
            # Refresh display
            pygame.display.flip()
            # game speed 60 FPS
            clock.tick(60)