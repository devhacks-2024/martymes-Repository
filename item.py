import pygame
class Item(pygame.sprite.Sprite):
  def __init__(self, name, pos, asset, ap, ad, hp):
    super().__init__()
    self.image = pygame.image.load(asset).convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.name = name
    self.ap = ap
    self. ad = ad
    self.hp = hp