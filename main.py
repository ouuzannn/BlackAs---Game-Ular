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

    def PosisiKepalaUlar(self) :
        return self.letakUlar[0]
    
    def turn(self, point):
        if self.PanjangUlar > 1 and (point[0]*-1, point[1]*-1) == self.arahUlar:
            return
        else :
            self.arahUlar = point

    def PergerakanUlar(self) :
        cur = self.PosisiKepalaUlar()
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

    def GambarUlar(self, surface):
        PenandaKepala = 0
        for p in self.letakUlar:
            bagianular = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
            if PenandaKepala == 0 :#penanda kepala
                self.warna = (25, 24, 47)
                pygame.draw.rect(surface, self.warna, bagianular)
            else :
                self.warna = (255, 24, 47)
                pygame.draw.rect(surface, self.warna, bagianular)
            pygame.draw.rect(surface, (25,24,228), bagianular, 1)
            PenandaKepala +=1

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
        self.letakmakanan = (0,0)
        self.warna = (223, 163, 49)
        self.PosisiAcakMakanan()

    def PosisiAcakMakanan(self):
        self.letakmakanan = (random.randint(1, grid_width-2)*gridsize, random.randint(1, grid_height-2)*gridsize)

    def gambarObjek(self, surface) :
        gambarmakanan = pygame.Rect((self.letakmakanan[0], self.letakmakanan[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.warna, gambarmakanan)
        pygame.draw.rect(surface, (93, 216, 228), gambarmakanan, 1)

class MakananBonus() :
    def __init__(self):
        self.LetakMakananBonus = (0,0)
        #self.warna = [(25, 163, 49), (0,0,0)]
        self.PosisiAcakMakanan()
        self.timer = 0
        self.waktubonus = 25
        self.tanda = 0

    def PosisiAcakMakanan(self):
            self.LetakMakananBonus = (random.randint(1, grid_width-2)*gridsize, random.randint(1, grid_height-2)*gridsize)

    def gambarObjek(self, surface, pilihwarna) :
        gambarmakananbonus = pygame.Rect(((self.LetakMakananBonus[0]-5), (self.LetakMakananBonus[1]-5)), (30, 30))
        pygame.draw.rect(surface, pilihwarna, gambarmakananbonus)
        pygame.draw.rect(surface, (93, 216, 228), gambarmakananbonus, 1)

class kotak : 
    def GambarKotak(self,surface) :
        for y in range(0, int(grid_height)) :
            for x in range(0, int(grid_width)) :
                if (x+y) %2 == 0:
                    gridgenap = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                    pygame.draw.rect(surface,(93,216,228), gridgenap)
                else :
                    gridganjil = pygame.Rect((x*gridsize, y*gridsize), (gridsize, gridsize))
                    pygame.draw.rect(surface, (84,194,205), gridganjil)
        #gambarborder
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
waktubatas = 5

gridsize = 20
grid_width = lebar_layar/gridsize
grid_height = tinggi_layar/gridsize

atas = (0, -1)
bawah = (0, 1)
kiri = (-1, 0)
kanan = (1,0)
hitung = 0

def mainin(indeks) :
    
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
    hitungwaktu=0
    hitung=0
    #Setting ukuran dan jenis font dari tulisan score
    myfont = pygame.font.SysFont("monospace",18)
    
    while True :
        if indeks == 1:
            pygame.quit()
            sys.exit()

        clock.tick(ular.kecepatan) #kecepatan ular
        ular.KontrolUlar()
        papan.GambarKotak(surface)
        ular.PergerakanUlar()
        hitung += 1
        
        if ular.PosisiKepalaUlar() == makanan.letakmakanan :
            ular.PanjangUlar += 1
            ular.nilai += 1
            ular.hitungmakanan += 1
            makananbonus.timer=0
            print("k", ular.kecepatan)
            makanan.PosisiAcakMakanan()
            if ular.nilai%10==0:
                ular.kecepatan = ular.kecepatan * 1.5
                makananbonus.waktubonus = makananbonus.waktubonus * 1.5
                          
        if(ular.hitungmakanan !=0 and ular.hitungmakanan % 5 == 0):
            makananbonus.tanda=1
                    
        if ( makananbonus.tanda==1 and makananbonus.timer<makananbonus.waktubonus) : 
            if hitung%2==0:
                pilihwarna=warnaa[0]
            else:
                pilihwarna=warnaa[1]
          
            makananbonus.gambarObjek(surface, pilihwarna)
            makananbonus.timer+=1

            if ular.PosisiKepalaUlar() == makananbonus.LetakMakananBonus :
                ular.PanjangUlar += 1
                ular.nilai += 5
                ular.hitungmakanan = 0
                makananbonus.tanda=0
                makananbonus.timer=0
                if ular.nilai%10==0:
                    ular.kecepatan = ular.kecepatan * 1.5
                    makananbonus.waktubonus = makananbonus.waktubonus * 1.5 
                #tampilbonus = 0
                makananbonus.PosisiAcakMakanan()           
            print("t", makananbonus.timer)
            print("w", makananbonus.waktubonus)

        elif makananbonus.timer>=makananbonus.waktubonus:
            makananbonus.tanda=0                       

        ular.GambarUlar(surface)
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
    TombolNewGame = TombolMenu.PyButton(lebar_layar/2, 130, "New Game")
    TombolQuit = TombolMenu.PyButton(tinggi_layar/2, 220, "Quit")

    menu.tambahkanTombol(TombolNewGame, mainin)
    menu.tambahkanTombol(TombolQuit, mainin)

  # draw the menu
    menu.tampilan(window)
    

if __name__ == '__main__':
    Menu(cek)

Menu(cek)