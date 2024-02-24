import pygame
class Item(pygame.sprite.Sprite):
  def __init__(self, name, pos, asset):
    super().__init__()
    self.image = pygame.image.load(asset).convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.name = name