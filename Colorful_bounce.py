import pygame
import random

pygame.init()

SPRITE_COLOR_CHANGE = pygame.USEREVENT + 1
BG_COLOR_CHANGE = pygame.USEREVENT + 2

#background color
BLUE=pygame.Color('blue')
LIGHTBLUE=pygame.Color('light blue')
DARKBLUE=pygame.Color('dark blue')

#sprite colors
YELLOW=pygame.Color('yellow')
MAGENTA=pygame.Color('magenta')
ORANGE=pygame.Color('orange')
WHITE=pygame.Color('white')

#sprite class representing the moving object
class Sprite(pygame.sprite.Sprite):

    #constuctor method
    def __init__(self, color, height, width):
        super().__init__()

        #create sprite surface with dimensions and colors
        self.image=pygame.Surface([width, height])
        self.image.fill(color)

        #get sprites rect defining position and size
        self.rect=self.image.get_rect()

        #set initail velocity with random direction
        self.velocity=[random.choice([-1,1]), random.choice([-1,1])]

    #method to update sprites position
    def update(self):

        #move sprite by its velocity
        self.rect.move_ip(self.velocity)

        #flag to track if the sprite hits the boundary
        boundary_hit=False

        #chk for collisions with left and right boundary and reverse direction
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True

        #chk for collisions with top or bottom boundary and reverse direction
        if self.rect.top <= 0 or self.rect.bottom >=400:
            self.velocity[1] = -self.velocity[-1] 
            boundary_hit = True

        #if boundary was hit, post events to change colors
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE))
            pygame.event.post(pygame.event.Event(BG_COLOR_CHANGE)) 

        #method to chage the sprites color
    def change_color(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))   

# function to change background's color
def change_bg_color():
    global bg_color 
    bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])

# create a grp to hold the sprite
all_sprites_list = pygame.sprite.Group()

sp1 = Sprite(WHITE, 20, 30)

# randomly position the sprite
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)

# add the sprite to the grp
all_sprites_list.add(sp1)

#create the game window
screen = pygame.display.set_mode((500, 400))

#set the window title
pygame.display.set_caption("colorful bounce")

# set bg color
bg_color = BLUE

#apply bg color
screen.fill(bg_color)

# game loop control flag
exit = False

# create a clock obj to control frame rate
clock = pygame.time.Clock()

#main game loop
while not exit:
    #event handling loop
    for event in pygame.event.get():
        # if window's close button is clicked, exit
        if event.type == pygame.QUIT:
            exit == True

         #if sprite's color change event is triggerd, change the color of the sprite
        elif event.type == SPRITE_COLOR_CHANGE:
            sp1.change_color()

        # if bg color change event is triggered, change the color of the bg
        elif event.type == BG_COLOR_CHANGE:
            change_bg_color()

    # update all sprites
    all_sprites_list.update()

    # fill screen with current bg color
    screen.fill(bg_color)

    # draw all sprites to the screen
    all_sprites_list.draw(screen)

    # refresh the display
    pygame.display.flip()
    
    # limit the frame rate to 240 fps
    clock.tick(240)

#uninitialize all pygame modules and close the window
pygame.quit()
