import pygame, sys
from pygame.locals import*
import math
import random

pygame.init()
SCREENWIDTH = 400
SCREENHEIGHT = 400
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)
PINK= (255,105,180)
GOLDEN = (255,223,0)
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

screen.fill(RED)

pygame.display.update()

# wait until user quits
running = True

x_speed = 2.0
y_speed = 0.0
x_pos = SCREENWIDTH/2
y_pos = SCREENWIDTH/10
cur_time = pygame.time.get_ticks()



class Food:
    pos: tuple
    calories: int = 1
    eaten: bool = False
    color = GREEN

    def __init__(self):
        # this will initialise the food position
        self.pos = (random.randrange(0,SCREENWIDTH), random.randrange(0,SCREENHEIGHT))
        # self.calories = calories

    def draw(self, surface):
        # this will draw the food
        if self.eaten == False:
            pygame.draw.circle(
                surface, 
                self.color, 
                self.pos,
                13, 
                0
            ) 

class GoldenFood(Food):
    calories: int = 5
    color = GOLDEN


class Scoreboard:
    x_pos: float
    y_pos: float
    score: int


    def draw (self, surface ):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(f'score: {self.score }', True, PINK, GOLDEN)
        textRect = text.get_rect()
        textRect.topright = (SCREENWIDTH,0)
        surface.blit(text, textRect)




    def __init__(self):
        self.score = 0
    

    def eaten_food(self,food):
        self.score = self.score + food.calories


class Snake:
    x_pos: float
    y_pos: float
    x_speed: float = 0
    y_speed: float = 0
    rms_speed: float
    frames: list = []
    color = PINK

    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def calculate_position(self, mouse_pos, SCREENHEIGHT,SCREENWIDTH,delta_time):
        x_accel =  (mouse_pos[0] - self.x_pos) / SCREENWIDTH
        y_accel = (mouse_pos[1] -  self.y_pos) / SCREENHEIGHT

        self.x_speed = self.x_speed + x_accel * delta_time
        self.y_speed = self.y_speed + y_accel * delta_time
        self.rms_speed = (self.x_speed * self.x_speed + self.y_speed * self.y_speed) ** 0.5
        self.x_pos = self.x_pos + self.x_speed * delta_time
        self.y_pos = self.y_pos + self.y_speed * delta_time

    def log(self):

        print(f"speed {self.x_speed:.3f}, {self.y_speed:.3f}, {self.rms_speed:.3f}")
        print(f"pos {self.x_pos:.3f}, {self.y_pos:.3f}")

    def add_frame(self):
        self.frames.append((self.color, (self.x_pos-10, self.y_pos-10, 20, 20)))
        self.frames = self.frames[-100:]

    def draw(self, surface):
        for colour, pos in self.frames:
            pygame.draw.rect(
                surface,
                colour,
                pos
            )

    def has_collision_happened(self, food):
        # this method calculates if self has collided with food
        # dist = ((x_0 - x_1)**2 + (y_0 - y_1)**2)**0.5
        
        if food.eaten: return False 

        dist = ((self.x_pos - food.pos[0])**2 + (self.y_pos - food.pos[1])**2)**0.5
        if dist < 13:
            return True
        else:
            return False
    
        

my_snake = Snake(x_pos=50, y_pos=100)
foods = [
    Food(),
    GoldenFood(),
]
my_scorebord = Scoreboard()


while running:

    screen.fill(BLACK)

    cur_time, old_time = pygame.time.get_ticks(), cur_time
    delta_time = (cur_time-old_time)/100
    print(f"time={cur_time} delta_time={delta_time}")

    mouse_pos = pygame.mouse.get_pos()
   

    my_snake.calculate_position(mouse_pos, SCREENHEIGHT, SCREENWIDTH, delta_time)
    my_snake.add_frame()
    my_snake.draw(screen)
    my_scorebord.draw(screen)

    for food in foods:
        food.draw(screen)
    
    for food in foods:
        has_collided = my_snake.has_collision_happened(food)
        print(f"has collision happened: {has_collided}")
        if has_collided:
            my_scorebord.eaten_food(food)
            food.eaten = True


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       

    else:
        pygame.display.update()


pygame.quit()