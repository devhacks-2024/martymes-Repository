from character import *
from character_frames import *
from var_setup import MAX_DAMAGE_TIME, DEFAULT_ATTACK_WAIT
from player_direction import *
MAX_DAMAGE_TIME = 400
class Player(Character):
    
    def __init__(self, size, speed, hp, starting_pos, idle_animation):
        super().__init__(size, speed, hp, starting_pos, idle_animation)#down up left right
        self.direction = Player_Direction("down")
        self.current_direction = "down"
        self.walking_down = self.render_image( player_down(), size)
        self.walking_up = self.render_image( player_up(), size)
        self.walking_left = self.render_image(player_left(), size)
        self.walking_right = self.render_image(player_right(), size)

        self.attacking_down = self.render_image(player_attack_down(), size)
        self.attacking_up = self.render_image(player_attack_up(), size)
        self.attacking_left = self.render_image(player_attack_left(), size)
        self.attacking_right = self.render_image(player_attack_right(), size)


        self.damage = 25
        self.is_attacking = [False, 0]
        self.finish_attack = False

        # need damage taking stuff to keep track
        self.taking_damage = -MAX_DAMAGE_TIME
        

    def get_damage(self):
        return self.damage
    
    def moveX(self, move):
        if(move < 0):
            self.direction.change_direction("left")
        else:
            self.direction.change_direction("right")
        super().moveX(move)

    def moveY(self, move):
        if(move <= 0):
            self.direction.change_direction("up")
        else:
            self.direction.change_direction("down")
        super().moveY(move)
    
    def attack_state(self):
        self.is_attacking[0] = True
        self.finish_attack = True
        self.is_attacking[1] = pygame.time.get_ticks()

        if(self.direction.get_direction() == "down"):
            self.current_animation = self.attacking_down
        if(self.direction.get_direction() == "up"):
            self.current_animation = self.attacking_up
        if(self.direction.get_direction() == "left"):
            self.current_animation = self.attacking_left
        if(self.direction.get_direction() == "right"):
            self.current_animation = self.attacking_right


    def change_direction(self):
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

    def update(self):
        #dont change state if hes attacking
        if(self.is_attacking[1] + DEFAULT_ATTACK_WAIT < pygame.time.get_ticks()):
            self.is_attacking[0] = False
            if(self.finish_attack):
                self.change_direction()
            self.finish_attack = False

        if(self.direction.get_direction() != self.current_direction and not self.is_attacking[0]):
            self.change_direction()

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