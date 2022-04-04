import sys
import pygame
from pygame.math import Vector2
import random
# https://www.youtube.com/watch?v=QFvqStqPCRU

class Fruit:
    def __init__(self):
        self.randomize_position()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size,cell_size,cell_size)
        pygame.draw.rect(screen, (183,166,114), fruit_rect)

    def randomize_position(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class Snake:
    def __init__(self):
        # https://humberto.io/blog/exploring-pygame-2-drawing-on-screen/
        # this direction of block in snake body is easy way how to overcome check fail self body
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0) # moving to the right
        self.new_block = False

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
        if self.new_block == True:
            # grow snake body after eating the fruit
            body_copy = self.body[:]  # we will copy only first two elements
            body_copy.insert(0,body_copy[0] + self.direction)  # insert new element right before at the start f the list
            self.body = body_copy[:]
            self.new_block = False
        else:
            # snake move consist of removing last element of snake
            body_copy = self.body[:-1]  # we will copy only first two elements
            body_copy.insert(0, body_copy[0] + self.direction)      #insert new element right before at the start f the list
            self.body = body_copy[:]



    """Add block to the body after eating the fruit"""
    def add_block(self):
        self.new_block = True

class MAIN_GAME_LOGIC:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    """Check if fruit and snake are on the same spot on the grid"""
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            print('snack')
            # reposition the fruit
            self.fruit.randomize_position()
            # add another block to the snake
            self.snake.add_block()

    def check_fail(self):
        # check if snake is out of screen boundary
        # LEFT and RIGHT
        if not 0 <= self.snake.body[0].x < cell_number:
            self.game_over()
        # UP and BOTTOM
        if not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        #check collision with itself - hit to the snake body, if head collide with every block
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

main_game = MAIN_GAME_LOGIC()

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
            main_game.update()
        if event.type == pygame.KEYDOWN:
            # Controlling snake direction
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:        # to prevent forbidden sudden direction change
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
    screen.fill((175,215,70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)