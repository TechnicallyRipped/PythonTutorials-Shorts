
import pygame

pygame.init()

screen = pygame.display.set_mode((400,400))

player = pygame.image.load('player.png')
player_x = 50
player_y = 50

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= 15
            if event.key == pygame.K_RIGHT:
                player_x += 15
            if event.key == pygame.K_UP:
                player_y -= 15
            if event.key == pygame.K_DOWN:
                player_y += 15
    screen.fill((15,15,15))
    screen.blit(player,(player_x,player_y))
    pygame.display.update()



























