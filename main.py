from pygame import *
from random import randint

win_height, win_width = 700,500

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,player_speed): 
        super().__init__()
        self.image=transform.scale(image.load(player_image), (65,65))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 495:
            self.rect.y += self.speed
    def update2(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 495:
            self.rect.y += self.speed


class Bullet(GameSprite):
    def update(self):
        self.rect.y-=self.speed
        if self.rect.y < 0:
            self.kill()




ship1 = Player('rocket.png', 600, 400, 10)
ship2 = Player('rocket.png', 50, 400, 10)

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound=mixer.Sound('fire.ogg')

font.init()
font1=font.Font(None,36)

img_back='galaxy.jpg'
img_hero='rocket.png'

win_width=700
win_height=500
display.set_caption('Shooter')
window=display.set_mode((win_width,win_height))
background=transform.scale(image.load(img_back),(win_width,win_height))
finish=False
run=True

while run:
    for e in event.get():
        if e.type==QUIT:
            run=False

    if not finish:
        window.blit(background,(0,0))
        ship1.reset()
        ship1.update1()
        ship2.reset()
        ship2.update2()
        display.update()
    
    time.delay(60)
