import pygame
import sys
import random

from character import *
from enemy import *
from small_enemy import *

from player import *
from character_frames import *
from inventory import *
from projectile import *
from item import *
from effect_engine import *
from shop_setup import *
from entity_movement import *
from var_setup import *
from enemy_spawner import *
from entity_setup import *


# Initialize Pygame
pygame.init()

def draw_sprites():
    the_player.update()
    attack_handler.update(screen)
    the_player.draw(screen)

    enemy_handler.update(screen)
    effect_engine.update(screen)
    inv.update()
    hp_bar_sprite.update()

    inv.draw(screen)

    hp_bar_sprite.draw(screen)

    
def draw_shop():
    global ITEM_1_BOUGHT
    global ITEM_2_BOUGHT
    global ITEM_3_BOUGHT
    shop_screen = pygame.display.set_mode((900, 500))
    pygame.display.set_caption('Buy Menu')

    
    
    running = True
    while running:
        shop_screen.fill(BLACK)
        points = font.render("Points: "+str(player.get_points()), True, WHITE)
        points_rect = points.get_rect()
        points_rect.center = (700, 450)
        shop_screen.blit(points, points_rect)
        if not ITEM_1_BOUGHT:
            shop_screen.blit(num_1, num_1_rect)
        if not ITEM_2_BOUGHT:
            shop_screen.blit(num_2, num_2_rect)
        if not ITEM_3_BOUGHT:
            shop_screen.blit(num_3, num_3_rect)
        shop_items.update()
        shop_items.draw(shop_screen)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    running = False
                elif event.key == pygame.K_1 and player.get_points()>=15:
                    player.remove_points(15)
                    ITEM_1_BOUGHT = True
                    inv.add(raba)
                    shop_items.remove(item_1)
                elif event.key == pygame.K_2 and player.get_points()>=30:
                    player.remove_points(30)
                    ITEM_2_BOUGHT = True
                    inv.add(stormsurge)
                    shop_items.remove(item_2)
                elif event.key == pygame.K_3 and player.get_points()>=40:
                    player.remove_points(40)
                    ITEM_3_BOUGHT = True
                    inv.add(youmuus)
                    shop_items.remove(item_3)
            elif event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        pygame.time.Clock().tick(60)
    
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('DIMENSION OF THE DERANGED DEITY')
    screen.blit(bg, (0,0))
    pygame.display.flip()

def draw_loss_screen():
    loss_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('You lose trashy')

    screenL2.update()
    screenL2.draw(loss_screen)
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
def draw_win_screen():
    win_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('You win lololololololololololol')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screenW2.update()
        screenW2.draw(win_screen)
        pygame.display.flip()

def draw_start_screen() -> bool:
    start = True
    start_screen = pygame.display.set_mode((512, 512))
    pygame.display.set_caption('why play, press enter to start')

    screenS2.update()
    screenS2.draw(start_screen)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
            if event.type == pygame.QUIT:
                start = False
                running = False

    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('DIMENSION OF THE DERANGED DEITY')
    screen.blit(bg, (0,0))
    pygame.display.flip()
    return start

running = draw_start_screen()
# Main game loop
while running:
    #update enemies location of player
    enemy_ping(enemy_handler.get_enemies(), player.getX(), player.getY())
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                draw_shop()

    # Clear the screen
    screen.blit(bg, (0,0))
    
    if(not time_halted[0]):
        # Handle player input
        handle_movement(player)
        #Handle player attack
        attack_handler.player_attack(time_halted)
        attack_handler.player_freeze(time_halted, enemy_handler.get_enemies(), inv.has(raba))
    else: 
        check_halt(time_halted)
    # Draw the square
    draw_sprites()

    #check if touching only if user has not quit
    if running:
        running = handle_player_collision(player, hp_bar, enemy_handler.get_enemies())
        if not running:
            draw_loss_screen()

    #check if attack touch enemy
    collisions = pygame.sprite.groupcollide(attack_handler.get_attacks(), enemy_handler.get_enemies(), False, False)
    for attack_projectile, colliding_sprites in collisions.items():
        for the_enemy in colliding_sprites:
            attack_projectile.explode()

            the_enemy.take_damage(attack_projectile.get_damage())
            if(the_enemy.is_dead()):
                player.add_point()
                #player size is the_enemy bc same sprite
                effect_engine.enemy_death((the_enemy.getX() + player_size//2, the_enemy.getY()+ player_size//2))


    #pushing the enemies so no collisions
    collisions = pygame.sprite.groupcollide(enemy_handler.get_enemies(), enemy_handler.get_enemies(), False, False)
    for the_enemy1, colliding_sprites in collisions.items():
        for the_enemy2 in colliding_sprites:
            if(the_enemy1 != the_enemy2):
                if(the_enemy1.getX() > the_enemy2.getX()):
                    the_enemy1.moveX(1)
                else:
                    the_enemy1.moveX(-1)
                if(the_enemy1.getY() > the_enemy2.getY()):
                    the_enemy1.moveY(1)
                else:
                    the_enemy1.moveY(-1)

                #funny movement lol
                # the_enemy1.moveX(random.uniform(-3.0, 3.0))
                # the_enemy1.moveY(random.uniform(-3.0, 3.0))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()