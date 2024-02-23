import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Movable Square")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the square
square_size = 50
square_color = WHITE
square_x = (SCREEN_WIDTH - square_size) // 2
square_y = (SCREEN_HEIGHT - square_size) // 2
square_speed = 5

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
        square_x -= square_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        square_x += square_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        square_y -= square_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        square_y += square_speed

    # Clear the screen
    screen.fill(BLACK)

    # Draw the square
    pygame.draw.rect(screen, square_color, (square_x, square_y, square_size, square_size))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
