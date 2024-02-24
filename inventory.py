import pygame
class Inventory(pygame.sprite.Sprite):
  def __init__(self,pos):
    super().__init__()
    self.image = pygame.image.load("assets/inventory.png").convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.center = pos