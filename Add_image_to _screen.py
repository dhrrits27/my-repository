import pygame

pygame.init()

SW, SH= 500, 500

display_surface=pygame.display.set_mode((SW, SH))
pygame.display.set_caption("add image and backgroud inmage")

background_image=pygame.transform.scale(
    pygame.image.load("bg.jpg").convert(), ((SW, SH)))

penguin_image=pygame.transform.scale(
    pygame.image.load('penguin.jpg').convert_alpha(), ((200, 200)))

penguin_rect=penguin_image.get_rect(center=(SW//2, SH//2-30))

text=pygame.font.Font(None,36).render('hello world', True, pygame.Color('black'))
text_rect=text.get_rect(center=(SW//2, SH//2+110))

def game_loop():
    clock=pygame.time.Clock()
    done=True
    while done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=False

        display_surface.blit(background_image,(0,0))
        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

game_loop()

