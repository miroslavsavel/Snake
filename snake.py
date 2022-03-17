import pygame

class Snake:
    """A class to manage the snake"""

    def __init__(self, game_instance):
        """Initialize the snake head and sets its random starting position"""
        self.screen = game_instance.screen
        self.settings = game_instance.settings
        self.screen_rect = game_instance.screen.get_rect()
        # draw snake head - red rectangle at random position
        # Initialing Color
        self.color = (255, 0, 0)
        # Drawing Rectangle
        #pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
        self.head = pygame.Rect(30, 30, 60, 60)


    def blitme(self):
        """Draw the snake head at its current location"""
        # https://stackoverflow.com/questions/37800894/what-is-the-surface-blit-function-in-pygame-what-does-it-do-how-does-it-work
        # self.screen.blit(self.screen, self.head)

    def update(self):
        """Update the snake's position based on the current direction movement flag."""
