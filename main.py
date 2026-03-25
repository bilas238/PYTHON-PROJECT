import pygame
from engine import GameEngine
from data_manager import DataManager

def main():
    pygame.init()
    
    # Screen size as a Tuple
    screen_info = (800, 600)
    screen = pygame.display.set_mode(screen_info)
    pygame.display.set_caption("Space Escape")

    data_handler = DataManager()
    high_score = data_handler.load_score()

    # List and For Loop for showing massage 
    start_messages = ["Loading...", "High Score: " + str(high_score), "Game Starting!"]
    for text in start_messages:
        print(text)

    game = GameEngine(screen)

    # While Loop for game startswith
    
    running = True
    while running:
        score = game.run()
        data_handler.save_score(score)
        running = False 
    #when game closed loop is over

    pygame.quit()

if __name__ == "__main__":
    main()