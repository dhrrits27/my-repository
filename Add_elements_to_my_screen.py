import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RECT_COLOR = (0, 128, 255)  # You can change this to any color

font = pygame.font.SysFont(None, 48)
text = font.render("Hello, Pygame!", True, BLACK)

rect_width, rect_height = 150, 100
rect_x = (640 - rect_width) // 2
rect_y = (480 - rect_height) // 2
rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

running = True
while running:
    screen.fill(WHITE)

    pygame.draw.rect(screen, RECT_COLOR, rect)

    text_rect = text.get_rect(center=(320, 400))
    screen.blit(text, text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
