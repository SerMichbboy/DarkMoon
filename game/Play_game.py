import pygame
import sys


def game():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Dark Moon")
    clock = pygame.time.Clock()
    click = False
    level_pick = pygame.image.load('images/stoneheart_1.jpg')
    screen.blit(level_pick, (0, 0))

    while True:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    break

        pygame.display.update()
        clock.tick(60)
