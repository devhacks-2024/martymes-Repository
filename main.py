import pygame
import sys

from character import *
from enemy import *
from inventory import *
from item import *


# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Movable Square")

player_size = 100
player_speed = 5

player = character(player_size, player_speed, (0,0))
the_player = pygame.sprite.Group()
the_player.add(player)

inv = pygame.sprite.Group(Inventory((SCREEN_WIDTH/2 + 8,SCREEN_HEIGHT/2 + 170)))
raba = Item("Rabadon's Deathcap", (SCREEN_WIDTH/2 + 8,SCREEN_HEIGHT/2 + 170), "assets/raba.png", 120, 0, 25)
items = pygame.sprite.Group(raba)

enemies = pygame.sprite.Group()
enemy1 = enemy(player_size, player_speed-4, (300, 400))
enemies.add(enemy1)

def handle_movement():
    global player
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
    the_player.draw(screen)
    enemies.update()
    enemies.draw(screen)
    inv.update()
    inv.draw(screen)
    items.update()
    items.draw(screen)

def enemy_ping(enemies, x, y):
    for e in enemies.sprites():
        if isinstance(e, enemy): 
            e.player_location(x, y)

# Main game loop
running = True
while running:
    #update enemies location of player
    enemy_ping(enemies, player.getX(), player.getY())
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Handle player input
    handle_movement()

    # Draw the square
    draw_sprites()


    #check if touching
    colliding_sprites = pygame.sprite.spritecollide(player, enemies, dokill=True, collided=None)



    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()