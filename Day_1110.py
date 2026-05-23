
import pygame as pg
import random

pg.init()

WIDTH = 500
HEIGHT = 700

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

class Raindrop:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.speed = random.randint(4, 10)
        self.length = random.randint(10, 20)

    def update(self):
        self.y += self.speed

        if self.y > HEIGHT:
            self.x = random.randint(0, WIDTH)
            self.y = random.randint(-100, -10)

    def draw(self, surface):
        pg.draw.line(surface,
                     (0,0,255),
                     (self.x, self.y),
                     (self.x, self.y + self.length),
                     5)

raindrops = []
for _ in range(150):
    raindrops.append(Raindrop())


running = True
while running:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill((0, 0, 0))

    for drop in raindrops:
        drop.update()
        drop.draw(screen)

    pg.display.update()