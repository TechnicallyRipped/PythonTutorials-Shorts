
import pygame as pg

pg.init()
width, height = 700, 500
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()

p1_sprite = pg.image.load('player.png')
p1_x, p1_y = width / 2, height / 2
p1_speed = 5

while True:
    screen.fill((255, 255, 255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        p1_x -= p1_speed
    if keys[pg.K_RIGHT]:
        p1_x += p1_speed

    screen.blit(p1_sprite, (p1_x,p1_y))
    pg.display.flip()
    clock.tick(30)





























