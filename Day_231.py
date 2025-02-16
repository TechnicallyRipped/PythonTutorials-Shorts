




import pygame as pg

pg.init()

width, height = 800, 600
screen = pg.display.set_mode((width, height))

cursor_image = pg.image.load('cursor.png')
pg.mouse.set_visible(False)

while True:
    screen.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    cursor_xy = pg.mouse.get_pos()
    screen.blit(cursor_image,cursor_xy)
    pg.display.flip()




















