import pygame

# Инициализация Pygame
pygame.init()

# Создание окна игры
width = 800
height = 600
window = pygame.display.set_mode((width, height))

# Загрузка изображения для вращения
image = pygame.image.load("game/images/Frames/main_chr/run1.png")

# Задание начальной позиции изображения
x = 400 - image.get_width() // 2  # Положение изображения по центру окна
y = 300 - image.get_height() // 2

# Задание смещения центра вращения
rotation_center_x = x + image.get_width() // 6   # X-координата центра вращения
rotation_center_y = y + image.get_height() // 6  # Y-координата центра вращения

# Угол поворота
angle = 0

# Цикл событий и обновления экрана
running = True
while running:
    # Очистка экрана
    window.fill((255, 255, 255))

    # Расчет повернутого изображения
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=(rotation_center_x, rotation_center_y))

    # Отображение повернутого изображения на экране
    window.blit(rotated_image, rotated_rect.topleft)

    # Обновление экрана
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление угла поворота
    angle += 1  # Увеличение угла поворота (пример)

pygame.quit()