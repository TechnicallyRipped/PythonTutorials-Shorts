

import pygame

pygame.init()

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

pygame.display.set_caption("Technically Ripped")

screen = pygame.display.set_mode((400,400))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

























