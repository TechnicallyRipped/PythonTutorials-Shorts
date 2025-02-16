


import pygame

pygame.init()

screen = pygame.display.set_mode((400,400))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("You pressed space")
    pygame.display.update()



























