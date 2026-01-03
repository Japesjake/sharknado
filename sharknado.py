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
SPAWN_TORNADO_EVENT = pg.USEREVENT + 2
pg.time.set_timer(SPAWN_PERSON_EVENT, 1000)
pg.time.set_timer(SPAWN_TORNADO_EVENT, 1000)

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
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pg.K_UP]:
            self.rect.y -= self.speed
        if keys[pg.K_DOWN]:
            self.rect.y += self.speed

class Person(Hitbox):
    def __init__(self,width,height,color,x,y,speed):
        super().__init__(width,height,color,x,y,speed)
    def update(self):
        self.rect.y += self.speed

class Tornado(Hitbox):
    def __init__(self,width,height,color,x,y,speed):
        super().__init__(width,height,color,x,y,speed)

class Bullet(Hitbox):
    def __init__(self,width,height,color,x,y,speed):
        super().__init__(width,height,color,x,y,speed)
    def update(self):
        self.rect.y -= self.speed

sharks = pg.sprite.Group()
people = pg.sprite.Group()
tornadoes = pg.sprite.Group()
bullets = pg.sprite.Group()
shark_hitbox = Shark(50,50,(255,0,0),400,400,10)
sharks.add(shark_hitbox)

running = True
while running:
    pg.sprite.groupcollide(sharks, tornadoes, False, True)
    pg.sprite.groupcollide(bullets,people,False, True)
    sharks.update()
    people.update()
    tornadoes.update()
    bullets.update()
    screen.fill((0,0,0))
    sharks.draw(screen)
    people.draw(screen)
    tornadoes.draw(screen)
    bullets.draw(screen)
    

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == SPAWN_PERSON_EVENT:
            people.add(Person(50,50,(0,255,0),rand.randint(0,screen_width-100),0,1))
        elif event.type == SPAWN_TORNADO_EVENT:
            tornadoes.add(Tornado(50,50,(0,0,255),rand.randint(0,screen_width-100),rand.randint(0,screen_height),1))
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                bullets.add(Bullet(10,30,(255,255,255),shark_hitbox.rect.x,shark_hitbox.rect.y,1))
                           
    pg.display.flip()
    clock.tick(FPS)

pg.quit()