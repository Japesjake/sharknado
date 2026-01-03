import pygame as pg
import random as rand
pg.init()
screen_width = 1000
screen_height = 1000
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Sharknado")
clock = pg.time.Clock()
FPS = 60

shark_hitbox = pg.Rect(400,400,50,50)
shark_speed = 10
tornadoes = []
people = []
spawn_rate = 1
t = 0

def draw_hitboxes(hitboxes):
    for hitbox in hitboxes:
        pg.draw.rect(screen, (255,0,0), hitbox)

def detect_collision(hitboxes,hitbox):
    i = hitbox.collidelist(hitboxes)
    if i != -1: hitboxes.pop(i)


running = True
while running:


    screen.fill((30, 30, 30))
    pg.draw.rect(screen,(200,200,200),shark_hitbox)

    detect_collision(tornadoes,shark_hitbox)
    detect_collision(people,shark_hitbox)
    draw_hitboxes(tornadoes)
    draw_hitboxes(people)
    
    
    t += spawn_rate
    if t > 100: 
        tornadoes.append(pg.Rect(rand.randint(1,1000),rand.randint(1,1000),50,50))
        people.append(pg.Rect(rand.randint(1,1000),0,50,50))

        t = 0
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        shark_hitbox.x -= shark_speed
    if keys[pg.K_RIGHT]:
        shark_hitbox.x += shark_speed
    if keys[pg.K_UP]:
        shark_hitbox.y -= shark_speed
    if keys[pg.K_DOWN]:
        shark_hitbox.y += shark_speed
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False    
    pg.display.flip()
    clock.tick(FPS)

pg.quit()