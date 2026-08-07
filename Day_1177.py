

import pygame as pg

pg.init()

WIDTH, HEIGHT = 300, 400
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

x,y,size = 150, 100, 50
gravity = 5

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    y += gravity

    if y >= HEIGHT:
        y = 0

    screen.fill((255, 255, 255))
    pg.draw.rect(screen, (0, 200, 255), (x, y, size, size))

    pg.display.flip()
    clock.tick(60)

pg.quit()