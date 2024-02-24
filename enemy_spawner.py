import pygame
import random

from enemy import * 
from var_setup import ENEMY_SIZE, ENEMY_SPEED, ENEMY_HP, SPAWN_RANGE, SCREEN_HEIGHT, SCREEN_WIDTH
from character_frames import player_down

class Enemy_Spawner(pygame.sprite.Sprite):
    def __init__(self) -> None:
        self.enemies = pygame.sprite.Group()
        self.idle_basic_enemy = player_down()
        
    def get_enemies(self):
        return self.enemies

    def create_wave(self, amount, side):
        if(side == "right"):
            start_pos_x = SCREEN_WIDTH + SPAWN_RANGE
        else:
            start_pos_x = SCREEN_WIDTH - SPAWN_RANGE
        for i in range(amount):
            start_pos_y = random.randint(0,SCREEN_HEIGHT)
            speed = random.choice(ENEMY_SPEED)
            enemy = Enemy(ENEMY_SIZE, speed, ENEMY_HP, (start_pos_x,start_pos_y), self.idle_basic_enemy)
            self.enemies.add(enemy)
            
    def update(self, screen):
        self.enemies.update()
        self.enemies.draw(screen)