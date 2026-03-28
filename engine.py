import pygame
import time
from models import Player, Enemy

class GameEngine:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player(375, 520)
        self.enemies = []
        self.score = 0
        # Font for scores and messages
        self.font = pygame.font.SysFont("Arial", 32)
        self.WHITE = (255, 255, 255)

    # show any message on screen
    def show_message(self, text, y_offset=0):
        msg = self.font.render(text, True, self.WHITE)
        rect = msg.get_rect(center=(400, 300 + y_offset))
        self.screen.blit(msg, rect)

    def run(self):
        clock = pygame.time.Clock()
        running = True
        # Variable to check if game is paused
        paused = False
        
        while running:
            # Quit or Key Press
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return self.score
                
                # Check if 'P' key is pressed to pause
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        paused = not paused

            # Logic if game is paused
            if paused:
                # Show pause messages
                self.show_message("GAME PAUSED", -30)
                self.show_message("Press 'P' to Resume", 30)
                pygame.display.flip()
                clock.tick(10)
                # Skip the rest of the game loop
                continue

            # --- GAME LOGIC STARTS HERE ---
            
            # Clear screen with black
            self.screen.fill((0, 0, 0))

            # Move player using keys
            keys = pygame.key.get_pressed()
            self.player.move(keys, 800)

            # Spawn new enemy
            if pygame.time.get_ticks() % 60 == 0:
                self.enemies.append(Enemy(800))

            # Update all enemies
            for enemy in self.enemies[:]:
                enemy.update()
                
                # If player hits an enemy
                if enemy.rect.colliderect(self.player.rect):
                    # Show Game Over screen
                    self.screen.fill((50, 0, 0))
                    self.show_message("GAME OVER!", -30)
                    self.show_message(f"Final Score: {self.score}", 30)
                    pygame.display.flip()
                    # Wait 2 seconds
                    time.sleep(2)
                    return self.score
                
                # If enemy passes the screen
                if enemy.rect.y > 600:
                    self.enemies.remove(enemy)
                    self.score += 1
                
                enemy.draw(self.screen)

            # Draw player
            self.player.draw(self.screen)
            
            # Show current score
            score_img = self.font.render(f"Score: {self.score}", True, self.WHITE)
            self.screen.blit(score_img, (15, 15))
            
            # Update screen
            pygame.display.flip()
            # game speed 60 fps
            clock.tick(60)