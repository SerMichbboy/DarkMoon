import pygame
from game.general import are_you_sure
from settings import Settings


def game():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Dark Moon")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((Settings.width_game, Settings.height_game))

    # Start coordinate
    bg_x = 0

    # player
    # ============================================================================
    player = pygame.image.load('images/Frames/bird/pngwing.com (1) (1).png')
    character_speed, character_x, character_y = 15, 300, 600
    is_jump = False
    jump_count = 9
    playe_anim_count = 0

    # ============================================================================

    # cycle
    # ----------------------------------------------------------------------------------------------------
    while True:
        mx, my = pygame.mouse.get_pos()
        level_pick = pygame.image.load('images/99px_ru_wallpaper_349262_mrachnij_temnij_les.jpg')
        screen.blit(level_pick, (bg_x, -1150))
        screen.blit(level_pick, (bg_x + 3840, -1150))
        screen.blit(player, (character_x, character_y))

        # Moving
        # =========================================================

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and character_x > 20:
            if bg_x < 0:
                if bg_x > 1000:
                    character_x -= character_speed
                bg_x += character_speed
            character_x -= character_speed
        if keys[pygame.K_d] and bg_x > -800:
            if character_x < 250:
                character_x += character_speed
            bg_x -= character_speed
        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -9:
                if jump_count > 0:
                    character_y -= (jump_count ** 2) / 2
                else:
                    character_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 9

        # ==========================================================

        if bg_x <= -3840:
            bg_x = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if are_you_sure(screen, clock, True):
                        return True

        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)

# -----------------------------------------------------------------------------------------------------
