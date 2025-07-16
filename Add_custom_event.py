import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Custom Event Sprite Color Change")

# Clock to control frame rate
clock = pygame.time.Clock()

# Define custom event
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)  # Change color every 2 seconds

# Define Sprite class
class ColorSprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(x, y))

    def change_color(self):
        self.color = [random.randint(0, 255) for _ in range(3)]
        self.image.fill(self.color)

# Create two sprites
sprite1 = ColorSprite((255, 0, 0), 200, 200)
sprite2 = ColorSprite((0, 0, 255), 400, 200)

# Group them
all_sprites = pygame.sprite.Group(sprite1, sprite2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Custom event to change color
        if event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    # Drawing
    screen.fill((30, 30, 30))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
