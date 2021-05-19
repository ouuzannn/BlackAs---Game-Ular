# pymenu.py

import pygame, TombolMenu, sys
from pygame.locals import *
from konstanta import *

class PyMenu(object):
  """ A class that can create and tampilan a simple game menu
    with custom Tombol and colors, from where the
    different game modes can be accessed. """

  def __init__(self, menuwarna, x=0, y=0, judul="", font="Krungthep"):
    """ Initializes the menu judul, Tombol, perintah, indeks and color. """
    # menu judul, Tombol and perintah
    self.namaTombol = TombolMenu.PyButton(x, y, judul, font)
    self.Tombol = []
    self.perintah = []

    # menu indeks and color
    self._indeks = 1
    self._indeksMaks = len(self.Tombol)-1
    self.menuwarna = menuwarna

  def tampilan(self, latar):
    """ tampilans the menu screen to the latar. """
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

  def tambahkanTombol(self, tombol, command):
    """ Adds the given tombol to the menu. """
    self.Tombol.append(tombol)
    self.perintah.append(command)
    self._indeksMaks = len(self.Tombol)-1

  def _checkEvents(self):
    """ Checks for pygame events. """
    for event in pygame.event.get():
      # check if player quits
      self._cekQuit(event)
      # check for keyboard events
      self._cekKeyboard(event)
      # check for tombol events
      self._cekMouse(event)

  def _cekKeyboard(self, event):
    """ Check for keyboard events. """
    # tombolBawah events
    if event.type == KEYDOWN:
      if event.key == K_UP or event.key == ord('w'):
        self._indeks -= 1
        if self._indeks < 0:
          self._indeks += (self._indeksMaks+1)
<<<<<<< HEAD
      if event.key == K_DOWN or event.key == ord('s'):
=======
      if event.kunci == t_bawah or event.kunci == ord('s'):
>>>>>>> 1abd321800b6c61f9a8ff33a76e488811feba028
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
    """ Check for mouse events. """
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
      for tombol in self.Tombol:
        if tombol.isHovered():
          self._perintahJalan(self._indeks) # call tombol action

  def _cekQuit(self, event):
    """ Checks if player wants to quit. """
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == KEYDOWN:
      if event.key == K_ESCAPE:
        pygame.quit()
        sys.exit()

  def _perintahJalan(self, indeks):
    """ Calls the function corresponding to the indeks. """
    return self.perintah[indeks](indeks)
