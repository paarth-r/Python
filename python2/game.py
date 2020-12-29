import sys
import random
import pygame
def detect_collision(player_pos,enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]
    e_x = enemy_pos[0]
    e_y = enemy_pos[1]
    if e_x >= p_x and e_x < (p_x + player_size) or (p_x >= e_x and p_x < (e_x+enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
        return False


pygame.init()
width = 800
length = 600
player_pos = [width/2,length-2*50]
enemy_size = 50
screen = pygame.display.set_mode((800,600))
enemy_pos = [random.randint(0,750),0]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            step = 50
            x = player_pos[0]
            y = player_pos[1]
            if event.key == pygame.K_LEFT:
                x -= step
            elif event.key == pygame.K_RIGHT:
                x += step
           
            player_pos = [x,y]

                
    screen.fill((0,255,0))
    if enemy_pos[1] >= 0 and enemy_pos[1] < length:
        enemy_pos[1] += 20
    else:
        enemy_pos[0] = random.randint(0,750)
        enemy_pos[1] = 1
        
    pygame.draw.rect(screen, (255,0,0), (player_pos[0],player_pos[1],50,50))
    pygame.draw.rect(screen, (0,0,255), (enemy_pos[0], enemy_pos[1],enemy_size, enemy_size)) 
    pygame.display.update()
        
pygame.quit()   
    
