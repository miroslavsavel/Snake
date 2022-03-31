import sys
import pygame

# https://www.youtube.com/watch?v=QFvqStqPCRU
pygame.init()
screen = pygame.display.set_mode((400, 500))
clock = pygame.time.Clock()
test_surface = pygame.Surface((100,200))
green = (175,215,70)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #screen.fill(pygame.Color('gold'))   # pygame.color
    screen.fill(green)

    screen.blit(test_surface,(200,250))   # block image transfer
    pygame.display.update()
    clock.tick(60)