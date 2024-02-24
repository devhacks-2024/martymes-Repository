from character import *
MAX_DAMAGE_TIME = 400
class Player(Character):
    
    def __init__(self, size, speed, hp, starting_pos, idle_animation):
        super().__init__(size, speed, hp, starting_pos, idle_animation[0])#down up left right
        self.direction = Player_Direction()
        self.current_direction = "down"
        self.walking_down = self.render_image( idle_animation[0], size)
        self.walking_up = self.render_image(idle_animation[1], size)
        self.walking_left = self.render_image(idle_animation[2], size)
        self.walking_right = self.render_image(idle_animation[3], size)

        # need damage taking stuff to keep track
        self.taking_damage = -MAX_DAMAGE_TIME
        

    def moveX(self, move):
        if(move <= 0):
            self.direction.change_direction("right")
        else:
            self.direction.change_direction("left")
        super().moveX(move)

    def moveY(self, move):
        if(move <= 0):
            self.direction.change_direction("up")
        else:
            self.direction.change_direction("down")
        super().moveY(move)

    
    def update(self):
        if(self.direction.get_direction() != self.current_direction):
            if(self.direction.get_direction() == "down"):
                self.current_animation = self.walking_down
                self.current_direction = "down"
            if(self.direction.get_direction() == "up"):
                self.current_animation = self.walking_up
                self.current_direction = "up"
            if(self.direction.get_direction() == "left"):
                self.current_animation = self.walking_left
                self.current_direction = "left"
            if(self.direction.get_direction() == "right"):
                self.current_animation = self.walking_right
                self.current_direction = "right"

        current_time = pygame.time.get_ticks()
        if current_time - self.last_animation_time > self.current_animation_speed:
            self.current_animation_index = (self.current_animation_index + 1) % len(self.current_animation)
            self.image = self.current_animation[self.current_animation_index]

            if self.taking_damage + MAX_DAMAGE_TIME > pygame.time.get_ticks():
                red_tint = (255, 0, 0)  # Red color
                tinted_image = self.image.copy()  # Make a copy of the original image
                tinted_image.fill(red_tint, special_flags=pygame.BLEND_MULT)  # Tint the copied image red
                self.image = tinted_image
            
            self.last_animation_time = current_time

class Player_Direction:
    def __init__(self) -> None:
        self.down = True
        self.up = False
        self.left = False
        self.right = False

    def change_direction(self, direction):
        self.down = False
        self.up = False
        self.left = False
        self.right = False

        if(direction == "down"):
            self.down = True
        if(direction == "up"):
            self.up = True
        if(direction == "left"):
            self.left = True
        if(direction == "right"):
            self.right = True

    def get_direction(self):
        if(self.down):
            return "down" 
        if(self.up):
            return "up" 
        if(self.left):
            return "left" 
        if(self.right):
            return "right" 