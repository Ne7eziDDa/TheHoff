import pygame
from img_load import player_img, player_mini 
from snd_load import shoot_sound, shoot_sound2, shoot_sound3
from pyGame_basic import WIDTH, HEIGHT, bullets, all_sprites
from bullet import Bullet # не думаю, что понадобится после полной сборки.

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

    
    def update(self):
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.power = 1
            self.power_time = pygame.time.get_ticks()
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1500:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT + 28
        if player.attack > 0 and pygame.time.get_ticks() - self.power_time >= 10:
            #print(f'{pygame.time.get_ticks()} : {self.power_time}') # на тесты.
            player.attack -= 16.8
            #print(f'player.attack : {player.attack}') # на тесты.

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

        if self.hidden == False:
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
                    shoot_sound2.play()
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
                    shoot_sound3.play()
                

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT - 2000)

player = Player()