

import pygame as pg

pg.init()

screen_width = 200
screen_height = 200
screen = pg.display.set_mode((screen_width, screen_height))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                screen_width += 25
                screen_height += 25
                screen = pg.display.set_mode((screen_width, screen_height))
    pg.display.flip()
pg.quit()






























