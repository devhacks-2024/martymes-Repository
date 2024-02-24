from typing import Any
import pygame
ALIVE_TIME = 1000

class Damage_Area(pygame.sprite.Sprite):
    def __init__(self, damage, start_pos, size) -> None:
        super().__init__()
        self.start_pos = start_pos
        self.size = size
        self.damage = damage
        self.area_surface = pygame.Surface((size, size))
        self.area_surface.fill((255,0,0))

        self.image = self.area_surface
        self.rect = self.image.get_rect()
        self.rect.topleft = start_pos

        self.alive = pygame.time.get_ticks()

    def get_damage(self):
        return self.damage

    def explode(self):
        pass #we can chain explosion
    
    def update(self) -> None:
        if(self.alive + ALIVE_TIME < pygame.time.get_ticks()):
            self.kill()