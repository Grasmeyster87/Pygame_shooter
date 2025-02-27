import pygame
import sys
from random import randint

pygame.init()

game_font = pygame.font.Font(None, 30)  # шрифт для игры

screen_width, screen_height = 800, 600
screen_fill_color = (32, 52, 71)
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Awesome Shooter Game")

FIGHTER_STEP = 0.2  # скорость перемещения корабля

fighter_image = pygame.image.load('images/fighter.png')
fighter_width, fighter_height = fighter_image.get_size()
fighter_x, fighter_y = screen_width / 2 - fighter_width / 2, screen_height - fighter_height
fighter_is_moving_left, fighter_is_moving_right = False, False

BALL_STEP = 0.3
ball_image = pygame.image.load('images/rocket.png')
ball_width, ball_height = ball_image.get_size()
ball_x, ball_y = 0, 0 # fighter_x + fighter_width / 2 - ball_width / 2, fighter_y - ball_height
ball_was_fired = False

ALIEN_STEP = 0.02
alien_speed = ALIEN_STEP
alien_image = pygame.image.load('images/alien.png')  # импорт изображения
alien_width, alien_height = alien_image.get_size()  # определим размеры изображения
alien_x, alien_y = randint(0, screen_width - alien_width), 0  # начальные координаты выбирается начальным образом

game_is_running = True

game_score = 0  # счетчик попаданий
while game_is_running:
    for event in pygame.event.get():  # обработка событий внутри цыкла
        if event.type == pygame.QUIT:   #  если событие завершено завершается игровой процес
            sys.exit()
        if event.type == pygame.KEYDOWN:  # если нажата одна из клавишь то выполняются соответствующие действия
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = True # для перемещения влево
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = True
            if event.key == pygame.K_SPACE:
                ball_was_fired = True
                ball_x = fighter_x + fighter_width / 2 - ball_width / 2
                ball_y = fighter_y - ball_height
        if event.type == pygame.KEYUP:  # если клавиша отпущена движение корабля прекращается
                if event.key == pygame.K_LEFT:
                    fighter_is_moving_left = False
                if event.key == pygame.K_RIGHT:
                    fighter_is_moving_right = False

    if fighter_is_moving_left and fighter_x >= FIGHTER_STEP:   # процес перемещения влево
        fighter_x -= FIGHTER_STEP  # изменение координаты X для корабля

    if fighter_is_moving_right and fighter_x <= screen_width - fighter_width - FIGHTER_STEP:
        fighter_x += FIGHTER_STEP

    # print(ball_was_fired)
    # alien_y += ALIEN_STEP  # изменение координаты y для инопланетянина на шаг
    alien_y += alien_speed  # изменение координаты по оси у инопланетянина

    if ball_was_fired and ball_y + ball_height < 0:
        ball_was_fired = False

    if ball_was_fired:  # если шарик виден на экране то мы перемещаем його по оси у вверх
        ball_y -= BALL_STEP

    screen.fill(screen_fill_color)  # вывести изображение фона
    screen.blit(fighter_image, (fighter_x, fighter_y))  # вывести истребитель
    screen.blit(alien_image, (alien_x, alien_y))  # показать инопланетянина на экране

    # если ball_was_fired то ресуем шарик на экране
    if ball_was_fired:
        screen.blit(ball_image, (ball_x, ball_y))

    # Счетчик попаданий
    game_score_text = game_font.render(f"Your Score is: {game_score}", True, 'white')
    screen.blit(game_score_text, (20, 20))

    pygame.display.update() # функция для обновления всех изменений на экране

    # проверка дошло ли изображение с инопланетянином до изображения с кораблем

    if alien_y + alien_height > fighter_y:  # достиг ли инопланетянин границы с кораблем
        game_is_running = False  # логическое значение для выхода из цикла

    # удаление шарика с экрана и перемещение инопланетянина в начальную позицию
    # попал ли шарик по инопланетянину
    if ball_was_fired and \
            alien_x < ball_x < alien_x + alien_width - ball_width and \
            alien_y < ball_y < alien_y + alien_height - ball_height:
        ball_was_fired = False  # скрытие шарика
        # перемещаем шарик с изображением инопланетянина наверх
        alien_x, alien_y = randint(0, screen_width - alien_width), 0
        alien_speed += ALIEN_STEP / 2 # увеличение скорости инопланетянина
        game_score += 1


game_over_text = game_font.render("Game Over", True, 'white')
game_over_rectangle = game_over_text.get_rect() # создание текста в прямоугольнике
game_over_rectangle.center = (screen_width / 2, screen_height / 2)  # определение координат центра всего экрана для вывода прямоугольника с текстом
screen.blit(game_over_text, game_over_rectangle)  # тобразить текст по центру экран

pygame.display.update()  # обновить екран
pygame.time.wait(5000) # задержка для чтения текста

pygame.quit()
