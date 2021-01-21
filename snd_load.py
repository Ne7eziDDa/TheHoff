import pygame
import os

game_folder = os.path.dirname(__file__) # система поиска папки игры для любой ОС.
snd_folder = os.path.join(game_folder, 'snd') # добавление папки snd.

def snd_load(folder, name):
    snd_loader = pygame.mixer.Sound(os.path.join(folder, name))
    return snd_loader

shoot_sound = snd_load(snd_folder, 'LaserShoot.wav') # загрузка звука выстрела.
shoot_sound2 = snd_load(snd_folder, 'DoubleShoot.wav')
shoot_sound3 = snd_load(snd_folder, 'QuadroShoot.wav')

shield_sound = snd_load(snd_folder, 'Powerup2.wav')
bolt_sound = snd_load(snd_folder, 'Powerup.wav')
dead_sound = snd_load(snd_folder, 'playerDead.ogg')
expl_sound = []
for snd in ['Expl1.wav', 'Expl2.wav']:
    expl_sound.append(snd_load(snd_folder, snd)) # загрузка списка звуков для взрыва.
                                                                         # ДОБАВИТЬ НЕСКОЛЬКО ВАРИАНТОВ ДЛЯ РАЗНЫХ ВЫСТРЕЛОВ!
pygame.mixer.music.load(os.path.join(snd_folder, 'ObservingTheStar.ogg')) # загрузка фоновой мелодии.
pygame.mixer.music.set_volume(1) # громкость 80%
