from settings import Settings
from general import draw_text, are_you_sure
from Play_game import game
import pygame
import sys


# __________________________________________________________________________________________

def pygame_init():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((Settings.menu_width, Settings.menu_height))
    pygame.display.set_caption("Dark Moon")
    clock = pygame.time.Clock()
    click = False
    font = pygame.font.SysFont(Settings.text_style, Settings.text_size)
    return screen, clock, click, font
# _________________________________________________________________________________________


def options(font, screen, clock):
    running = True
    draw_text('OPTIONS SCREEN', font, Settings.WHITE, screen, 20, 20)
    draw_text('AUDIO', font, Settings.WHITE, screen, 270, 455)
    draw_text('GRAPHICS', font, Settings.WHITE, screen, 250, 495)
    draw_text('EXIT', font, Settings.WHITE, screen, 270, 535)
    while running:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        clock.tick(60)


def main_menu():
    screen, clock, click, font = pygame_init()
    pygame.mixer.music.load('sounds/a5bf579ed23da4d.ogg')
    pygame.mixer.music.play()
    animation_mist = pygame.image.load('images/Frames/pngegg.png')
    animation_mist.set_alpha(75)
    animation_mist.get_rect()
    x, y, speed = -700, 230, 0.7

    while True:
        background_menu_image = pygame.image.load('images/1024x768-553071-moon-backgrounds.jpg')
        screen.blit(background_menu_image, (0, 0))
        x += speed

        if x >= Settings.menu_width:
            speed = -speed
        screen.blit(animation_mist, (x, y))
        pygame.transform.scale(background_menu_image, (1024, 768))

        mx, my = pygame.mouse.get_pos()

        start_button = pygame.Rect(190, 450, 200, 30)
        settings_button = pygame.Rect(190, 490, 200, 30)
        exit_button = pygame.Rect(190, 530, 200, 30)

        if start_button.collidepoint((mx, my)):
            if click:
                pygame.quit()
                game()
                break

        elif settings_button.collidepoint((mx, my)):
            if click:
                options(font, screen, clock)
        elif exit_button.collidepoint((mx, my)):
            if click:
                are_you_sure(screen, clock)

        draw_text('Main Menu', pygame.font.SysFont('Georgia', 13), Settings.WHITE, screen, 263, 425)
        draw_text('PLAY', font, Settings.WHITE, screen, 270, 455)
        draw_text('OPTIONS', font, Settings.WHITE, screen, 250, 495)
        draw_text('EXIT', font, Settings.WHITE, screen, 270, 535)

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    are_you_sure(screen, clock)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.mixer.Sound('sounds/10e1076dfd6c701.ogg').play()
                    click = True

        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)


while True:
    main_menu()
