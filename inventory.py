import pygame
class Inventory(pygame.sprite.Sprite):
  def __init__(self,pos):
    super().__init__()
    self.image = pygame.image.load("assets/inventory.png").convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.center = pos

  def remove_item(self, key):
    self.items.remove(key)

  def add_item(self, new_item):
    self.items.add(new_item)