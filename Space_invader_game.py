import math
import random
import pygame

# constants
SW = 800
SH = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DIST = 27

# initialize the game
pygame.init()

#creating the screen
screen = pygame.display.set_mode((SW , SH))

# background
background = pygame.image.load('background.jpg')

# caption and icon
pygame.display.set_caption('space invader')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#player
player_img = pygame.image.load('player.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# enemy
enemy_img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for __i in range(num_of_enemies):
    enemy_img.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, SW - 64))   # 64 IS THE SIZE OF THE ENEMY
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# bullet
bullet_img = pygame.image.load('bullet.png')
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = 'ready'

# score
score_value = 0
 # font = pygame.font.Font(None,36).render('score', True, pygame.Color('black'))
textX = 10
textY = 10

# game over text
# over_font = pygame.font.Font(None, 64)

def show_score(x, y):
    # display current score on screen
    score = pygame.font.Font(None, 36).render("score: " + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))

def game_over_text():
    # display the game over text
    over_text = pygame.font.Font(None, 64).render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    # draw the player on the screen
    screen.blit(player_img, (x, y))

def enemy(x, y, i):
    #draw an enemy on the screen
    DEFAULT_SIZE = (200,200)
    enemy_img[i] = pygame.transform.scale(enemy_img, DEFAULT_SIZE)
    screen.blit(enemy_img[i], (x, y))

def fire_bullet(x, y):
    # fire a bullet from the players position
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x+16, y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    # chk if there is collision between bullet and enemy
    distance = math.sqrt((enemyX - bulletX)**2 + (enemyY - bulletY)**2)
    return distance < COLLISION_DIST

# game loop
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            playerX_change = 0

    # player movement
    playerX += playerX_change
    playerX = max(0, min(playerX, SW - 64)) # 64 is the size of the player

    # enemy movement
    for i in range(num_of_enemies):
        if enemyY[i] > 340:   # game over condition
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= SW - 64:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        # collision chk
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, SW - 64) 
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = PLAYER_START_Y
        bullet_state = "ready"

    elif bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change     
    
    player(playerX, playerY)
    show_score(textY, textY)
    pygame.display.update()