

import pygame as pg

pg.init()
pg.mixer.init()

pg.mixer.music.load('test.ogg')
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(.1)

screen = pg.display.set_mode((200, 200))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    pg.display.flip()




