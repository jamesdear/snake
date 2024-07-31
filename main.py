import pygame, sys
from pygame.locals import*

pygame.init()
SCREENWIDTH = 400
SCREENHEIGHT = 400
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)
PINK= (255,105,180)
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

screen.fill(RED)

pygame.display.update()

# wait until user quits
running = True

x_speed = 1.0
y_speed = 0.5
x_pos = SCREENWIDTH/2
y_pos = SCREENHEIGHT/2

while running:
    x_pos = x_pos + x_speed
    y_pos = y_pos + y_speed

    pygame.draw.rect(
        screen,
        PINK,
        (x_pos, y_pos, 20, 20)
    )
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.unicode == 'r':
                screen.fill(RED)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(
                screen, 
                (event.pos[0]*255/SCREENWIDTH,event.pos[1]*255/SCREENHEIGHT,180), 
                (event.pos[0]-30,event.pos[1]-30, 60, 60),
                0,
            )
            print(event.pos)
        # if event.type == pygame.MOUSEMOTION:
            # screen.fill((event.pos[1]*255/SCREENHEIGHT,40,event.pos[0]*255/SCREENWIDTH))
 #           pygame.display.flip()
        

    else:
        pygame.display.update()


pygame.quit()