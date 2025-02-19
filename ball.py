import pygame
from constants import BALL_STEP

class Ball:
    def __init__(self, fighter):
        self.image = pygame.image.load('images/rocket.png')
        self.width, self.height = self.image.get_size()
        self.x, self.y = 0, 0
        self.step = BALL_STEP
        self.was_fired = False  # шар изначально невидим на экране
        self.fighter = fighter

    def fire(self):
        self.was_fired = True
        self.x = self.fighter.x + self.fighter.width / 2 - self.width / 2
        self.y = self.fighter.y - self.height

    def update_position(self):  #  перемещение мяча вверх
        if self.was_fired:
            self.y -= self.step

    def is_out_of_screen(self):  # проверка выхода мяча за границы экрана
        return  self.y + self.height < 0

    def reset(self):
        self.was_fired = False

    def is_collision(self, alien):  # есть ли столкновение или нет с alien
        return  (
            alien.x < self.x < alien.x + alien.width - self.width and
            alien.y < self.y < alien.y + alien.height - self.height
        )