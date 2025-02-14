import pygame
import sys

from pygame.examples.scrap_clipboard import screen

# from random import randint

# clock = pygame.time.Clock()

screen_width, screen_height = 800, 600

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("My Pygame")
fill_color = (32, 52, 71)

rect_width, rect_height = 100, 200
rect_x = screen_width / 2 - rect_width / 2
rect_y = screen_height / 2 - rect_height / 2

rect_color = pygame.Color('light yellow')

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(fill_color)
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))
    # screen.fill((randint(0, 255), randint(0, 255), randint(0, 255)))
    # screen.fill(pygame.Color('yellow'))
    # screen.fill((255, 0, 0))
    pygame.display.update()
    # clock.tick(1)