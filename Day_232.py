




import pygame as pg

pg.init()

width, height = 180, 160
screen = pg.display.set_mode((width, height))

while True:
    screen.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN:
            print("Player pressed key")
        if event.type == pg.KEYUP:
            print("Player released key")
    pg.display.flip()






















