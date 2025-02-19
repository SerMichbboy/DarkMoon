import pygame
from .settings import Settings
import sys


def draw_text(text, _font, color, surface, x, y):
    textobj = _font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def are_you_sure(screen, clock, from_game=False):
    click = False
    font = pygame.font.SysFont(Settings.text_style, Settings.text_size)
    running = True
    if from_game:
        x, y = Settings.width_game // 2 - 60, Settings.height_game // 2
    else:
        x, y = Settings.menu_width // 2 - 60, Settings.menu_height // 2
    draw_text('Are you sure', font, Settings.WHITE, screen, x, y)
    button_yes = pygame.Rect(x + 10, y + 35, 40, 30)
    button_no = pygame.Rect(x + 62, y + 35, 40, 30)
    draw_text('Yes', font, Settings.WHITE, screen, x + 10, y + 35)
    draw_text('No', font, Settings.WHITE, screen, x + 62, y + 35)
    while running:
        mx, my = pygame.mouse.get_pos()
        if button_yes.collidepoint((mx, my)):
            if click:
                pygame.quit()
                return True
        if button_no.collidepoint((mx, my)):
            if click:
                return False

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.mixer.Sound('sounds/10e1076dfd6c701.ogg').play()
                    click = True

        pygame.display.update()
        clock.tick(60)


def audio_set(font, screen, clock):
    running = True

    # Задание начальной позиции кружка
    circle_radius, circle_x, circle_y = 8, 692, 464
    circle_x_2, circle_y_2 = 692, 504

    # Задание флага захвата кружка
    circle_grabbed = False

    while running:
        background_menu_image = pygame.image.load('images/1024x768-553071-moon-backgrounds.jpg')
        screen.blit(background_menu_image, (0, 0))

        draw_text('AUDIO SETTINGS', font, Settings.WHITE, screen, 20, 20)
        draw_text('Music:', font, Settings.WHITE, screen, 250, 455)
        draw_text('Sounds:', font, Settings.WHITE, screen, 250, 495)
        draw_text('<esc', font, Settings.WHITE, screen, 100, 700)

        pygame.draw.rect(screen, (200, 200, 200), (400, 455, 300, 20))
        pygame.draw.rect(screen, (200, 200, 200), (400, 495, 300, 20))

        # Функция для проверки, находится ли точка внутри прямоугольника
        def point_in_rect(x, y, rect_x, rect_y, rect_width, rect_height):
            return rect_x <= x <= rect_x + rect_width and rect_y <= y <= rect_y + rect_height

        # Отрисовка кружка
        pygame.draw.circle(screen, (50, 50, 50), (circle_x, circle_y), circle_radius)
        pygame.draw.circle(screen, (50, 50, 50), (circle_x_2, circle_y_2), circle_radius)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.mixer.Sound('sounds/10e1076dfd6c701.ogg').play()

            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Проверка, находится ли курсор внутри кружка
                    if point_in_rect(event.pos[0], event.pos[1], circle_x - circle_radius, circle_y - circle_radius,
                                     circle_radius * 2, circle_radius * 2) or point_in_rect(event.pos[0], event.pos[1],
                                                                                            circle_x_2 - circle_radius,
                                                                                            circle_y_2 - circle_radius,
                                                                                            circle_radius * 2,
                                                                                            circle_radius * 2):
                        circle_grabbed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    circle_grabbed = False
            elif event.type == pygame.MOUSEMOTION:
                if circle_grabbed:
                    # Обновление позиции кружка в соответствии с перемещением мыши
                    new_circle_x = circle_x + event.rel[0]
                    # Проверка, чтобы кружок не выходил за пределы внутреннего прямоугольника
                    if 400 + circle_radius <= new_circle_x <= 400 + 300 - circle_radius:
                        circle_x = new_circle_x
                    elif 400 + circle_radius <= new_circle_x <= 400 + 300 - circle_radius:
                        circle_x = new_circle_x
                    # Обновление громкости звука на основе позиции кружка
                    Settings.loudly = ((circle_x - 408) / 300)

        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)


def graphics_set(font, screen, clock):
    run = True
    # Задание начальной позиции кружка
    circle_radius, circle_x, circle_y = 8, 692, 464
    # Задание флага захвата кружка
    circle_grabbed = False
    while run:

        background_menu_image = pygame.image.load('images/1024x768-553071-moon-backgrounds.jpg')
        screen.blit(background_menu_image, (0, 0))

        draw_text('GRAPHICS SETTINGS', font, Settings.WHITE, screen, 20, 20)
        draw_text('Screen:', font, Settings.WHITE, screen, 250, 455)
        draw_text('Details:', font, Settings.WHITE, screen, 250, 495)
        draw_text('<esc', font, Settings.WHITE, screen, 100, 700)

        pygame.draw.rect(screen, (200, 200, 200), (400, 455, 300, 20))
        pygame.draw.rect(screen, (200, 200, 200), (400, 495, 300, 20))

        # Функция для проверки, находится ли точка внутри прямоугольника
        def point_in_rect(x, y, rect_x, rect_y, rect_width, rect_height):
            return rect_x <= x <= rect_x + rect_width and rect_y <= y <= rect_y + rect_height

        # Отрисовка кружка
        pygame.draw.circle(screen, (50, 50, 50), (circle_x, circle_y), circle_radius)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.mixer.Sound('sounds/10e1076dfd6c701.ogg').play()

            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    # Проверка, находится ли курсор внутри кружка
                    if point_in_rect(event.pos[0], event.pos[1], circle_x - circle_radius, circle_y - circle_radius,
                                     circle_radius * 2, circle_radius * 2):
                        circle_grabbed = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    circle_grabbed = False

            elif event.type == pygame.MOUSEMOTION:
                if circle_grabbed:
                    # Обновление позиции кружка в соответствии с перемещением мыши
                    new_circle_x = circle_x + event.rel[0]
                    # Проверка, чтобы кружок не выходил за пределы внутреннего прямоугольника
                    if 400 + circle_radius <= new_circle_x <= 400 + 300 - circle_radius:
                        circle_x = new_circle_x

        pygame.display.update()
        clock.tick(60)
