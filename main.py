import sys
import pygame
from pygame.math import Vector2
# https://www.youtube.com/watch?v=QFvqStqPCRU

class Fruit:
    def __init__(self):
        self.x = 0
        self.y = 1
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size,cell_size,cell_size)
        pygame.draw.rect(screen, (126,166,114), fruit_rect)




pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
fruit = Fruit()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((175,215,70))
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(60)