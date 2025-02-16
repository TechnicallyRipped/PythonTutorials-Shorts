
import pygame as pg
pg.init()
width, height = 320, 256

tile_size = 64
tile_0,tile_1 = pg.image.load('tile_0.png'),pg.image.load('tile_1.png')

tilemap = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0]]

screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    for row_index, row in enumerate(tilemap):
        for col_index, tile in enumerate(row):
            x = col_index * tile_size
            y = row_index * tile_size
            if tile == 0:
                screen.blit(tile_0, (x, y))
            elif tile == 1:
                screen.blit(tile_1, (x, y))

    pg.display.flip()
    clock.tick(60)































