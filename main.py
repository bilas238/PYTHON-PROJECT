import pygame
from engine import GameEngine
from data_manager import DataManager

def main():
    pygame.init()
    
    # Screen size as tuple
    
    screen_info = (800, 600)
    screen = pygame.display.set_mode(screen_info)
    pygame.display.set_caption("Space Escape")

    # Defining Game Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    
    data_handler = DataManager()
    high_score = data_handler.load_score()

    # List & For Loop use for showing massage at starting time 
    
    status_updates = ["Checking Files...", "High Score: " + str(high_score), "Game Loading!"]
    for status in status_updates:
        print(status)

    game = GameEngine(screen)

    # playing game 
    running = True
    while running:
        
        
        # Filling screen with BLACK color 
        
        screen.fill(BLACK) 
        
        score = game.run()
        data_handler.save_score(score)
        running = False 

    pygame.quit()

if __name__ == "__main__":
    main()