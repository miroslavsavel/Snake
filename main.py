import sys
import pygame
from settings import Settings

class SnakeGame:
    """Overall class to manage game assets and behviour"""

    def __init__(self):
        pygame.init()
        self.settings = Settings() #in the Settings class are defined properties of game
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("SSSnake")

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

if __name__ == '__main__':
    #Make a game instance and run the game
    game_instance = SnakeGame()
    game_instance.run_game()