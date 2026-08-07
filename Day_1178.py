
import pygame as pg

pg.init()
screen = pg.display.set_mode((200,200))
clock = pg.time.Clock()

radius = 20
min_r,max_r = 20,80
growing = True

running = True
while running:
    screen.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    if growing:
        radius += 1
        if radius >= max_r:
            growing = False
    else:
        radius -= 1
        if radius <= min_r:
            growing = True

    pg.draw.circle(screen,(0,200,255),
                   (100,100),radius)
    pg.display.flip()
    clock.tick(60)
pg.quit()