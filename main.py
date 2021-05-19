import pygame
import sys
import random 
import TombolMenu,MenuGame
from konstanta import *


class Ular():
    def __init__(self):
        self.PanjangUlar = 1
        self.letakUlar = [((lebar_layar/2), (tinggi_layar/2))]
        self.arahUlar = random.choice([atas, bawah, kiri, kanan])
        self.nilai = 0
        self.kecepatan = 5
        self.hitungmakanan = 0

    def get_head_position(self) :
        return self.letakUlar[0]
    def turn(self, point):
        if self.PanjangUlar > 1 and (point[0]*-1, point[1]*-1) == self.arahUlar:
            return
        else :
            self.arahUlar = point

    def PergerakanUlar(self) :
        cur = self.get_head_position()
        x,y = self.arahUlar
        new = (((cur[0]+(x*gridsize))%lebar_layar), (cur[1]+(y*gridsize))%tinggi_layar)
        if (len(self.letakUlar) > 2 and new in self.letakUlar[2:]) :
            #akhir()
            cek=0
            self.reset()
            Menu(cek)            
        elif cur[0] >= (lebar_layar-20) or cur[0] <= 0 or cur[1] >= (tinggi_layar-20) or cur[1] <= 0:
            #akhir()
            cek=0
            self.reset()
            Menu(cek)
        else :
            self.letakUlar.insert(0,new)
            if len(self.letakUlar) > self.PanjangUlar :
                self.letakUlar.pop()
    
    def reset(self) :
        self.PanjangUlar = 1
        self.letakUlar = [((lebar_layar/2), (tinggi_layar/2))]
        self.arahUlar = random.choice([atas, bawah, kiri, kanan])
        self.nilai = 0
        self.kecepatan = 5
        self.hitungmakanan = 0

    def draw(self, surface):
        PenandaKepala = 0
        for p in self.letakUlar:
            r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
            if PenandaKepala == 0 :#penanda kepala
                self.warna = (25, 24, 47)
                pygame.draw.rect(surface, self.warna, r)
            else :
                self.warna = (255, 24, 47)
                pygame.draw.rect(surface, self.warna, r)
            pygame.draw.rect(surface, (25,24,228), r, 1)
            PenandaKepala +=1

    def KontrolUlar(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
            elif event.type == pygame.tombolBawah :
                if event.key == pygame.t_atas:
                    self.turn(atas)
                elif event.key == pygame.t_bawah :
                    self.turn(bawah)
                elif event.key == pygame.t_kiri :
                    self.turn(kiri)
                elif event.key == pygame.t_kanan :
                    self.turn(kanan)

class Makanan() :
    def __init__(self):
        self.letakUlar = (0,0)
        self.warna = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.letakUlar = (random.randint(1, grid_width-2)*gridsize, random.randint(1, grid_height-2)*gridsize)

    def gambarObjek(self, surface) :
        r = pygame.Rect((self.letakUlar[0], self.letakUlar[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.warna, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

class MakananBonus() :
    def __init__(self):
        self.letakUlar = (0,0)
        #self.warna = [(25, 163, 49), (0,0,0)]
        self.randomize_position()
        self.timer = 0

    def randomize_position(self):
            self.letakUlar = (random.randint(1, grid_width-2)*gridsize, random.randint(1, grid_height-2)*gridsize)

    def gambarObjek(self, surface, pilihwarna) :
        r = pygame.Rect(((self.letakUlar[0]-5), (self.letakUlar[1]-5)), (30, 30))
        pygame.draw.rect(surface, pilihwarna, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

class kotak : 
    def GambarKotak(self,surface) :
        for y in range(0, int(grid_height)) :
            for x in range(0, int(grid_width)) :
                if (x+y) %2 == 0:
                    r = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                    pygame.draw.rect(surface,(93,216,228), r)
                else :
                    rr = pygame.Rect((x*gridsize, y*gridsize), (gridsize, gridsize))
                    pygame.draw.rect(surface, (84,194,205), rr)
        for y in range(0, int(grid_height)) :
            for x in range(0, int(grid_width)) :
                if (x<1 or y<1 or x>22 or y>22):
                    xxx = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                    pygame.draw.rect(surface,(0,0,0), xxx)


#GLOBAL VARIABEL
clock = pygame.time.Clock()
lebar_layar = 480
tinggi_layar = 480
latar = (0, 0, 0)
win = pygame.display.set_mode((lebar_layar, tinggi_layar))
pygame.init()
bonus=bool(0)

gridsize = 20
grid_width = lebar_layar/gridsize
grid_height = tinggi_layar/gridsize

atas = (0, -1)
bawah = (0, 1)
kiri = (-1, 0)
kanan = (1,0)

def mainin(indeks) :
    # if menu.main_menu.show_controls :
    #     return 0
     #buat screen
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((lebar_layar, tinggi_layar), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    
    #deklarasi objek
    papan = kotak()
    ular = Ular()
    makanan = Makanan()
    makananbonus = MakananBonus()

    putih=(255, 255, 255)
    hijau=(25, 163, 49)
    warnaa=[putih,hijau]
    hitung=0
    #Setting ukuran dan jenis font dari tulisan score
    myfont = pygame.font.SysFont("monospace",18)
    #tampilbonus = bool(1)

    while True :
        if indeks == 1:
            pygame.quit()
            sys.exit()

        #print (indeks) 
        clock.tick(ular.kecepatan) #kecepatan ular
        ular.KontrolUlar()
        #kotak.GambarKotak(surface)
        papan.GambarKotak(surface)
        ular.PergerakanUlar()
        hitung += 1
        if ular.get_head_position() == makanan.letakUlar :
            ular.PanjangUlar += 1
            ular.nilai += 1
            ular.hitungmakanan += 1
            makanan.randomize_position()
            if ular.nilai%10==0:
                ular.kecepatan+=4
        
        # if ular.hitungmakanan > 5 and (ular.hitungmakanan+1) % 5 ==0 :
        #     tampilbonus = 1
        #if ular.hitungmakanan !=0 and ular.hitungmakanan % 5 == 0 and tampilbonus == 1 :

        if (ular.hitungmakanan !=0 and ular.hitungmakanan % 5 == 0) : #or (ular.hitungmakanan>5 and (ular.hitungmakanan-1)%5==0 and ular.nilai%5==0) :
            if hitung%2==0:
                pilihwarna=warnaa[0]
            else:
                pilihwarna=warnaa[1]
            makananbonus.gambarObjek(surface, pilihwarna)
            if ular.get_head_position() == makananbonus.letakUlar :
                ular.PanjangUlar += 1
                ular.nilai += 5
                ular.hitungmakanan = 0
                #tampilbonus = 0
                makananbonus.randomize_position()
        ular.draw(surface)
        makanan.gambarObjek(surface)

        screen.blit(surface, (0,0)) #menampilkan gambar pada window game
        text = myfont.render("Score : {0}".format(ular.nilai), 1, (putih))
        screen.blit(text, (20,0))
        pygame.display.update()  

cek=bool(1)

def Menu(cek):

  
    window = pygame.display.set_mode((lebar_layar, tinggi_layar), 0, 32)

    if cek == 1 :
        menu = MenuGame.PyMenu(BLACK, lebar_layar/2, 45, "GAME ULAR BLACK AS")
    else :
        menu = MenuGame.PyMenu(RED, lebar_layar/2, 45, "PERMAINAN BERAKHIR")
  
  # create the buttons
    newButton = TombolMenu.PyButton(lebar_layar/2, 130, "New Game")
    quitButton = TombolMenu.PyButton(tinggi_layar/2, 220, "Quit")

    menu.tambahkanTombol(newButton, mainin)
    menu.tambahkanTombol(quitButton, mainin)

  # draw the menu
    menu.tampilan(window)
    

if __name__ == '__main__':
    Menu(cek)

Menu()