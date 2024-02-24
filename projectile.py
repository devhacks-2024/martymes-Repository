import pygame
from character import *
from character_frames import *
from damage_area import *

class Projectile(Character):
    
    def __init__(self, attack_handler, start_pos, damage, direction, animations) -> None:
        self.size = 100
        self.speed = 5
        self.direction = direction
        self.attack_handler = attack_handler
        animation = self.projectile_direction(direction, animations)#down up left right
        super().__init__(self.size, self.speed, 0, start_pos, animation)
        self.rect.topright = start_pos

        self.damage = damage
        self.current_animation_speed = 500
        self.alive_time = 0
   
    def get_damage(self):
        return self.damage
    
    def projectile_direction(self, direction, animations):
        if(direction == "down"):
            return projectile_down()
        if(direction == "up"):
            return  projectile_up()
        if(direction == "left"):
            return projectile_left()
        if(direction == "right"):
            return projectile_right()
        
    def explode(self):
        self.attack_handler.explosion((self.getX(), self.getY()))
        self.kill()

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
            self.current_animation_index = (self.current_animation_index + 1) % len(self.current_animation)
            self.image = self.current_animation[self.current_animation_index]
            self.last_animation_time = current_time

        if(self.alive_time + 1 > len(self.current_animation)):

            #maybe call a finish animation function to be overwritten
            self.kill()