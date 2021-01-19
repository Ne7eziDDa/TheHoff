import pygame
import random
import os

WIDTH = 1376
HEIGHT = 710
FPS = 60
POWERUP_TIME = 6500 # общеевремя действия бонусов.

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
orange = (255, 140, 0)


pygame.init() # инициализация игры.
pygame.mixer.init() # инициализация звука. 
screen = pygame.display.set_mode(( WIDTH, HEIGHT ))#, pygame.FULLSCREEN) # окно программы.
pygame.display.set_caption('The Roff.')
clock = pygame.time.Clock()

game_folder = os.path.dirname(__file__) # система поиска папки игры для любой ОС.
img_folder = os.path.join(game_folder, 'img') # добавление папки img.
snd_folder = os.path.join(game_folder, 'snd') # добавление папки snd.
player_img = pygame.image.load(os.path.join(img_folder, 'ship1.png'))#.convert() # при конвертирования добавляет битые пиксели. 
player_mini = pygame.image.load(os.path.join(img_folder, 'ship1Tiny.png'))
meteor_images = []
meteor_list = ['meteorBrown_big1.png','meteorBrown_med1.png',
               'meteorBrown_med1.png','meteorBrown_med3.png',
               'meteorBrown_small1.png','meteorBrown_small2.png',
               'meteorBrown_tiny1.png']
for img in meteor_list:
    meteor_images.append(pygame.image.load(os.path.join(img_folder, img)))

bullet_images = {}
bullet_images['blue'] = pygame.image.load(os.path.join(img_folder, 'bullet_blue.png'))
bullet_images['pink'] = pygame.image.load(os.path.join(img_folder, 'bullet_pink.png'))
bullet_images['yellow'] = pygame.image.load(os.path.join(img_folder, 'bullet_yellow.png'))

#bullet_img = pygame.image.load(os.path.join(img_folder, 'bullet_blue.png'))
background = pygame.image.load(os.path.join(img_folder, 'backBig.png'))
background_rect = background.get_rect()

powerup_images = {}
powerup_images['shield'] = pygame.image.load(os.path.join(img_folder, 'shield.png'))
powerup_images['shield3'] = pygame.image.load(os.path.join(img_folder, 'shield3.png'))
powerup_images['bolt'] = pygame.image.load(os.path.join(img_folder, 'bolt.png')) # bolt2 и shield2 - серебро, брак картинки.
powerup_images['bolt3'] = pygame.image.load(os.path.join(img_folder, 'bolt3.png'))


explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['player'] = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(os.path.join(img_folder, filename)).convert()
    img.set_colorkey(black)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)
    filename = 'sonicExplosion0{}.png'.format(i)
    img = pygame.image.load(os.path.join(img_folder, filename)).convert()
    img.set_colorkey(black)
    explosion_anim['player'].append(img)

# загрузка звуков.
shoot_sound = pygame.mixer.Sound(os.path.join(snd_folder, 'LaserShoot.wav')) # загрузка звука выстрела.
shield_sound = pygame.mixer.Sound(os.path.join(snd_folder, 'Powerup2.wav'))
bolt_sound = pygame.mixer.Sound(os.path.join(snd_folder, 'Powerup.wav'))
dead_sound = pygame.mixer.Sound(os.path.join(snd_folder, 'playerDead.ogg'))
expl_sound = []
for snd in ['Expl1.wav', 'Expl2.wav']:
    expl_sound.append(pygame.mixer.Sound(os.path.join(snd_folder, snd))) # загрузка списка звуков для взрыва.
                                                                         # ДОБАВИТЬ НЕСКОЛЬКО ВАРИАНТОВ ДЛЯ РАЗНЫХ ВЫСТРЕЛОВ!
pygame.mixer.music.load(os.path.join(snd_folder, 'ObservingTheStar.ogg')) # загрузка фоновой мелодии.
pygame.mixer.music.set_volume(1) # громкость 80%


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
            if event.type == pygame.KEYUP:
                waiting = False

