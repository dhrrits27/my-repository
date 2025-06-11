import pygame

def main():
    pygame.init()
    sw , sh=500 , 500
    screen=pygame.display.set_mode((sw,sh))
    pygame.display.set_caption("color changing sprite")

    colors={
        'red':pygame.Color('red'),
        'green':pygame.Color('green'),
        'blue':pygame.Color('blue'),
        'white':pygame.Color('white'),
        'yellow':pygame.Color('yellow')
    }

    current_color=colors['white']

    x,y=30,30
    spw,sph=60,60

    clock=pygame.time.Clock()

    done=False

    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True

        pressed=pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x-=3
        if pressed[pygame.K_RIGHT]: x+=3
        if pressed[pygame.K_UP]: y-=3
        if pressed[pygame.K_DOWN]: y+=3

        x=min(max(0,x),sw-spw)
        y=min(max(0,y),sh-sph)

        if x==0: current_color=colors['blue']
        elif x==sw-spw: current_color=colors['yellow']
        elif y==0: current_color=colors['red']
        elif y==sh-sph: current_color=colors['green']
        else: current_color=colors['white']

        screen.fill ((0,0,0))

        pygame.draw.rect(screen, current_color, (x,y,spw,sph))
        pygame.display.flip()
        clock.tick(90)

    pygame.quit()

if __name__=="__main__":
    main()
    