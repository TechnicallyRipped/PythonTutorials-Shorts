

import pygame

pygame.init()

screen = pygame.display.set_mode((400,400))

player = pygame.image.load('player.png')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(player,(100,100))
    pygame.display.update()

























