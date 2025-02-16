

import pygame as pg
pg.init()
screen = pg.display.set_mode((500, 500))

# Define a rectangle (x, y, width, height)
x = pg.Rect(50, 50, 300, 200)
color = (255,0,0) #RGB 

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Surface, color(tuple), rect
    pg.draw.rect(screen,color,x)      

    pg.display.flip()


