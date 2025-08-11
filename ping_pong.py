#Создай собственный Шутер!
from pygame import *
from random import *
from time import time as tm

#создай окно игры
window = display.set_mode((700,500))
display.set_caption('Пинг-понг')
#задай фон сцены
background = transform.scale(image.load('fon.png'),(700,500))
#создай 2 спрайта и размести их на сцене
clock = time.Clock()
#обработай событие «клик по кнопке "Закрыть окно"»
game = True

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,w,h):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):  #нужен для отрисовки экземляра на экране
        window.blit(self.image,(self.rect.x,self.rect.y))



class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
    
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

player_r = Player('r.png',0,10,5,70,100)
player_l = Player('r.png',630,10,5,70,100)
ball = GameSprite('b.png',400,200,3,50,50)


finish = False
font.init()
font1 = font.SysFont('Arial',70)
win = font1.render('YOU WIN!',True,(157, 237, 165))
lose = font1.render('YOU LOSE!!!',True,(255, 3, 3))


while game:

    for e in event.get(): #возвращает список действий пользовотеля 
        if e.type == QUIT:
            game = False
        
    if finish != True:
        window.blit(background,(0,0))
        player_l.update_l()
        player_r.update_r()
        player_l.reset()
        player_r.reset()
        ball.reset()
    display.update()
    clock.tick(60)