import pygame
pygame.init()

screen = pygame.display.set_mode((640,480))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen,(255,0,0), (320,150,50,50))
    pygame.display.update()

pygame.quit()
