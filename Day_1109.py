

import pygame as pg
import random

pg.init()

WIDTH = 500
HEIGHT = 700

screen = pg.display.set_mode((WIDTH,HEIGHT))
clock = pg.time.Clock()

raindrops = []
for _ in range(150):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    speed = random.randint(4, 10)
    length = random.randint(10, 20)
    raindrops.append([x, y, speed, length])

running = True
while running:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill((0,0,0))

    for drop in raindrops:
        x, y, speed, length = drop
        pg.draw.line(screen,
                     (0, 0, 255),
                     (x, y),
                     (x, y + length),
                     2)

        drop[1] += speed

        if drop[1] > HEIGHT:
            drop[0] = random.randint(0, WIDTH)
            drop[1] = random.randint(-100, -10)

    pg.display.update()

pg.quit()