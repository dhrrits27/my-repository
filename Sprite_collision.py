import pygame
import random

SW , SH = 500 , 400
MOVE_SPEED= 5
FONT_SIZE = 72

pygame.init()

bg_image = pygame.transform.scale(pygame.image.load("background_image.jpg"),(SW, SH))

#LOAD FONT AT BEGINNING
font = pygame.font.SysFont("Times New Roman",FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])

        # bg color of sprite
        self.image.fill(pygame.Color('dodgerblue'))

        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width,height))
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x = max(
            min(self.rect.x + x_change, SW - self.rect.width), 0)
        self.rect.y = max(
            min(self.rect.y + y_change, SH - self.rect.height), 0)
        
# setup
screen = pygame.display.set_mode((SW , SH))
pygame.display.set_caption("sprite collision")
all_sprites = pygame.sprite.Group()

#create sprites
sp1= Sprite(pygame.Color('black'),20, 30)

sp1.rect.x, sp1.rect.y = random.randint(0, SW - sp1.rect.width), random.randint(0, SH - sp1.rect.height)
all_sprites.add(sp1)

sp2= Sprite(pygame.Color('red'),20, 30)

sp2.rect.x, sp2.rect.y = random.randint(0, SW - sp2.rect.width), random.randint(0, SH - sp2.rect.height)
all_sprites.add(sp2)

# game loop control variable
running, won =  True, False
clock = pygame.time.Clock()

# main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False

    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVE_SPEED
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVE_SPEED   
        sp1.move(x_change, y_change)
        
        if sp1.rect.colliderect(sp2.rect):
            all_sprites.remove(sp2)
            won = True

    # drawing
    screen.blit(bg_image, (0,0))
    all_sprites.draw(screen)

    #display win message
    if won:
        win_text = font.render("you win!", True, pygame.Color('black'))
        screen.blit(win_text, ((SW - win_text.get_width())//2, SH - win_text.get_height()) // 2)

    pygame.display.flip()
    clock.tick(90)

pygame.quit()


        