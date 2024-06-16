import pygame
import random
import time

pygame.init()

# Параметры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра тир")
icon = pygame.image.load("img/hc9c943f7d7054e45b89c41ccb087f8486-jpg.jpg")
pygame.display.set_icon(icon)

# Загрузка изображения цели
target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

# Начальные координаты цели
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Начальные параметры
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
score = 0
target_speed_x = 2
target_speed_y = 2

# Время окончания игры
game_duration = 30
start_time = time.time()

# Главный игровой цикл
running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    # Движение цели
    target_x += target_speed_x
    target_y += target_speed_y

    # Отскок от границ экрана
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y = -target_speed_y

    # Отрисовка цели
    screen.blit(target_img, (target_x, target_y))

    # Отображение очков
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Очки: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Обновление экрана
    pygame.display.update()

    # Проверка времени
    current_time = time.time()
    if current_time - start_time > game_duration:
        running = False

# Завершение игры
pygame.quit()
print(f"Игра окончена! Ваши очки: {score}")