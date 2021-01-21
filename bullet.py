import pygame
from img_load import bullet_images
from player import Player

player = Player()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.speedx = 0
        self.speedy = 0
        if player.power == 1:
            self.image = bullet_images['blue']
            player.shoot_delay = 350
            self.speedy = -20
        elif player.power == 2:
            self.image = bullet_images['yellow']
            player.shoot_delay = 250 # нужен баланс скорость / кол-во выстрелов / урон?
            self.speedy = -28
        elif player.power == 3:
            self.image = bullet_images['pink']
            player.shoot_delay = 425
            self.speedy = -15
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom < 0:
            self.kill()