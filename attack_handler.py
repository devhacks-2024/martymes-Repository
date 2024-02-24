from typing import Any
import pygame
from var_setup import player_size
from projectile import*
from damage_area import *
EXPLODE_SIZE = 100
#for the player to attack
class Attack_Handler(pygame.sprite.Sprite):

    def __init__(self, player) -> None:
        self.player_attacks = pygame.sprite.Group()
        self.player = player

    def player_attack(self, time_halted):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p] or keys[pygame.K_SPACE] and not time_halted[0]:

            new_attack = Projectile(self, (self.player.getX() + player_size//2, self.player.getY() + player_size//2), self.player.get_damage() ,self.player.get_direction(), [projectile_down(), projectile_up(), projectile_left(), projectile_right()])
            self.player_attacks.add(new_attack)
            time_halted[1] = pygame.time.get_ticks()
            time_halted[0] = True
            self.player.attack_state()

    def get_attacks(self):
        return self.player_attacks
    
    def explosion(self, start_pos):
        explode = Damage_Area(self.player.get_damage(), start_pos, EXPLODE_SIZE)
        self.player_attacks.add(explode)

    def update(self, screen) -> None:
        self.player_attacks.update()
        self.player_attacks.draw(screen)