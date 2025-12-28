import pygame as pg

pg.init()
screen_width = 1000
screen_height = 1000
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Sharknado")
clock = pg.time.Clock()
FPS = 60

shark_hitbox = pg.Rect(400,400,50,50)
shark_speed = 5
hitboxes = []
hitboxes.append(pg.Rect(100,100,50,50))

running = True
while running:
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

    screen.fill((30, 30, 30))
    pg.draw.rect(screen,(200,200,200),shark_hitbox)
    for hitbox in hitboxes:
        pg.draw.rect(screen, (255,0,0), hitbox)
    pg.display.flip()
    clock.tick(FPS)


pg.quit()
