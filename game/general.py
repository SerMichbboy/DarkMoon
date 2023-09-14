import pygame
from settings import Settings
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

    click = False
    running = True
    pygame.init()
    pygame.mixer.init()

    pygame.display.set_mode((Settings.menu_width, Settings.menu_height), pygame.NOFRAME)

    while running:
        background_menu_image = pygame.image.load('images/1024x768-553071-moon-backgrounds.jpg')
        screen.blit(background_menu_image, (0, 0))

        draw_text('AUDIO SETTINGS', font, Settings.WHITE, screen, 20, 20)
        draw_text('Music:', font, Settings.WHITE, screen, 250, 455)
        draw_text('Sounds:', font, Settings.WHITE, screen, 250, 495)

        mx, my = pygame.mouse.get_pos()

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

        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)


def graphics_set(font, screen, clock):

    click = False
    running = True
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_mode((Settings.menu_width, Settings.menu_height), pygame.NOFRAME)
    exit_button = pygame.Rect(190, 530, 200, 30)

    while running:
        background_menu_image = pygame.image.load('images/1024x768-553071-moon-backgrounds.jpg')
        screen.blit(background_menu_image, (0, 0))

        draw_text('GRAPHICS SETTINGS', font, Settings.WHITE, screen, 20, 20)
        draw_text('Screen:', font, Settings.WHITE, screen, 250, 455)
        draw_text('Details:', font, Settings.WHITE, screen, 250, 495)
        draw_text('Back', font, Settings.WHITE, screen, 250, 535)

        mx, my = pygame.mouse.get_pos()

        if exit_button.collidepoint((mx, my)):
            if click:
                are_you_sure(screen, clock)

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

        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)
