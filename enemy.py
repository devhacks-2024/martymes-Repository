import random
from character import *
HALT_TIME = 2000


class Enemy(Character):
    def __init__(self, size, speed, hp, starting_position, idle_animation):
        super().__init__(size, speed, hp, starting_position, idle_animation)
        self.player_location_x = 0
        self.player_location_y = 0
        self.current_direction = "down"

        self.halt = [False, 0]

    def player_location(self,x,y):
        self.player_location_x = x
        self.player_location_y = y
    
    def halt_enemy(self):
        self.halt[0] = True
        self.halt[1] = pygame.time.get_ticks()

    def update(self):
        super().update()
        
        if(self.halt[1] + HALT_TIME < pygame.time.get_ticks()):
            self.halt[0] = False

        if(not self.halt[0]):
            #go towards player
            if(self.player_location_y > self.getY()):
                self.moveY(random.uniform(0.5,1))
            else:
                self.moveY(-1*random.uniform(0.5,1))
            if(self.player_location_x > self.getX()):
                self.moveX(random.uniform(0.5,1))
            else:
                self.moveX(-1*random.uniform(0.5,1))
        
