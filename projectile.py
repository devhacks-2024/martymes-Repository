import pygame
from character import *

class Projectile(Character):
    
    def __init__(self, start_pos, direction, animations) -> None:
        self.size = 100
        self.speed = 5
        self.direction = direction
        animation = self.projectile_direction(direction, animations)#down up left right

        super().__init__(self.size, self.speed, 0, start_pos, animation)
        
        self.current_animation_speed = 500
        self.alive_time = 0
   
    
    def projectile_direction(self, direction, animations):
        if(direction == "down"):
            return animations[0]
        if(direction == "up"):
            return animations[1]
        if(direction == "left"):
            return animations[2]
        if(direction == "right"):
            return animations[3]
        
    def update(self):
        current_time = pygame.time.get_ticks()

            
        if(self.direction == "down"):
            self.moveY(1)
        if(self.direction == "up"):
            self.moveY(-1)
        if(self.direction == "right"):
            self.moveX(1)
        if(self.direction == "left"):
            self.moveX(-1)

        if current_time - self.last_animation_time > self.current_animation_speed:
            
            self.alive_time = self.alive_time + 1
            print(self.alive_time)
            self.current_animation_index = (self.current_animation_index + 1) % len(self.current_animation)
            self.image = self.current_animation[self.current_animation_index]
            self.last_animation_time = current_time

        if(self.alive_time + 1 > len(self.current_animation)):
            self.kill()
   
    