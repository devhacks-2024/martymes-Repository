# setup item shop assets and whatnot
import pygame
pygame.init()
WHITE = (255, 255, 255)

font = pygame.font.Font(None, 36)

item_1 = pygame.sprite.Sprite()
item_1.image = pygame.image.load("assets/raba.png")
item_1.rect = item_1.image.get_rect()
item_1.rect.center = (900/2 - 136, 500/2 - 100)
num_1 = font.render('1', True, WHITE)
num_1_rect = num_1.get_rect()
num_1_rect.center = (900/2 - 225, 500/2 + 50)

item_2 = pygame.sprite.Sprite()
item_2.image = pygame.image.load("assets/stormsurge.png")
item_2.rect = item_2.image.get_rect()
item_2.rect.center = (900/2, 500/2 - 100)
num_2 = font.render('2', True, WHITE)
num_2_rect = num_2.get_rect()
num_2_rect.center = (900/2, 500/2 + 50)

item_3 = None
num_3 = font.render('3', True, WHITE)
num_3_rect = num_3.get_rect()
num_3_rect.center = (900/2 + 225, 500/2 + 50)

shop_items = pygame.sprite.Group((item_1, item_2))
ITEM_1_BOUGHT = False
ITEM_2_BOUGHT = False
ITEM_3_BOUGHT = False