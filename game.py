import pygame
import sys
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

    def run(self):
        while self.game_is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                self.handle_key_events(event)
            self.update_game_state()

    def handle_key_events(self, event):
        if event.type == pygame.KEYDOWN:  # если нажата одна из клавишь то выполняются соответствующие действия
            if event.key == pygame.K_LEFT:
                self.fighter.move_left() # для перемещения влево
            if event.key == pygame.K_RIGHT:
                self.fighter.move_right()
            if event.key == pygame.K_SPACE:
                self.ball.fire()
        if event.type == pygame.KEYUP:  # если клавиша отпущена движение корабля прекращается
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.fighter.stop_moving()

    def update_game_state(self):
        self.fighter.update_position()
        self.alien.update_position()
        self.ball.update_position()

        if self.ball.is_out_of_screen():
            self.ball.reset()

        if self.ball.is_collision(self.alien):
            self.ball.reset()
            self.alien.reset()
            self.game_score += 1

        if self.alien.has_reached_fighter(self.fighter):
            self.game_is_running = False
