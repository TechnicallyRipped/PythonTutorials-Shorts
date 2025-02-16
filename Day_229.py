




import pygame as pg

pg.init()
pg.mixer.init()

sfx = pg.mixer.Sound('test.ogg')

screen = pg.display.set_mode((200, 200))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                sfx.play()
    pg.display.flip()































