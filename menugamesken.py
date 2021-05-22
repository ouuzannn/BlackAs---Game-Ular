# pymenu.py

import pygame, tombolmenusken, sys
from pygame.locals import *
from konstanta import *

class PyMenu(object):
  def __init__(self, menuwarna, x=0, y=0, judul="", font="Krungthep"):
    # menu judul, Tombol and perintah
    self.namaTombol = tombolmenusken.PyButton(x, y, judul, font)
    self.Tombol = []
    self.perintah = []

    # menu indeks and color
    self._indeks = 1
    self._indeksMaks = len(self.Tombol)-1
    self.menuwarna = menuwarna

  #Menggambar menu
  def tampilan(self, latar):
    while True:
      # check for events
      self._checkEvents()
      # tampilan background
      latar.fill(self.menuwarna)
      # tampilan judul
      if self.namaTombol.text != "":  #teks
        self.namaTombol.draw(latar) #tampilan
      
      # tampilan Tombol
      for tombol in self.Tombol:
        tombol.draw(latar)

      # highlight Tombol
      for tombol in self.Tombol:
        if tombol.selected: #pilih
          tombol.setHighlighted()
        else:
          tombol.setNormal()

      # update menu
      pygame.display.update() #layar

  #ditaruh di main
  def tambahkanTombol(self, tombol, command):
    self.Tombol.append(tombol)
    self.perintah.append(command)
    self._indeksMaks = len(self.Tombol)-1

#Cek perintah pada menu
  def _checkEvents(self):
    for event in pygame.event.get():
      # check if player quits
      self._cekQuit(event)
      # check for keyboard events
      self._cekKeyboard(event)
      # check for tombol events
      self._cekMouse(event)

  def _cekKeyboard(self, event):
    """ Check perintah keyboard """
    # tombolBawah events
    if event.type == KEYDOWN:
      if event.key == K_UP or event.key == ord('w'):
        self._indeks -= 1
        if self._indeks < 0:
          self._indeks += (self._indeksMaks+1)
      if event.key == K_DOWN or event.key == ord('s'):
        self._indeks += 1
        if self._indeks > (self._indeksMaks):
          self._indeks -= (self._indeksMaks+1)
      if event.key == K_RETURN:
        self._perintahJalan(self._indeks) # call tombol action
      # tombol selection
      for tombol in self.Tombol:
        if tombol == self.Tombol[self._indeks] and tombol.active:
          tombol.selected = True
        else:
          tombol.selected = False

  def _cekMouse(self, event):
    """ Check perintah pada mouse """
    # mouse motion events
    if event.type == MOUSEMOTION:
      for i in range(0, (self._indeksMaks+1)):
        if self.Tombol[i].isHovered():
          self.Tombol[i].selected = True
          self._indeks = i
        else:
          self.Tombol[i].selected = False
    # mouse click events
    if event.type == MOUSEBUTTONUP:
      #0 = new game
      #1 = exit 
      for tombol in self.Tombol:
        if tombol.isHovered():
          self._perintahJalan(self._indeks) # call tombol action

  def _cekQuit(self, event):
    """ Checks kalau user keluar """
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == KEYDOWN:
      if event.key == K_ESCAPE:
        pygame.quit()
        sys.exit()

  def _perintahJalan(self, indeks):
    """ memanggil fungsi untuk me return printah. """
    print(indeks)
    return self.perintah[indeks](indeks)
