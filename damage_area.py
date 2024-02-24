
import pygame
from character_frames import *
ALIVE_TIME = 200

class Damage_Area(pygame.sprite.Sprite):
    def __init__(self, damage, start_pos, size) -> None:
        super().__init__()
        self.start_pos = start_pos
        self.size = size
        self.damage = damage


        self.current_animation = self.render_image(explosion_animation(), size)
        self.current_animation_index = 0
        self.current_animation_speed = ALIVE_TIME//len(self.current_animation)
        self.last_animation_time = pygame.time.get_ticks()
        
        self.image = self.current_animation[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = start_pos

        self.alive = pygame.time.get_ticks()

    def render_image(self, idle_animation, size):
        loaded_pictures = []
        for pic_name in idle_animation:
            loaded_pictures.append(pygame.image.load(pic_name).convert_alpha())
        scaled_width = size  # New width for the scaled image
        scaled_height = size  # New height for the scaled image

        scaled_pictures = []
        for pic in loaded_pictures:
            scaled_pictures.append(pygame.transform.scale(pic, (scaled_width, scaled_height)))
        return scaled_pictures
    
    def get_damage(self):
        return self.damage

    def explode(self):
        pass #we can chain explosion
    
    def update(self) -> None:
        if(self.alive + ALIVE_TIME < pygame.time.get_ticks()):
            self.kill()

        current_time = pygame.time.get_ticks()
        if current_time - self.last_animation_time > self.current_animation_speed:
            self.current_animation_index = (self.current_animation_index + 1) % len(self.current_animation)
            self.image = self.current_animation[self.current_animation_index]
            self.last_animation_time = current_time