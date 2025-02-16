

import pygame

pygame.init()

screen = pygame.display.set_mode((400,400))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

























