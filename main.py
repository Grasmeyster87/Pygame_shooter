import pygame
import sys
# from random import randint

# clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Pygame")



while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 255, 0), (0, 0, 100, 200))
    # screen.fill((randint(0, 255), randint(0, 255), randint(0, 255)))
    # screen.fill(pygame.Color('yellow'))
    # screen.fill((255, 0, 0))
    pygame.display.update()
    # clock.tick(1)