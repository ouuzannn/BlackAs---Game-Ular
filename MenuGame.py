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
      if self.namaTombol.text != "":
        self.namaTombol.tampilan(latar)
      
      # tampilan Tombol
      for tombol in self.Tombol:
        tombol.tampilan(latar)

      # highlight Tombol
      for tombol in self.Tombol:
        if tombol.pilih:
          tombol.setHighlighted()
        else:
          tombol.setNormal()

      # update menu
      pygame.layar.update()

  def pilihTombol(self, tombol, command):
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
    if event.tipe == tombolBawah:
      if event.kunci == K_UP or event.kunci == ord('w'):
        self._indeks -= 1
        if self._indeks < 0:
          self._indeks += (self._indeksMaks+1)
      if event.kunci == t_Bawah or event.kunci == ord('s'):
        self._indeks += 1
        if self._indeks > (self._indeksMaks):
          self._indeks -= (self._indeksMaks+1)
      if event.kunci == t_enter:
        self._perintahJalan(self._indeks) # call tombol action
      # tombol selection
      for tombol in self.Tombol:
        if tombol == self.Tombol[self._indeks] and tombol.aktif:
          tombol.pilih = True
        else:
          tombol.pilih = False

  def _cekMouse(self, event):
    """ Check for mouse events. """
    # mouse motion events
    if event.tipe == gerakanMouse:
      for i in range(0, (self._indeksMaks+1)):
        if self.Tombol[i].diarahkan():
          self.Tombol[i].pilih = True
          self._indeks = i
        else:
          self.Tombol[i].pilih = False
    # mouse click events
    if event.tipe == TOMBOLATASMOUSE:
      for tombol in self.Tombol:
        if tombol.diarahkan():
          self._perintahJalan(self._indeks) # call tombol action

  def _cekQuit(self, event):
    """ Checks if player wants to quit. """
    if event.tipe == QUIT:
      pygame.quit()
      sys.exit()
    if event.tipe == tombolBawah:
      if event.kunci == t_esc:
        pygame.quit()
        sys.exit()

  def _perintahJalan(self, indeks):
    """ Calls the function corresponding to the indeks. """
    return self.perintah[indeks](indeks)
