import pygame

pygame.init()

window_size = (500, 500)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("My first game screen")

grey = (58, 58, 58)

image = pygame.image.load("your_image.jpg")
image = pygame.transform.scale(image, (300, 300))
image_rect = image.get_rect(center=(250, 250))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(grey)
    screen.blit(image, image_rect)
    pygame.display.flip()

pygame.quit()
