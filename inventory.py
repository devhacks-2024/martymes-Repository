import pygame
class Inventory:
  def __init__(self, items):
    self.items = items # Group of sprites

  def remove_item(self, key):
    self.items.remove(key)

  def add_item(self, new_item):
    self.items.add(new_item)

  def draw_sprites(self):
    self.items.draw()