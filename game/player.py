import pygame as game
from settings import Settings


class Player(game.sprite.Sprite):
    def __init__(self, player_img, shoot_snd, shoot_img):
        game.sprite.Sprite.__init__(self)
        self.image = game.transform.scale(player_img, (50, 30))
        self.rect = self.image.get_rect()
        self.rect.centerx = Settings.WIDTH / 2
        self.rect.bottom = Settings.HEIGHT - 40
        self.speedx = 0
        self.speedy = 5
        self.last_update = game.time.get_ticks()
        self.is_jumping = False
        self.jump_count = 10

    def update(self):
        self.speedx = 0
        keystate = game.key.get_pressed()
        if keystate[game.K_a]:
            self.speedx = -8
        if keystate[game.K_d]:
            self.speedx = 8
        if keystate[game.K_SPACE] and not self.is_jumping:
            self.jump_count = 10
            self.is_jumping = True

        # прыжок
        if self.is_jumping:
            if self.jump_count < 5:
                self.rect.y += self.speedy
            else:
                self.rect.y -= self.speedy

        self.rect.x += self.speedx
        if self.rect.right > Settings.WIDTH:
            self.rect.right = Settings.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0