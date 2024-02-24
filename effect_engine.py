from typing import Any
import pygame
from character_frames import *
from effects import *


class Effect_Engine(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.enemy_death_animation = enemy_death() 
        enemy_death_animation_size = 250
        self.enemy_death_animation = self.render_image(self.enemy_death_animation, enemy_death_animation_size)#size
        
        
        self.bone_effect_animation = freeze_effect()
        bone_effect_size = 100
        self.bone_effect_animation = self.render_image(self.bone_effect_animation, bone_effect_size)
        
        self.current_effects = pygame.sprite.Group()
        #create group

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
    

    def enemy_death(self, start_pos):
        death_animation_speed = 150
        death_animation = Effects(start_pos, death_animation_speed, self.enemy_death_animation)
        self.current_effects.add(death_animation)

    def bone_effect(self, start_pos):
        bone_animation_speed = 200
        bone_animation = Effects(start_pos, bone_animation_speed, self.bone_effect_animation)
        self.current_effects.add(bone_animation)

    def update(self, screen) -> None:
        self.current_effects.update()
        self.current_effects.draw(screen)