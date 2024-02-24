import pygame

class character(pygame.sprite.Sprite):
    def __init__(self, size, speed):
        super().__init__()
        # Load and scale player images for walking animation
        self.image_walk1 = pygame.image.load("player1.png").convert_alpha()
        self.image_walk2 = pygame.image.load("player2.png").convert_alpha()
        scaled_width = size  # New width for the scaled image
        scaled_height = size  # New height for the scaled image
        self.image_walk1 = pygame.transform.scale(self.image_walk1, (scaled_width, scaled_height))
        self.image_walk2 = pygame.transform.scale(self.image_walk2, (scaled_width, scaled_height))
        
        # Set up initial image and rect
        self.image = self.image_walk1
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)  # Initial position at the center of the screen
        
        # Define size and speed attributes
        self.square_size = size
        self.square_speed = speed
        
        # Walking animation attributes
        self.walk_animation_frames = [self.image_walk1, self.image_walk2]
        self.walk_animation_index = 0
        self.walk_animation_speed = 100 # Speed of animation change
        self.last_animation_time = pygame.time.get_ticks()


        
        
    def moveX(self, move):
        self.rect.x += move * self.square_speed
        
    def moveY(self, move):
        self.rect.y += move * self.square_speed

    def getX(self) -> int:
        return self.rect.x

    def getY(self) -> int:
        return self.rect.y
    
    def get_width(self) -> int:
        return self.rect.width

    def get_height(self) -> int:
        return self.rect.height
        
    def update(self):
        # Update walking animation
        current_time = pygame.time.get_ticks()
        if current_time - self.last_animation_time > self.walk_animation_speed:
            self.walk_animation_index = (self.walk_animation_index + 1) % len(self.walk_animation_frames)
            self.image = self.walk_animation_frames[self.walk_animation_index]
            self.last_animation_time = current_time

        # Tint the image red - for damage
        # red_tint = (255, 0, 0)  # Red color
        # tinted_image = self.image.copy()  # Make a copy of the original image
        # tinted_image.fill(red_tint, special_flags=pygame.BLEND_MULT)  # Tint the copied image red
        # self.image = tinted_image

