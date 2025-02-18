import pygame
from constants import BALL_STEP

class Ball:
    def __init__(self, fighter):
        self.image = pygame.image.load('images/ball.png')
        self.width, self.height = self.image.get_size()
        self.x, self.y = 0, 0
        self.step = BALL_STEP
        self.was_fired = False
        self.fighter = fighter