import pygame
import sys
import random 
from menu import Menu
from uni_vars import *

class Ular():
    def __init__(self):
        self.PanjangUlar = 1
        self.letakUlar = [((lebar_layar/2), (tinggi_layar/2))]
        self.arahUlar = random.choice([atas, bawah, kiri, kanan])
        self.nilai = 0
        self.kecepatan = 10    

    def get_head_position(self) :
        return self.letakUlar[0]


    def turn(self, point):
        if self.PanjangUlar > 1 and (point[0]*-1, point[1]*-1) == self.arahUlar:
            return
        else :
            self.arahUlar = point

    def move(self) :
        cur = self.get_head_position()
        x,y = self.arahUlar
        new = (((cur[0]+(x*gridsize))%lebar_layar), (cur[1]+(y*gridsize))%tinggi_layar)
        if (len(self.letakUlar) > 2 and new in self.letakUlar[2:]) :
            self.reset()
        #elif cur == self.letakUlar[0,new] or cur == self.letakUlar[lebar_layar,new] or cur == self.letakUlar[new,0] or cur == self.letakUla[new,tinggi_layar]:
            #self.reset()
        else :
            self.letakUlar.insert(0,new)
            if len(self.letakUlar) > self.PanjangUlar :
                self.letakUlar.pop()
    
    def reset(self) :
        self.PanjangUlar = 1
        self.letakUlar = [((lebar_layar/2), (tinggi_layar/2))]
        self.arahUlar = random.choice([atas, bawah, kiri, kanan])
        self.nilai = 0
        self.kecepatan = 10

    def draw(self, surface):
        i = 0
        for p in self.letakUlar:
            r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
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
                    self.turn(atas)
                elif event.key == pygame.K_DOWN :
                    self.turn(bawah)
                elif event.key == pygame.K_LEFT :
                    self.turn(kiri)
                elif event.key == pygame.K_RIGHT :
                    self.turn(kanan)

class Makanan() :
    def __init__(self):
        self.letakUlar = (0,0)
        self.warna = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.letakUlar = (random.randint(0, grid_width-1)*gridsize, random.randint(0, grid_height-1)*gridsize)

    def draw(self, surface) :
        r = pygame.Rect((self.letakUlar[0], self.letakUlar[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.warna, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

class MakananBonus() :
    def __init__(self):
        self.letakUlar = (0,0)
        self.warna = (25, 163, 49)
        self.randomize_position()
        self.waktu = 0

    def randomize_position(self):
        #i = 5
        #if i in range (0,5) :
            self.letakUlar = (random.randint(0, grid_width-1)*gridsize, random.randint(0, grid_height-1)*gridsize)

    def draw(self, surface) :
        r = pygame.Rect((self.letakUlar[0], self.letakUlar[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.warna, r)
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
lebar_layar = 480
tinggi_layar = 480

gridsize = 20
grid_width = lebar_layar/gridsize
grid_height = tinggi_layar/gridsize

atas = (0, -1)
bawah = (0, 1)
kiri = (-1, 0)
kanan = (1,0)

def menu():
	main_menu = Menu()

	while main_menu.running:
		clock.tick(40)

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
    screen = pygame.display.set_mode((lebar_layar, tinggi_layar), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    GambarKotak(surface)

    ular = Ular()
    makanan = Makanan()
    makananbonus = MakananBonus()
    waktu = 0
    
    myfont = pygame.font.SysFont("monospace",50)

    while True :
        clock.tick(ular.kecepatan) #kecepatan ular
        ular.KontrolUlar()
        GambarKotak(surface)
        ular.move()
        if ular.get_head_position() == makanan.letakUlar :
            ular.PanjangUlar += 1
            ular.nilai += 1
            makanan.randomize_position()
            if ular.nilai%10==0:
                ular.kecepatan+=4
        elif ular.get_head_position() == makananbonus.letakUlar :
            ular.PanjangUlar += 1
            ular.nilai += 5
        if ular.nilai !=0 and ular.nilai % 5 == 0 and waktu % 5 !=0  :
            makananbonus.draw(surface)
        ular.draw(surface)
        makanan.draw(surface)
        #if ular.nilai !=0 and ular.nilai % 5 == 0 :

        waktu += 1
        screen.blit(surface, (0,0)) #menampilkan gambar pada window game
        text = myfont.render("Score : {0}".format(ular.nilai), 1, (0,0,0))
        screen.blit(text, (5,10))
        pygame.display.update()
        
menu()
main()