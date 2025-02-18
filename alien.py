import pygame
from constants import SCREEN_WIDTH, ALIEN_STEP
from random import randint

class Alien:
    def __init__(self):
        self.image = pygame.image.load('image/alien.png')
        self.width, self.height = self.image.get_size()
        self.x, self.y = randint(0, SCREEN_WIDTH - self.width), 0
        self.step = ALIEN_STEP
        self.speed = self.step
        