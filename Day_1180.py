

import pygame as pg

pg.init()
screen = pg.display.set_mode((300, 300))

running = True
while running:
    screen.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.display.flip()
    timer = pg.time.get_ticks()
    print(timer)
pg.quit()
