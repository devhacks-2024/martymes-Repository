import pygame
import random

from player import Player
from var_setup import *
from effect_engine import Effect_Engine
from item import Item
from character_frames import *
from inventory import Inventory
from enemy import Enemy
from enemy_spawner import Enemy_Spawner
from small_enemy import Small_Enemy
from hp_bar import Hp_Bar

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('DIMENSION OF THE DERANGED DEITY')
bg = pygame.image.load("assets/bg.png").convert()

player = Player(player_size, player_speed, player_hp, (0,0), player_down())
player_attacks = pygame.sprite.Group()#empty

the_player = pygame.sprite.Group()
the_player.add(player)

effect_engine = Effect_Engine()

inv = pygame.sprite.Group(Inventory((SCREEN_WIDTH/2 + 8,SCREEN_HEIGHT/2 + INV_HEIGHT_OFFSET)))
raba = Item("Rabadon's Deathcap", (SCREEN_WIDTH/2 + 8,SCREEN_HEIGHT/2 + INV_HEIGHT_OFFSET), "assets/raba.png", 120, 0, 25)
stormsurge = Item("Stormsurge", (SCREEN_WIDTH/2 + 8,SCREEN_HEIGHT/2 + INV_HEIGHT_OFFSET), "assets/stormsurge.png" , 90, 0, 10)
youmuus = Item("Youmuu's", (SCREEN_WIDTH/2 + 168,SCREEN_HEIGHT/2 + INV_HEIGHT_OFFSET), "assets/youmuus.png", 0, 60, 0)

hp_bar = Hp_Bar()
hp_bar_sprite = pygame.sprite.Group(hp_bar)

enemy_handler = Enemy_Spawner()
enemy_handler.create_wave(15, "right")
# enemies = pygame.sprite.Group()
# enemy1 = Enemy(player_size, random.randint(1, player_speed-2), player_hp, (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)), player_down())
# ghoul = Small_Enemy(player_size, random.randint(2,player_speed-1), 20, (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)), [ghoul_right(), ghoul_left()])
# enemies.add(enemy1)
# enemies.add(ghoul)