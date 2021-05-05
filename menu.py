import pygame
from random import randint
from uni_vars import win, width, height
pygame.font.init()


class Button:
    def __init__(self, window, x, y, width, height, text='', text_size=20):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_size = text_size
        self.color = (255, 255, 255)
        self.text_color = (0, 0, 0)
        self.rect = (self.x, self.y, self.width, self.height)
        self.font = pygame.font.SysFont('Comic Sans MS', self.text_size)

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
        pygame.draw.rect(self.window, self.color, self.rect)
        text = self.font.render(self.text, True, self.text_color)
        x = self.x + 5
        y = self.y + 20
        self.window.blit(text, (x, y))


class Menu:
	def __init__(self):
		self.title_size = 80
		self.title_color = [255, 255, 255]
		self.title_pos = (width/2-self.title_size*2, 80) #posisi judul
		self.waktu = 0
		self.running = True
		self.btn_width = 200
		self.btn_height = 65
		self.play_button = Button(win, (width / 2 - self.btn_width / 2), (height / 2.2),
                         self.btn_width, self.btn_height,
                         text='Permainan Baru', text_size=20)

		self.controls_button = Button(win, (width / 2 - self.btn_width / 2), (height / 2 + 75),
                         self.btn_width, self.btn_height,
                         text='Keluar', text_size=20)

		self.play_button.color = (0, 255, 0)

		self.show_controls = False

	def message(self, text, text_size, color, letakUlar):
		font = pygame.font.SysFont('Comic Sans MS', text_size)
		screen_text = font.render(text, True, color)
		win.blit(screen_text, letakUlar)

	def logic(self):
		self.waktu += 1

		if self.waktu % 10 == 0:
			self.title_color[0] = randint(0, 255)
			self.title_color[1] = randint(0, 255)
			self.title_color[2] = randint(0, 255)

		if self.play_button.clicked():
			self.running = False

		if self.controls_button.clicked():
			if self.show_controls:
				self.show_controls = False
			if self.show_controls == False:
				self.show_controls = True

	def render(self):
		self.message("Welcome to", 40, (255, 255, 255), (width/2-50*2, self.title_pos[1]-50))
		self.message("Python.io", self.title_size, self.title_color, self.title_pos)

		self.play_button.render()
		self.controls_button.render()

		if self.show_controls:
			self.message("Press Control Button", 20, (255, 255, 255), (width/4+50, height/1.2))
