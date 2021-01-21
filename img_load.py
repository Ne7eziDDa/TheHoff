import pygame
import os

game_folder = os.path.dirname(__file__) # система поиска папки игры для любой ОС.
img_folder = os.path.join(game_folder, 'img') # добавление папки img.

def img_load(folder, name):
    img_loader = pygame.image.load(os.path.join(folder, name))
    return img_loader

game_icon = img_load(img_folder, 'icon.png')

player_img = img_load(img_folder, 'ship1.png')
player_mini = img_load(img_folder, 'ship1Tiny.png')
meteor_images = []
meteor_list = ['meteorBrown_big1.png','meteorBrown_med1.png',
               'meteorBrown_med1.png','meteorBrown_med3.png',
               'meteorBrown_small1.png','meteorBrown_small2.png',
               'meteorBrown_tiny1.png']
for img in meteor_list:
    meteor_images.append(img_load(img_folder, img))

bullet_images = {}
bullet_images['blue'] = img_load(img_folder, 'bullet_blue.png')
bullet_images['pink'] = img_load(img_folder, 'bullet_pink.png')
bullet_images['yellow'] = img_load(img_folder, 'bullet_yellow.png')

background = img_load(img_folder, 'backBig.png')
background_rect = background.get_rect()

powerup_images = {}
powerup_images['shield'] = img_load(img_folder, 'shield.png')
powerup_images['shield3'] = img_load(img_folder, 'shield3.png')
powerup_images['bolt'] = img_load(img_folder, 'bolt.png') # bolt2 и shield2 - серебро, брак картинки.
powerup_images['bolt3'] = img_load(img_folder, 'bolt3.png')


explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['player'] = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = img_load(img_folder, filename).convert()
    img.set_colorkey(black)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)
    filename = 'sonicExplosion0{}.png'.format(i)
    img = img_load(img_folder, filename).convert()
    img.set_colorkey(black)
    explosion_anim['player'].append(img)