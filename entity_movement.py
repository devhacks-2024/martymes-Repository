import pygame
from main import SCREEN_WIDTH, SCREEN_HEIGHT, player_size
from enemy import Enemy
from projectile import Projectile
from character_frames import *

pygame.init()

time_wait = 1000

def handle_movement(player):
    keys = pygame.key.get_pressed()
    if  player.getX() > 0:
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.moveX(-1)
    if player.getX() < SCREEN_WIDTH - player.get_width():
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.moveX(1)
    if player.getY() > 0:
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.moveY(-1)
    if player.getY() < SCREEN_HEIGHT - player.get_height():
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.moveY(1)

def enemy_ping(enemies, x, y):
    for e in enemies.sprites():
        if isinstance(e, Enemy): 
            e.player_location(x, y)

def check_halt(halt_player):
    if(halt_player[1] + time_wait < pygame.time.get_ticks()):
        halt_player[0] = False

def player_attack(player, player_attacks, time_halted):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_p] or keys[pygame.K_SPACE] and not time_halted[0]:

        new_attack = Projectile((player.getX() + player_size//2, player.getY() + player_size//2), player.get_direction(), [projectile_down(), projectile_up(), projectile_left(), projectile_right()])
        player_attacks.add(new_attack)
        time_halted[1] = pygame.time.get_ticks()
        time_halted[0] = True