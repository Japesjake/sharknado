import pygame as pg
def draw_hitboxes(hitboxes):
    for hitbox in hitboxes:
        pg.draw.rect(screen, (255,0,0), hitbox)