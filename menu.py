import pygame
from random import randint
from uni_vars import win, width, height
pygame.font.init()


class Button:
    def __init__(self, window, x, y, width, height, teks='', ukuran_teks=20):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.teks = teks
        self.ukuran_teks = ukuran_teks
        self.warna = (255, 255, 255)
        self.warna_teks = (0, 0, 0)
        self.rect = (self.x, self.y, self.width, self.height)
        self.font = pygame.font.SysFont('Comic Sans MS', self.ukuran_teks)

    def clicked(self):
        mouse = pygame.mouse.get_pos()
        mouse_x = mouse[0]
        mouse_y = mouse[1]
        mouse_press = pygame.mouse.get_pressed()

        if mouse_press[0]:
            if mouse_x > self.x and mouse_x < self.x + self.width:
                if mouse_y > self.y and mouse_y < self.y + self.height:
                    return True

    def render(self):
		#Posisi Teks Button
        pygame.draw.rect(self.window, self.warna, self.rect)
        teks = self.font.render(self.teks, True, self.warna_teks)
        x = self.x + 5
        y = self.y + 20
        self.window.blit(teks, (x, y))


class Menu:
	def __init__(self):
		self.ukuran_judul = 80
		self.warna_judul = [255, 255, 255]
		self.posisi_judul = (width/2-self.ukuran_judul*2, 80) #posisi judul
		self.waktu = 0
		self.running = True
		self.btn_width = 200
		self.btn_height = 65
		self.play_button = Button(win, (width / 2 - self.btn_width / 2), (height / 2.2),
                         self.btn_width, self.btn_height,
                         teks='Permainan Baru', ukuran_teks=20)

		self.controls_button = Button(win, (width / 2 - self.btn_width / 2), (height / 2 + 75),
                         self.btn_width, self.btn_height,
                         teks='Keluar', ukuran_teks=20)

		self.play_button.warna = (0, 255, 0)

		self.show_controls = False

	def message(self, teks, ukuran_teks, warna, letakUlar):
		font = pygame.font.SysFont('Comic Sans MS', ukuran_teks)
		screen_text = font.render(teks, True, warna)
		win.blit(screen_text, letakUlar)

	def logic(self):
		self.waktu += 1

		if self.waktu % 10 == 0:
			self.warna_judul[0] = randint(0, 255)
			self.warna_judul[1] = randint(0, 255)
			self.warna_judul[2] = randint(0, 255)

		if self.play_button.clicked():
			self.running = False

		if self.controls_button.clicked():
			if self.show_controls:
				self.show_controls = False
			if self.show_controls == False:
				self.show_controls = True

	def render(self):
		self.message("Welcome to", 40, (255, 255, 255), (width/2-50*2, self.posisi_judul[1]-50))
		self.message("Python.io", self.ukuran_judul, self.warna_judul, self.posisi_judul)

		self.play_button.render()
		self.controls_button.render()

		if self.show_controls:
			self.message("Press Control Button", 20, (255, 255, 255), (width/4+50, height/1.2))
