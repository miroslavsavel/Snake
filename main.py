import sys
import pygame

# https://www.youtube.com/watch?v=QFvqStqPCRU
pygame.init()
screen = pygame.display.set_mode((400, 500))
clock = pygame.time.Clock()
test_surface = pygame.Surface((100,200))
green = (175,215,70)
test_surface.fill((0,0,255))
x_pos = 200

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #screen.fill(pygame.Color('gold'))   # pygame.color
    screen.fill(green)
    x_pos -= 1
    #top left point at 200 and 250
    screen.blit(test_surface,(200,x_pos))   # block image transfer
    pygame.display.update()
    clock.tick(60)