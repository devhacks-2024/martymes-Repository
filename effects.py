from typing import Any
import pygame

class Effects(pygame.sprite.Sprite):
    def __init__(self, starting_pos, speed, animations_frames) -> None:
        super().__init__()
        #initialization
        self.current_animation = animations_frames
        self.last_animation_time = pygame.time.get_ticks()
        self.current_animation_index = 0
        self.current_animation_speed = speed
        self.alive_time = 0

        #so it spawns in
        self.image = animations_frames[0]
        self.rect = self.image.get_rect() #sets the hit box of the sprite
        self.rect.center = starting_pos # Initial the position 

    def update(self) -> None:      
        current_time = pygame.time.get_ticks()
        if current_time - self.last_animation_time > self.current_animation_speed:
            self.alive_time = self.alive_time + 1
            self.current_animation_index = (self.current_animation_index + 1) % len(self.current_animation)
            self.image = self.current_animation[self.current_animation_index]
            self.last_animation_time = current_time

        #so the animation dies when it finishes    
        if(self.alive_time + 1 > len(self.current_animation)):
            self.kill()