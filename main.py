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
        pygame.draw.rect(screen, (183,166,114), fruit_rect)

class Snake:
    def __init__(self):
        # https://humberto.io/blog/exploring-pygame-2-drawing-on-screen/
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0) # moving to the right

    def draw_snake(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            # create a rect
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            # draw the rectangle
            pygame.draw.rect(screen,(180,116,114),block_rect)


    """We would like to execute this method at certain intervals => timer"""
    def move_snake(self):
        # snake move consist of removing last element of snake
        body_copy = self.body[:-1]  # we will copy only first two elements
        body_copy.insert(0, body_copy[0] + self.direction)      #insert new element right before at the start f the list
        self.body = body_copy[:]

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
fruit = Fruit()
snake = Snake()

#custom trigger
SCREEN_UPDATE = pygame.USEREVENT
# how often we would like to trigger our custom event, in ms
pygame.time.set_timer(SCREEN_UPDATE,150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            snake.move_snake()
        if event.type == pygame.KEYDOWN:
            # Controlling snake direction
            if event.key == pygame.K_UP:
                snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1,0)
    screen.fill((175,215,70))
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)