import pygame
class Item(pygame.sprite.Sprite):
  def __init__(self, name, pos, asset):
    super().__init__()
    self.image = pygame.image.load(asset).convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.center = pos

    self.name = name

  def update(self):
    # depending on key press, blacks out the item corresponding to the ability assigned to that key press
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q or event.key == pygame.K_o:
          print("hello")