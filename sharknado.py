import pygame as pg
import random as rand
pg.init()
screen_width = 1000
screen_height = 1000
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Sharknado")
clock = pg.time.Clock()
FPS = 60
SPAWN_PERSON_EVENT = pg.USEREVENT + 1
pg.time.set_timer(SPAWN_PERSON_EVENT, 10000)

shark_hitbox = pg.Rect(400,400,50,50)

class Hitbox(pg.sprite.Sprite):
    def __init__(self,width,height,color,x,y,speed):
        super().__init__()
        self.image = pg.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

class Shark(Hitbox):
    def __init__(self,width,height,color,x,y,speed):
        super().__init__(width,height,color,x,y,speed)
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            shark_hitbox.rect.x -= self.speed
        if keys[pg.K_RIGHT]:
            shark_hitbox.rect.x += self.speed
        if keys[pg.K_UP]:
            shark_hitbox.rect.y -= self.speed
        if keys[pg.K_DOWN]:
            shark_hitbox.rect.y += self.speed

class Person(Hitbox):
    def __init__(self,width,height,color,x,y,speed):
        super().__init__(width,height,color,x,y,speed)
    def update(self):
        self.rect.y += 1

shark = pg.sprite.Group()
shark_hitbox = Shark(50,50,(255,0,0),400,400,10)
shark.add(shark_hitbox)

running = True
while running:
    shark.update()
    screen.fill((0,0,0))
    shark.draw(screen)
    

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False    
    pg.display.flip()
    clock.tick(FPS)

pg.quit()