class Player(pygame.sprite.Sprite): 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # инициализатор встроенных классов Sprite.
        self.image = player_img # image спрайта.
        self.rect = self.image.get_rect() # оценивает image и высчитывает прямоугольник, способный его окружить.
        self.radius = 39 # радиус круга, замещающего .rect
        #pygame.draw.circle(self.image, red, self.rect.center, self.radius) # отрисовка круга для наглядности.
        self.rect.centerx =  WIDTH / 2
        self.rect.bottom = HEIGHT + 18
        self.speedx = 0
        self.speedy = 0
        self.shield = 100
        self.attack = 0
        self.shoot_delay = 350
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3 # ОТРИСОВКУ ЖИЗНЕЙ НУЖНО ПОМЕНЯТЬ В ДРУГУ СТОРОНУ ДЛЯ УВЕЛИЧЕНИЯ КОЛ-ВА ДОСТУПНЫХ ОНЫХ. # СДЕЛАНО!
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_time = pygame.time.get_ticks()

    
    def update(self):
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.power = 1
            self.attack = 0
            self.power_time = pygame.time.get_ticks()
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1200:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT + 28

        self.speedx = 0
        self.speedy = 0

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -5
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_d]:
            self.speedx = 5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5

        # ниже движение вверх-вниз    
        if keystate[pygame.K_w]:
            self.speedy = -6
        if keystate[pygame.K_UP]:
            self.speedy = -6
        if keystate[pygame.K_s]:
            self.speedy = 4
        if keystate[pygame.K_DOWN]:
            self.speedy = 4
        if keystate[pygame.K_SPACE]:
            self.shoot()

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.left > WIDTH:
            self.rect.left = 0
        if self.rect.right < 0:
            self.rect.right = WIDTH
        if self.rect.bottom > HEIGHT - 28:
            self.rect.bottom = HEIGHT - 28

    def powerup(self):
        self.power_time = pygame.time.get_ticks()
   
    def shoot(self):
        now = pygame.time.get_ticks()

        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power == 1:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()
            if self.power == 2:
                bullet1 = Bullet(self.rect.left + 85, self.rect.top)
                bullet2 = Bullet(self.rect.right - 85, self.rect.top)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shoot_sound.play()
            if self.power == 3:
                bullet_sprite = []
                bullet1 = Bullet(self.rect.left + 15, self.rect.top)
                bullet2 = Bullet(self.rect.right - 15, self.rect.top)
                bullet3 = Bullet(self.rect.left + 62, self.rect.top)
                bullet4 = Bullet(self.rect.right - 62, self.rect.top)
                bullet_sprite.append(bullet1)
                bullet_sprite.append(bullet2)
                bullet_sprite.append(bullet3)
                bullet_sprite.append(bullet4)
                all_sprites.add(bullet_sprite)
                bullets.add(bullet_sprite)
                shoot_sound.play()
                

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT - 2000)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(meteor_images)
        #self.image_orig.set_colorkey(white)
        self.image = self.image_orig.copy()
        self.rect = self.image_orig.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 16)
        self.speedx = random.randrange(-3, 3)
        self.rot = 0 # вращение спрайта.
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx
         
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 16)

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center 

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


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

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

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
powerups = pygame.sprite.Group() # группировка спрайтов.

player = Player()

score = 0 # переменная счёта. 
all_sprites.add(player) # добавление player в папку.
for i in range (10): # вот что надо крутить при увеличении уровня.
    newmob()
    
pygame.mixer.music.play(loops=-1) # включение фоновой музыки. loops - кол-во повторений, где -1 - бесконечное повторение.

game_over = False
running = True
while running:
    if game_over: # тело процесса.
        show_go_screen()
        game_over = False
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        powerups = pygame.sprite.Group() # группировка спрайтов.

        player = Player()
        all_sprites.add(player) # добавление player в папку.
        pygame.mixer.music.play(loops=-1) # включение фоновой музыки. loops - кол-во повторений, где -1 - бесконечное повторение.


    clock.tick(FPS) # держим цикл на нужной скорости.
    # Ввод процесса, события.
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # создание события QUIT. Выход.
            running = False 
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_ESCAPE]:
            running = False 


    # Обновление.
    all_sprites.update()
    
    # проверка столкновения.
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        score += 42 - hit.radius # вычисление счёта с учётом размеров астероидов.
        random.choice(expl_sound).play()
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        if random.random() > 0.91:
            pow = Pow(hit.rect.center)
            all_sprites.add(pow)
            powerups.add(pow)
        newmob()
        
    hits = pygame.sprite.spritecollide(player, powerups, True)
    for hit in hits:
        if hit.type == 'shield':
            shield_sound.play()
            player.shield += random.randrange(5, 10)
            if player.shield >= 100:
                player.shield = 100
        if hit.type == 'shield2':
            shield_sound.play()
            player.shield += random.randrange(15, 25)
            if player.shield >= 100:
                player.shield = 100
        if hit.type == 'shield3':
            shield_sound.play()
            player.shield += random.randrange(30, 50)
            if player.shield >= 100:
                player.shield = 100
        if hit.type == 'bolt':
            bolt_sound.play()
            player.power = 2
            player.powerup()
            player.attack = 6500
        if hit.type == 'bolt3':
            bolt_sound.play()
            player.power = 3
            player.powerup()
            player.attack = 6500
    

    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    for hit in hits:
        player.shield -= hit.radius
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        newmob()
        if player.shield <= 0:
            death_explosion = Explosion(player.rect.center, 'player')
            dead_sound.play()
            all_sprites.add(death_explosion)
            player.hide()
            player.lives -= 1
            player.shield = 100

    if player.lives == 0 and not death_explosion.alive():
        game_over = True # заканчивает игру, если игрок умер.

    # Рендеринг. 
    screen.fill(black) # заполнение экрана цветом.
    screen.blit(background, background_rect)

    all_sprites.draw(screen)

    draw_text(screen, str(score), 18, WIDTH / 2, 10)
    #draw_text(screen, str(FPS), 18, WIDTH / 2 + 50, 10) #FPS
    draw_shield_bar(screen, 10, 10, player.shield)
    if player.attack >= 6500:
        draw_bonus_attack(screen, 10, 25, player.attack)
    draw_lives(screen, WIDTH - 35, 10, player.lives, player_mini)

    # Переворот экрана после отрисовки.
    pygame.display.flip()


pygame.quit()