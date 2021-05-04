import pygame
import sys
import random 
from menu import Menu
from uni_vars import *

class Snake():
    def __init__(self):
        self.PanjangUlar = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0
        self.kecepatan = 10    

    def get_head_position(self) :
        return self.positions[0]


    def turn(self, point):
        if self.PanjangUlar > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else :
            self.direction = point

    def move(self) :
        cur = self.get_head_position()
        x,y = self.direction
        new = (((cur[0]+(x*gridsize))%screen_width), (cur[1]+(y*gridsize))%screen_height)
        if (len(self.positions) > 2 and new in self.positions[2:]) :
            self.reset()
        #elif cur == self.positions[0,new] or cur == self.positions[screen_width,new] or cur == self.positions[new,0] or cur == self.positions[new,screen_height]:
            #self.reset()
        else :
            self.positions.insert(0,new)
            if len(self.positions) > self.PanjangUlar :
                self.positions.pop()
    
    def reset(self) :
        self.PanjangUlar = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0
        self.kecepatan = 10

    def draw(self, surface):
        i = 0
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
            if i == 0 :#penanda kepala
                self.color = (25, 24, 47)
                pygame.draw.rect(surface, self.color, r)
            else :
                self.color = (255, 24, 47)
                pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (25,24,228), r, 1)
            i +=1

    def KontrolUlar(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN :
                    self.turn(down)
                elif event.key == pygame.K_LEFT :
                    self.turn(left)
                elif event.key == pygame.K_RIGHT :
                    self.turn(right)

class Food() :
    def __init__(self):
        self.position = (0,0)
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, grid_width-1)*gridsize, random.randint(0, grid_height-1)*gridsize)

    def draw(self, surface) :
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

class FoodBonus() :
    def __init__(self):
        self.position = (0,0)
        self.color = (25, 163, 49)
        self.randomize_position()
        self.timer = 0

    def randomize_position(self):
        self.position = (random.randint(0, grid_width-1)*gridsize, random.randint(0, grid_height-1)*gridsize)

    def draw(self, surface) :
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

def GambarKotak(surface) :
    for y in range(0, int(grid_height)) :
        for x in range(0, int(grid_width)) :
            if (x+y) %2 == 0:
                r = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface,(93,216,228), r)
            else :
                rr = pygame.Rect((x*gridsize, y*gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, (84,194,205), rr)

#GLOBAL VARIABEL
screen_width = 480
screen_height = 480

gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1,0)

def menu():
	main_menu = Menu()

	while main_menu.running:
		clock.tick(100)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				global running
				main_menu.running = False
				running = False

		main_menu.logic()
		win.fill(background)
		main_menu.render()
		pygame.display.update()


def main() :
    pygame.init() #buat screen
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    GambarKotak(surface)

    snake = Snake()
    food = Food()
    foodbonus = FoodBonus()
    timer = 0
    
    myfont = pygame.font.SysFont("monospace",50)

    while True :
        clock.tick(snake.kecepatan) #kecepatan ular
        snake.KontrolUlar()
        GambarKotak(surface)
        snake.move()
        if snake.get_head_position() == food.position :
            snake.PanjangUlar += 1
            snake.score += 1
            food.randomize_position()
            if snake.score%10==0:
                snake.kecepatan+=4
        elif snake.get_head_position() == foodbonus.position :
            snake.PanjangUlar += 1
            snake.score += 5
        if snake.score !=0 and snake.score % 5 == 0 and timer % 5 !=0  :
            foodbonus.draw(surface)
        snake.draw(surface)
        food.draw(surface)
        #if snake.score !=0 and snake.score % 5 == 0 :

        timer += 1
        screen.blit(surface, (0,0))
        text = myfont.render("Score {0}".format(snake.score), 1, (0,0,0))
        screen.blit(text, (5,10))
        pygame.display.update()


menu()
main()
