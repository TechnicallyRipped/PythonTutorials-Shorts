

import pygame as pg
pg.init()
screen = pg.display.set_mode((500, 500))

red = (255, 0, 0)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # surface, color, center, radius
    pg.draw.circle(screen, red, (250, 250), 50)

    pg.display.flip()


