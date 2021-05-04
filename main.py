import pygame
import sys
import random 
from menu import Menu
from uni_vars import *

class Snake():
    def __init__(self):
        self.PanjangUlar = 1
        self.positions = [((screen_width/2), (tinggi_layar/2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0
            

    def get_position_kepala(self) :
        return self.positions[0]

    def turn(self, point):
        if self.PanjangUlar > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else :
            self.direction = point

    def move(self) :
        cur = self.get_position_kepala()
        x,y = self.direction
        new = (((cur[0]+(x*ukurankotak))%screen_width), (cur[1]+(y*ukurankotak))%tinggi_layar)
        if (len(self.positions) > 2 and new in self.positions[2:]) :
            self.reset()
        #elif buat kalo nabrak dinding mati
        else :
            self.positions.insert(0,new)
            if len(self.positions) > self.PanjangUlar :
                self.positions.pop()
    
    def reset(self) :
        self.PanjangUlar = 1
        self.positions = [((screen_width/2), (tinggi_layar/2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def draw(self, surface):
        i = 0
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (ukurankotak,ukurankotak))
            if i == 0 :#penanda kepala
                self.warna = (25, 24, 47)
                pygame.draw.rect(surface, self.warna, r)
            else :
                self.warna = (255, 24, 47)
                pygame.draw.rect(surface, self.warna, r)
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
        self.warna = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, grid_width-1)*ukurankotak, random.randint(0, grid_height-1)*ukurankotak)

    def draw(self, surface) :
        r = pygame.Rect((self.position[0], self.position[1]), (ukurankotak, ukurankotak))
        pygame.draw.rect(surface, self.warna, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

def GambarKotak(surface) :
    for y in range(0, int(grid_height)) :
        for x in range(0, int(grid_width)) :
            if (x+y) %2 == 0:
                r = pygame.Rect((x*ukurankotak, y*ukurankotak), (ukurankotak,ukurankotak))
                pygame.draw.rect(surface,(93,216,228), r)
            else :
                rr = pygame.Rect((x*ukurankotak, y*ukurankotak), (ukurankotak, ukurankotak))
                pygame.draw.rect(surface, (84,194,205), rr)

#GLOBAL VARIABEL
screen_width = 480
tinggi_layar = 480

ukurankotak = 20
grid_width = screen_width/ukurankotak
grid_height = tinggi_layar/ukurankotak

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1,0)

def menu():
	main_menu = Menu()

	while main_menu.running:
		clock.tick(60)

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
    screen = pygame.display.set_mode((screen_width, tinggi_layar), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    GambarKotak(surface)

    snake = Snake()
    food = Food()
    
    myfont = pygame.font.SysFont("monospace",50)

    while True :
        clock.tick(40) #kecepatan ular
        snake.KontrolUlar()
        GambarKotak(surface)
        snake.move()
        if snake.get_position_kepala() == food.position :
            snake.PanjangUlar += 1
            snake.score += 1
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0,0))
        text = myfont.render("Score {0}".format(snake.score), 1, (0,0,0))
        screen.blit(text, (5,10))
        pygame.display.update()

menu()
main()
