import pygame
import sys

from character import *
from enemy import *

from player import *
from character_frames import *
from inventory import *
from projectile import *

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
time_halted = [False, 0]
time_wait = 1000

player = Player(player_size, player_speed, (0,0), [player_down(), player_up(), player_left(), player_right()])
the_player = pygame.sprite.Group()
the_player.add(player)

player_attacks = pygame.sprite.Group()#empty

inv_sprite = Inventory((SCREEN_WIDTH/2 + 8,SCREEN_HEIGHT/2 + 170))
inv = pygame.sprite.Group(inv_sprite)

enemies = pygame.sprite.Group()
enemy1 = Enemy(player_size, player_speed-4, (300, 400), player_down())
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
    enemies.update()
    the_player.update()
    inv.update()
    player_attacks.update()

    the_player.draw(screen)
    enemies.draw(screen)
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

    if(not time_halted[0]):
        # Handle player input
        handle_movement(player)
        #Handle player attack
        player_attack(player, player_attacks, time_halted)
        
    else: 
        check_halt(time_halted)

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