import pygame
from fighter import Fighter
from alien import Alien
from ball import Ball
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_FILL_COLOR, GAME_CAPTION

class Game:
    def __init__(self):
        pygame.display.set_caption(GAME_CAPTION)
        self.screen_width, self.screen_height = SCREEN_WIDTH, SCREEN_HEIGHT
        self.screen_fill_color = SCREEN_FILL_COLOR
        self.screen = pygame.display.set_mode(self.screen_width, self.screen_height)
        self.game_font = pygame.font.Font(None, 30)
        self.game_score = 0

        self.fighter = Fighter
        self.alien = Alien()
        self.ball = Ball(self.fighter)

        self.game_is_running = True
        