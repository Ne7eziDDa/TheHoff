import pygame
import random
from img_load import powerup_images

class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield', 'shield', 'shield','shield3','bolt', 'bolt', 'bolt', 'bolt3'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()