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

from attack_handler import*

from hp_bar import Hp_Bar


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('DIMENSION OF THE DERANGED DEITY')
bg = pygame.image.load("assets/bg.png").convert()

# Loss and win screens
screenL = pygame.sprite.Sprite()
screenL.image = pygame.image.load("assets/loss_screen.png")
screenL.rect = screenL.image.get_rect()

screenL2 = pygame.sprite.Group(screenL)

screenW = pygame.sprite.Sprite()
screenW.image = pygame.image.load("assets/win_screen.png")
screenW.rect = screenW.image.get_rect()

screenW2 = pygame.sprite.Group(screenW)

screenS = pygame.sprite.Sprite()
screenS.image = pygame.image.load("assets/start_screen.png")
screenS.rect = screenS.image.get_rect()

screenS2 = pygame.sprite.Group(screenS)

player = Player(player_size, player_speed, player_hp, (0,0), player_down())

the_player = pygame.sprite.Group()
the_player.add(player)

attack_handler = Attack_Handler(player)

effect_engine = Effect_Engine()

inv = Inventory((SCREEN_WIDTH/2 + 8,SCREEN_HEIGHT/2 + INV_HEIGHT_OFFSET))
inv_sprite = pygame.sprite.Group(inv)
raba = Item("Rabadon's Deathcap", (SCREEN_WIDTH/2 + 8,SCREEN_HEIGHT/2 + INV_HEIGHT_OFFSET), "assets/raba.png")
stormsurge = Item("Stormsurge", (SCREEN_WIDTH/2 + 8,SCREEN_HEIGHT/2 + INV_HEIGHT_OFFSET), "assets/stormsurge.png")
youmuus = Item("Youmuu's", (SCREEN_WIDTH/2 + 168,SCREEN_HEIGHT/2 + INV_HEIGHT_OFFSET), "assets/youmuus.png")

hp_bar = Hp_Bar()
hp_bar_sprite = pygame.sprite.Group(hp_bar)

enemy_handler = Enemy_Spawner()
enemy_handler.create_wave(15, "right")
# enemies = pygame.sprite.Group()
# enemy1 = Enemy(player_size, random.randint(1, player_speed-2), player_hp, (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)), player_down())
# ghoul = Small_Enemy(player_size, random.randint(2,player_speed-1), 20, (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)), [ghoul_right(), ghoul_left()])
# enemies.add(enemy1)
# enemies.add(ghoul)