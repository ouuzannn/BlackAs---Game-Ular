# pymenu.py

import pygame, TombolMenu, sys
from pygame.locals import *
from konstanta import *

class PyMenu(object):
  """ A class that can create and draw a simple game menu
    with custom Tombol and colors, from where the
    different game modes can be accessed. """

  def __init__(self, menuwarna, x=0, y=0, title="", font="Krungthep"):
    """ Initializes the menu title, Tombol, commands, index and color. """
    # menu title, Tombol and commands
    self.titleButton = TombolMenu.PyButton(x, y, title, font)
    self.Tombol = []
    self.commands = []

    # menu index and color
    self._index = 1
    self._maxIndex = len(self.Tombol)-1
    self.menuwarna = menuwarna

  def draw(self, surface):
    """ Draws the menu screen to the surface. """
    while True:
      # check for events
      self._checkEvents()
      # draw background
      surface.fill(self.menuwarna)
      # draw title
      if self.titleButton.text != "":
        self.titleButton.draw(surface)
      
      # draw Tombol
      for tombol in self.Tombol:
        tombol.draw(surface)

      # highlight Tombol
      for tombol in self.Tombol:
        if tombol.selected:
          tombol.setHighlighted()
        else:
          tombol.setNormal()

      # update menu
      pygame.display.update()

  def addButton(self, tombol, command):
    """ Adds the given tombol to the menu. """
    self.Tombol.append(tombol)
    self.commands.append(command)
    self._maxIndex = len(self.Tombol)-1

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
        self._index -= 1
        if self._index < 0:
          self._index += (self._maxIndex+1)
      if event.kunci == t_Bawah or event.kunci == ord('s'):
        self._index += 1
        if self._index > (self._maxIndex):
          self._index -= (self._maxIndex+1)
      if event.kunci == t_enter:
        self._perintahJalan(self._index) # call tombol action
      # tombol selection
      for tombol in self.Tombol:
        if tombol == self.Tombol[self._index] and tombol.aktif:
          tombol.selected = True
        else:
          tombol.selected = False

  def _cekMouse(self, event):
    """ Check for mouse events. """
    # mouse motion events
    if event.tipe == gerakanMouse:
      for i in range(0, (self._maxIndex+1)):
        if self.Tombol[i].diarahkan():
          self.Tombol[i].selected = True
          self._index = i
        else:
          self.Tombol[i].selected = False
    # mouse click events
    if event.tipe == TOMBOLATASMOUSE:
      for tombol in self.Tombol:
        if tombol.diarahkan():
          self._perintahJalan(self._index) # call tombol action

  def _cekQuit(self, event):
    """ Checks if player wants to quit. """
    if event.tipe == QUIT:
      pygame.quit()
      sys.exit()
    if event.tipe == tombolBawah:
      if event.kunci == t_esc:
        pygame.quit()
        sys.exit()

  def _perintahJalan(self, index):
    """ Calls the function corresponding to the index. """
    return self.commands[index](index)
