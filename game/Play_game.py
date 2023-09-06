import pygame
from game.general import are_you_sure
from settings import Settings


def game():

    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Dark Moon")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((Settings.width, Settings.height))

    while True:
        level_pick = pygame.image.load('images/stoneheart_1.jpg')
        screen.blit(level_pick, (0, 0))
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    are_you_sure(screen, clock)

        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)
