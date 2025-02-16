

import pygame as pg

pg.init()

screen = pg.display.set_mode((800, 600), pg.RESIZABLE)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        # Handle window resize
        if event.type == pg.VIDEORESIZE:
            screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)

    pg.draw.circle(screen, (255,0,0), (250, 250), 50)

    pg.display.flip()

