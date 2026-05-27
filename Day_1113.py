
import pygame as pg

pg.init()
WIDTH,HEIGHT = 600,600
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

surface = pg.Surface((300, 200))

running = True
while running:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((255,0,0))
    surface.fill((0, 0, 255))

    pg.draw.circle(surface,(0,255,0),
                   (150,100),50)

    screen.blit(surface,(100,100))

    pg.display.update()

pg.quit()