# pymenu.py

import pygame, TombolMenu, sys
from pygame.locals import *
from konstanta import *

class PyMenu(object):
  """ A class that can create and draw a simple game menu
    with custom buttons and colors, from where the
    different game modes can be accessed. """

  def __init__(self, menucolor, x=0, y=0, title="", font="Krungthep"):
    """ Initializes the menu title, buttons, commands, index and color. """
    # menu title, buttons and commands
    self.titleButton = TombolMenu.PyButton(x, y, title, font)
    self.buttons = []
    self.commands = []

    # menu index and color
    self._index = 1
    self._maxIndex = len(self.buttons)-1
    self.menucolor = menucolor

  def draw(self, surface):
    """ Draws the menu screen to the surface. """
    while True:
      # check for events
      self._checkEvents()
      # draw background
      surface.fill(self.menucolor)
      # draw title
      if self.titleButton.text != "":
        self.titleButton.draw(surface)
      
      # draw buttons
      for button in self.buttons:
        button.draw(surface)

      # highlight buttons
      for button in self.buttons:
        if button.selected:
          button.setHighlighted()
        else:
          button.setNormal()

      # update menu
      pygame.display.update()

  def addButton(self, button, command):
    """ Adds the given button to the menu. """
    self.buttons.append(button)
    self.commands.append(command)
    self._maxIndex = len(self.buttons)-1

  def _checkEvents(self):
    """ Checks for pygame events. """
    for event in pygame.event.get():
      # check if player quits
      self._cekQuit(event)
      # check for keyboard events
      self._cekKeyboard(event)
      # check for button events
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
        self._perintahJalan(self._index) # call button action
      # button selection
      for button in self.buttons:
        if button == self.buttons[self._index] and button.aktif:
          button.selected = True
        else:
          button.selected = False

  def _cekMouse(self, event):
    """ Check for mouse events. """
    # mouse motion events
    if event.tipe == gerakanMouse:
      for i in range(0, (self._maxIndex+1)):
        if self.buttons[i].diarahkan():
          self.buttons[i].selected = True
          self._index = i
        else:
          self.buttons[i].selected = False
    # mouse click events
    if event.tipe == TOMBOLATASMOUSE:
      for button in self.buttons:
        if button.diarahkan():
          self._perintahJalan(self._index) # call button action

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
