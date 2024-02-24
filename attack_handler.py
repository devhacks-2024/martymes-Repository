from typing import Any
import pygame
from var_setup import player_size, EXPLODE_SIZE
from projectile import*
from damage_area import *
import random


#for the player to attack
class Attack_Handler(pygame.sprite.Sprite):

    def __init__(self, player, effect_engine) -> None:
        self.player_attacks = pygame.sprite.Group()
        self.player = player
        self.effect_engine = effect_engine
    def player_attack(self, time_halted):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p] or keys[pygame.K_SPACE] and not time_halted[0]:
            new_attack = Projectile(self, (self.player.getX() + player_size//2, self.player.getY() ), self.player.get_damage() ,self.player.get_direction(), [projectile_down(), projectile_up(), projectile_left(), projectile_right()])
            self.player_attacks.add(new_attack)
            time_halted[1] = pygame.time.get_ticks()
            time_halted[0] = True
            self.player.attack_state()

        
    def player_freeze(self, time_halted, enemies, ability1):
        keys = pygame.key.get_pressed()
        if ((keys[pygame.K_q] or keys[pygame.K_o])and not time_halted[0] and ability1):
            
            time_halted[1] = pygame.time.get_ticks()
            time_halted[0] = True
            self.player.attack_freeze_state(enemies, self.effect_engine)


    def get_attacks(self):
        return self.player_attacks
    
    def explosion(self, start_pos):
        explode = Damage_Area(self.player.get_damage(), start_pos, EXPLODE_SIZE)
        self.player_attacks.add(explode)

    def update(self, screen) -> None:
        self.player_attacks.update()
        self.player_attacks.draw(screen)