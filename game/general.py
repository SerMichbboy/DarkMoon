import pygame
from settings import Settings
import sys


def draw_text(text, _font, color, surface, x, y):
    textobj = _font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def are_you_sure(screen, clock):
    click = False
    font = pygame.font.SysFont(Settings.text_style, Settings.text_size)
    running = True
    draw_text('Are you sure', font, Settings.WHITE, screen, 460, 420)
    button_yes = pygame.Rect(465, 450, 40, 30)
    button_no = pygame.Rect(525, 450, 40, 30)
    draw_text('Yes', font, Settings.WHITE, screen, 470, 455)
    draw_text('No', font, Settings.WHITE, screen, 532, 455)
    while running:
        mx, my = pygame.mouse.get_pos()
        if button_yes.collidepoint((mx, my)):
            if click:
                pygame.quit()
                exit()
        if button_no.collidepoint((mx, my)):
            if click:
                break

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

