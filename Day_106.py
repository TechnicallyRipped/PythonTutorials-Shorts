

import pygame

pygame.init()

screen = pygame.display.set_mode((400,400))
player = pygame.image.load('player.png')

running = True
while running:
    screen.blit(player,(50,50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screenshot = pygame.Surface((400,400))
                screenshot.blit(screen, (0, 0))
                pygame.image.save(screenshot, "pygame_screenshot.png")
                print('You took a screenshot')
    pygame.display.flip()

























