import pygame
import pyGame_basic
from mob import Mob
from pyGame_basic import mobs, white, green, orange, WIDTH, HEIGHT, screen, score, background, background_rect, clock, FPS, all_sprites

font_name = pygame.font.match_font('Verdana')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    bar_length = 150
    bar_height = 12
    fill = (pct / 100) * bar_length
    outline_rect = pygame.Rect(x, y, bar_length, bar_height)
    fill_rect = pygame.Rect(x, y, fill, bar_height)
    pygame.draw.rect(surf, green, fill_rect)
    pygame.draw.rect(surf, white, outline_rect, 2)

def draw_bonus_attack(surf, x , y, pct):
    if pct <0:
        pct = 0
    bar_length = 150
    bar_height = 12
    fill = (pct / 6500) * bar_length
    outline_rect = pygame.Rect(x, y, bar_length, bar_height)
    fill_rect = pygame.Rect(x, y, fill, bar_height)
    pygame.draw.rect(surf, orange, fill_rect)
    pygame.draw.rect(surf, white, outline_rect, 2)

def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x - 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)

def show_go_screen():
    screen.blit(background, background_rect)
    draw_text(screen, 'The Roff.', 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, f'Your score: {score}!', 22, WIDTH / 2, HEIGHT / 2)
    draw_text(screen, 'PRESS ANY KEY TO RESTART.', 18, WIDTH / 2, HEIGHT / 2 + 100)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP: # ДОБАВИТЬ ВЫХОД ПО ESC!
                waiting = False