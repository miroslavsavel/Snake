import sys
import pygame
from settings import Settings
from snake import Snake

class SnakeGame:
    """Overall class to manage game assets and behviour"""

    def __init__(self):
        pygame.init()
        self.settings = Settings() #in the Settings class are defined properties of game
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("SSSnake")
        self.snake = Snake(self)  # creating ship object with parameter on the object itself

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.snake.update()
            self._update_screen()

    def _check_events(self):
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # Redraw the screen each pass through the loop
        self.screen.fill(self.settings.bg_color)
        pygame.draw.rect(self.screen, self.snake.color, self.snake.head)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance and run the game
    game_instance = SnakeGame()
    game_instance.run_game()