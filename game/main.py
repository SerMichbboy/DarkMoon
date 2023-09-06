import pygame
import sys

# __________________________________________________________________________________________

pygame.init()
pygame.mixer.init()
width = 1024
height = 768
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dark Moon")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Georgia', 20)
click = False


# __________________________________________________________________________________________


def draw_text(text, _font, color, surface, x, y):
    textobj = _font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def options():
    running = True
    draw_text('OPTIONS SCREEN', font, (255, 255, 255), screen, 20, 20)
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


def game():
    running = True
    draw_text('GAME SCREEN', font, (255, 255, 255), screen, 20, 20)
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


def are_you_sure():
    global click
    running = True
    draw_text('Are you sure', font, (255, 255, 255), screen, 460, 420)
    button_yes = pygame.Rect(465, 450, 40, 30)
    button_no = pygame.Rect(525, 450, 40, 30)
    draw_text('Yes', font, (255, 255, 255), screen, 470, 455)
    draw_text('No', font, (255, 255, 255), screen, 532, 455)
    while running:
        mx, my = pygame.mouse.get_pos()
        if button_yes.collidepoint((mx, my)):
            if click:
                pygame.quit()
                exit()
        if button_no.collidepoint((mx, my)):
            if click:
                break

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


def main_menu():
    global click
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
        if x >= width:
            speed = -speed
        screen.blit(animation_mist, (x, y))

        pygame.transform.scale(background_menu_image, (1024, 768))

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(190, 450, 200, 30)
        button_2 = pygame.Rect(190, 490, 200, 30)
        button_3 = pygame.Rect(190, 530, 200, 30)

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        elif button_2.collidepoint((mx, my)):
            if click:
                options()
        elif button_3.collidepoint((mx, my)):
            if click:
                are_you_sure()

        draw_text('Main Menu', pygame.font.SysFont('Georgia', 13), (250, 250, 250), screen, 263, 425)
        draw_text('PLAY', font, (255, 255, 255), screen, 270, 455)
        draw_text('OPTIONS', font, (255, 255, 255), screen, 250, 495)
        draw_text('EXIT', font, (255, 255, 255), screen, 270, 535)

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.mixer.Sound('sounds/10e1076dfd6c701.ogg').play()
                    click = True

        screen.blit(animation_mist, (x, y))
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)


main_menu()
