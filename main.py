import pygame
import sys

from character import *

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
player = character(player_size, player_speed)


enemy = character(player_size, player_speed-2)


#create a sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)


# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.moveX(-1)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.moveX(1)
    if keys[pygame.K_UP] or keys[pygame.K_w]:
       player.moveY(-1)
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.moveY(1)

    # Clear the screen
    screen.fill(BLACK)

    # Draw the square
    all_sprites.update()
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
