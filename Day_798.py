
import pygame as pg

pg.init()
width,height = 400,600
screen = pg.display.set_mode((width,height))
clock = pg.time.Clock()
x, y = 100, 100
box_size = 50
dx,dy = 5,5
running = True
while running:
    screen.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    x += dx
    y += dy
    if x <= 0 or x + box_size >= width:
        dx *= -1
    if y <= 0 or y + box_size >= height:
        dy *= -1
    pg.draw.rect(screen, (255,0,0), 
                 (x, y, box_size, box_size))
    pg.display.update()
    clock.tick(60)
pg.quit()
