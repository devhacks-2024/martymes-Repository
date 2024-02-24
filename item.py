import pygame
class Item(pygame.sprite.Sprite):
  def __init__(self, sprite, name, ap, ad, hp):
    super().__init__(self)
    self.sprite = sprite
    self.name = name
    self.ap = ap
    self. ad = ad
    self.hp = hp