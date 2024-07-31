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
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.unicode == 'r':
                screen.fill(RED)
            elif event.unicode == 'y':
                screen.fill(YELLOW)
            elif event.unicode == 'g':
                screen.fill(GREEN)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(
                screen, 
                (event.pos[0]*255/SCREENWIDTH,event.pos[1]*255/SCREENHEIGHT,180), 
                (event.pos[0]-30,event.pos[1]-30, 60, 60),
                0,
            )
            print(event.pos)

 #           pygame.display.flip()
        

    else:
        pygame.display.update()


pygame.quit()