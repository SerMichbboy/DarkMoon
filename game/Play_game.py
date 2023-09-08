import pygame
from game.general import are_you_sure
from settings import Settings


def game():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Dark Moon")

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((Settings.width_game, Settings.height_game), pygame.FULLSCREEN)
    # Start coordinate
    bg_x = 0

    # Sounds
    pygame.mixer.music.load('sounds/music/kevin-macleod-ghost-story.ogg')
    pygame.mixer.music.play()

    # player
    # ============================================================================

    player_go_right = [pygame.image.load(f'images/Frames/main_chr/run1.png'),
                       pygame.image.load(f'images/Frames/main_chr/run2.png'),
                       pygame.image.load(f'images/Frames/main_chr/run3.png'),
                       pygame.image.load(f'images/Frames/main_chr/run4.png'),
                       pygame.image.load(f'images/Frames/main_chr/run5.png'),
                       pygame.image.load(f'images/Frames/main_chr/run6.png')
                       ]

    player_go_left = [pygame.image.load(f'images/Frames/main_chr_left/run1left.png'),
                      pygame.image.load(f'images/Frames/main_chr_left/run2left.png'),
                      pygame.image.load(f'images/Frames/main_chr_left/run3left.png'),
                      pygame.image.load(f'images/Frames/main_chr_left/run4left.png'),
                      pygame.image.load(f'images/Frames/main_chr_left/run5left.png'),
                      pygame.image.load(f'images/Frames/main_chr_left/run6left.png')
                      ]

    player_jump_right = [pygame.image.load('images/Frames/main_chr_jump/jump1.png'),
                         pygame.image.load('images/Frames/main_chr_jump/jump2.png')]

    player_jump_left = [pygame.image.load('images/Frames/main_chr_jump_left/jump1left.png'),
                        pygame.image.load('images/Frames/main_chr_jump_left/jump2left.png')]

    character_speed, character_x, character_y = 15, 300, 600
    is_jump = False
    jump_count = 9
    player_anim_count = 0

    # ============================================================================

    # cycle
    # ----------------------------------------------------------------------------------------------------
    while True:
        mx, my = pygame.mouse.get_pos()
        level_pick = pygame.image.load('images/99px_ru_wallpaper_349262_mrachnij_temnij_les.jpg')
        screen.blit(level_pick, (bg_x, -1050))
        screen.blit(level_pick, (bg_x + 3840, -1050))
        keys = pygame.key.get_pressed()

        def player(arg):
            return screen.blit(arg[player_anim_count], (character_x, character_y))

        # Moving
        # =========================================================

        # Go left
        if keys[pygame.K_a] and bg_x < -20:
            if jump_count == 9:
                player(player_go_left)
            if player_anim_count >= 5:
                player_anim_count = 0
            if bg_x >= 20:
                character_speed = 0
            player_anim_count += 1
            bg_x += character_speed

        # Go right
        elif keys[pygame.K_d]:
            if jump_count == 9:
                player(player_go_right)
            if is_jump != 9:
                player_anim_count += 1
                bg_x -= character_speed
            if player_anim_count >= 5:
                player_anim_count = 0

        elif not keys[pygame.K_SPACE]:
            screen.blit(player_go_right[1], (character_x, character_y))

        # Jumping

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        elif is_jump:
            if jump_count >= -9:
                if jump_count > 0:
                    if keys[pygame.K_a]:
                        screen.blit(player_jump_left[0], (character_x, character_y))
                    elif keys[pygame.K_d]:
                        screen.blit(player_jump_right[0], (character_x, character_y))
                    character_y -= (jump_count ** 2) / 2
                else:
                    if keys[pygame.K_a]:
                        screen.blit(player_jump_left[1], (character_x, character_y))
                    elif keys[pygame.K_d]:
                        screen.blit(player_jump_right[1], (character_x, character_y))
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
        clock.tick(30)

# -----------------------------------------------------------------------------------------------------
