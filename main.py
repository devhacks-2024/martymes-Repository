import pygame
import sys

from character import *
from enemy import *

from player import *
from character_frames import *
from inventory import *

from projectile import *

from item import *


# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
INV_HEIGHT_OFFSET = 230
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('DIMENSION OF THE DERANGED DEITY')
bg = pygame.image.load("assets/bg.png").convert()

player_size = 100
player_hp = 100
player_speed = 5
time_halted = [False, 0]
time_wait = 1000



# setup item shop assets and whatnot
font = pygame.font.Font(None, 36)
item_1 = pygame.sprite.Sprite()
item_1.image = pygame.image.load("assets/raba.png").convert_alpha()
item_1.rect = item_1.image.get_rect()
item_1.rect.center = (900/2 - 136, 500/2 - 100)
num_1 = font.render('1', True, WHITE)
num_1_rect = num_1.get_rect()
num_1_rect.center = (900/2 - 225, 500/2 + 50)

item_2 = pygame.sprite.Sprite()
item_2.image = pygame.image.load("assets/stormsurge.png").convert_alpha()
item_2.rect = item_2.image.get_rect()
item_2.rect.center = (900/2, 500/2 - 100)
num_2 = font.render('2', True, WHITE)
num_2_rect = num_2.get_rect()
num_2_rect.center = (900/2, 500/2 + 50)

num_3 = font.render('3', True, WHITE)
num_3_rect = num_3.get_rect()
num_3_rect.center = (900/2 + 225, 500/2 + 50)

shop_items = pygame.sprite.Group((item_1, item_2))
ITEM_1_BOUGHT = False
ITEM_2_BOUGHT = False
ITEM_3_BOUGHT = False

player = Player(player_size, player_speed, player_hp, (0,0), [player_down(), player_up(), player_left(), player_right()])


player_attacks = pygame.sprite.Group()#empty

the_player = pygame.sprite.Group()
the_player.add(player)

inv = pygame.sprite.Group(Inventory((SCREEN_WIDTH/2 + 8,SCREEN_HEIGHT/2 + INV_HEIGHT_OFFSET)))
raba = Item("Rabadon's Deathcap", (SCREEN_WIDTH/2 + 8,SCREEN_HEIGHT/2 + INV_HEIGHT_OFFSET), "assets/raba.png", 120, 0, 25)
stormsurge = Item("Stormsurge", (SCREEN_WIDTH/2 + 8,SCREEN_HEIGHT/2 + INV_HEIGHT_OFFSET), "assets/stormsurge.png" , 90, 0, 10)

enemies = pygame.sprite.Group()
enemy1 = Enemy(player_size, player_speed-4, player_hp, (300, 400), player_down())
enemies.add(enemy1)

def player_attack(player, player_attacks, time_halted):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_p] or keys[pygame.K_SPACE] and not time_halted[0]:

        new_attack = Projectile((player.getX() + player_size//2, player.getY() + player_size//2), player.get_direction(), [projectile_down(), projectile_up(), projectile_left(), projectile_right()])
        player_attacks.add(new_attack)
        time_halted[1] = pygame.time.get_ticks()
        time_halted[0] = True

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

    

def draw_sprites():
    the_player.update()
    player_attacks.update()
    the_player.draw(screen)
    enemies.update()
    enemies.draw(screen)
    inv.update()
    inv.draw(screen)
    player_attacks.draw(screen)

def enemy_ping(enemies, x, y):
    for e in enemies.sprites():
        if isinstance(e, Enemy): 
            e.player_location(x, y)

def check_halt(halt_player):
    if(halt_player[1] + time_wait < pygame.time.get_ticks()):
        halt_player[0] = False


# Main game loop

def draw_shop():
    global ITEM_1_BOUGHT
    global ITEM_2_BOUGHT
    global ITEM_3_BOUGHT
    shop_screen = pygame.display.set_mode((900, 500))
    pygame.display.set_caption('Buy Menu')
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        shop_screen.fill(BLACK)
        if not ITEM_1_BOUGHT:
            shop_screen.blit(num_1, num_1_rect)
        if not ITEM_2_BOUGHT:
            shop_screen.blit(num_2, num_2_rect)
        if not ITEM_3_BOUGHT:
            shop_screen.blit(num_3, num_3_rect)
        shop_items.update()
        shop_items.draw(shop_screen)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            ITEM_1_BOUGHT = True
            inv.add(raba)
            shop_items.remove(item_1)
        elif keys[pygame.K_2]:
            ITEM_2_BOUGHT = True
            inv.add(stormsurge)
            shop_items.remove(item_2)

        pygame.display.flip()
    
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('DIMENSION OF THE DERANGED DEITY')
    screen.blit(bg, (0,0))

collision_timer = 0
running = True
def handle_collision():
    global running
    global collision_timer
    if pygame.sprite.spritecollide(player, enemies, dokill=False, collided=None) and collision_timer==0:
        collision_timer = 50
        player.take_damage(20)
        if(player.get_hp()<0):
            running = False



# Main game loop
while running:
    #update enemies location of player
    enemy_ping(enemies, player.getX(), player.getY())
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screend
    screen.blit(bg, (0,0))
    
    if(not time_halted[0]):
        # Handle player input
        handle_movement(player)
        #Handle player attack
        player_attack(player, player_attacks, time_halted)
    else: 
        check_halt(time_halted)

    # Check if shop opened
    if(pygame.key.get_pressed()[pygame.K_TAB]):
        draw_shop()
    


    # Draw the square
    draw_sprites()

    #check if touching
    if(collision_timer>0):
        collision_timer -= 1
    else:
        handle_collision()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()