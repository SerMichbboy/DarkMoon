import os
import sys
import pygame
from .settings import Settings
from .general import draw_text, are_you_sure, audio_set, graphics_set
from .Play_game import game

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def pygame_init():
    """Инициализация Pygame и создание окна."""
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((Settings.menu_width, Settings.menu_height), pygame.NOFRAME)
    pygame.display.set_caption("Dark Moon")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(Settings.text_style, Settings.text_size)
    return screen, clock, font


def load_image(path):
    """Загрузка изображения из указанного пути."""
    return pygame.image.load(path)


def load_sound(path):
    """Загрузка звука из указанного пути."""
    return pygame.mixer.Sound(path)


def options(font, screen, clock):
    """Функция для отображения меню настроек."""
    running = True
    click = False
    draw_text('OPTIONS SCREEN', font, Settings.WHITE, screen, 20, 20)
    draw_text('AUDIO', font, Settings.WHITE, screen, 270, 455)
    draw_text('GRAPHICS', font, Settings.WHITE, screen, 250, 495)

    audio_button = pygame.Rect(190, 450, 200, 30)
    graphics_button = pygame.Rect(190, 490, 200, 30)

    while running:
        mx, my = pygame.mouse.get_pos()

        if audio_button.collidepoint((mx, my)) and click:
            audio_set(font, screen, clock)

        if graphics_button.collidepoint((mx, my)) and click:
            graphics_set(font, screen, clock)

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                load_sound('sounds/10e1076dfd6c701.ogg').play()
                click = True

        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)


def main_menu():
    """Функция для отображения главного меню."""
    screen, clock, font = pygame_init()
    
    pygame.mixer.music.set_volume(Settings.loudly)
    pygame.mixer.music.load('sounds/a5bf579ed23da4d.ogg')
    pygame.mixer.music.play(-1)
    
    animation_mist = load_image('images/Frames/pngegg.png')
    animation_mist.set_alpha(75)
    x, y, speed = -700, 230, 0.7

    while True:
        background_menu_image = load_image('images/1024x768-553071-moon-backgrounds.jpg')
        screen.blit(background_menu_image, (0, 0))
        x += speed

        if x >= Settings.menu_width:
            speed = -speed
        screen.blit(animation_mist, (x, y))

        mx, my = pygame.mouse.get_pos()
        start_button = pygame.Rect(190, 450, 200, 30)
        settings_button = pygame.Rect(190, 490, 200, 30)
        exit_button = pygame.Rect(190, 530, 200, 30)

        if start_button.collidepoint((mx, my)) and pygame.mouse.get_pressed()[0]:
            pygame.quit()
            game()
            break
        elif settings_button.collidepoint((mx, my)) and pygame.mouse.get_pressed()[0]:
            options(font, screen, clock)
        elif exit_button.collidepoint((mx, my)) and pygame.mouse.get_pressed()[0]:
            are_you_sure(screen, clock)

        draw_text('Main Menu', pygame.font.SysFont('Georgia', 13), Settings.WHITE, screen, 263, 425)
        draw_text('PLAY', font, Settings.WHITE, screen, 270, 455)
        draw_text('OPTIONS', font, Settings.WHITE, screen, 250, 495)
        draw_text('EXIT', font, Settings.WHITE, screen, 270, 535)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                are_you_sure(screen, clock)

        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    while True:
        main_menu()
