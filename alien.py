import pygame
from constants import SCREEN_WIDTH, ALIEN_STEP
from random import randint

class Alien:
    def __init__(self):
        self.image = pygame.image.load('images/alien.png') # добавление фото пришельца
        self.width, self.height = self.image.get_size()  # получение размера фото
        self.x, self.y = randint(0, SCREEN_WIDTH - self.width), 0  # получение случайных координат для появления пришельца
        self.step = ALIEN_STEP  # начальная скорость пришельца
        self.speed = self.step  # изменение скорости пришельца

    def update_position(self):  # перемещение инопланетянина вниз
        self.y +=self.speed

    def increase_speed(self):  # увеличение скорости
        self.speed += self.step / 2

    def reset(self):  # сброс позиции и возврат инопланетянина в исходную позицию
        self.increase_speed()
        self.x, self.y = randint(0, SCREEN_WIDTH - self.width), 0

    def has_reached_fighter(self, fighter):  # метод проверяе достиг ли инопланетянин fighter
        return self.y + self.height > fighter.y