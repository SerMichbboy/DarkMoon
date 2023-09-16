import pygame

# Инициализация Pygame
pygame.init()

# Создание окна игры
width = 800
height = 400
window = pygame.display.set_mode((width, height))

# Задание цветов
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Задание размеров и координат прямоугольников
outer_rect_width = 400
outer_rect_height = 100
outer_rect_x = width // 2 - outer_rect_width // 2
outer_rect_y = height // 2 - outer_rect_height // 2

inner_rect_width = 300
inner_rect_height = 50
inner_rect_x = outer_rect_x + outer_rect_width // 2 - inner_rect_width // 2
inner_rect_y = outer_rect_y + outer_rect_height // 2 - inner_rect_height // 2

# Задание начальной позиции кружка
circle_radius = 25
circle_x = inner_rect_x + inner_rect_width // 2
circle_y = inner_rect_y + inner_rect_height // 2

# Задание флага захвата кружка
circle_grabbed = False

# Задание начальной громкости звука
volume_min = 0
volume_max = inner_rect_width
volume = volume_min

# Функция для проверки, находится ли точка внутри прямоугольника
def point_in_rect(x, y, rect_x, rect_y, rect_width, rect_height):
    return rect_x <= x <= rect_x + rect_width and rect_y <= y <= rect_y + rect_height

# Цикл событий и обновления экрана
running = True
while running:
    # Очистка экрана
    window.fill(WHITE)

    # Отрисовка внешнего прямоугольника
    pygame.draw.rect(window, GRAY, (outer_rect_x, outer_rect_y, outer_rect_width, outer_rect_height))

    # Отрисовка внутреннего прямоугольника
    pygame.draw.rect(window, BLUE, (inner_rect_x, inner_rect_y, inner_rect_width, inner_rect_height))

    # Отрисовка кружка
    pygame.draw.circle(window, RED, (circle_x, circle_y), circle_radius)

    # Обновление экрана
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                # Проверка, находится ли курсор внутри кружка
                if point_in_rect(event.pos[0], event.pos[1], circle_x - circle_radius, circle_y - circle_radius,
                                 circle_radius * 2, circle_radius * 2):
                    circle_grabbed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Левая кнопка мыши
                circle_grabbed = False
        elif event.type == pygame.MOUSEMOTION:
            if circle_grabbed:
                # Обновление позиции кружка в соответствии с перемещением мыши
                new_circle_x = circle_x + event.rel[0]
                # Проверка, чтобы кружок не выходил за пределы внутреннего прямоугольника
                if inner_rect_x + circle_radius<= new_circle_x <= inner_rect_x + inner_rect_width - circle_radius:
                    circle_x = new_circle_x
                # Обновление громкости звука на основе позиции кружка
                volume = int((circle_x - inner_rect_x) / inner_rect_width * (volume_max - volume_min) + volume_min)

pygame.quit()