import sys
import pygame
from pygame.math import Vector2
import random
# https://www.youtube.com/watch?v=QFvqStqPCRU

class Fruit:
    def __init__(self):
        self.x = random.randint(0, cell_number-1)
        self.y = random.randint(0, cell_number-1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size,cell_size,cell_size)
        pygame.draw.rect(screen, (126,166,114), fruit_rect)

class Snake:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]

    def draw_snake(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            # create a rect
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            # draw the rectangle
            pygame.draw.rect(screen,(180,126,114),block_rect)

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
fruit = Fruit()
snake = Snake()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((175,215,70))
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)