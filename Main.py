# init
import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))

#title & logo
icon = pygame.image.load("Logo.jpeg")
pygame.display.set_caption("space invaders")
pygame.display.set_icon(icon)
# bullet
bullet_img = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 480
bullet_state = "ready"
by_change = 10
bstate = "ready"
# player_boi
player_img = pygame.image.load("player.png")
player_x = 370
player_y = 480
px_change = 0
score = 0

# bad_boi
enemy_img = pygame.image.load("space-invaders.png")
enemy_x = random.randint(0, 736)
enemy_y = 0
ey_change = 40
ex_change = 4


# display player
def player(x, y):
    screen.blit(player_img, (x, y))

# display enemy
def enemy(x, y):
    screen.blit(enemy_img, (x, y))
#fire bullet
def fire_bullet(x, y):
    global bullet_state  
    bullet_state = "fired"
    screen.blit(bullet_img, (x, y - 50))
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance =  math.sqrt(((enemy_x - bullet_x)**2) + ((enemy_y - bullet_y)**2))
    return distance <= 25

running = True
while running == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                px_change -= 5
            if event.key == pygame.K_RIGHT:
                px_change += 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_x = player_x
                fire_bullet(bullet_x, bullet_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                px_change = 0

    screen.fill((1, 3, 128))

    player_x += px_change
    enemy_x += ex_change
    if bullet_y <=0:
        bullet_y = 480
        bullet_state = "ready"
    if enemy_x >= 736:
        enemy_x = 736
        ex_change = -4
        enemy_y += ey_change
    if enemy_x <= 0:
        enemy_x = 0
        ex_change = 4
        enemy_y += ey_change

    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    if bullet_state is "fired":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= by_change

    collision = is_collision(enemy_x, enemy_y, bullet_x, bullet_y)
    if collision:
        bullet_y = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemy_x = random.randint(0,800)
        enemy_y = 0
    ex_change += 10
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    pygame.display.update()
