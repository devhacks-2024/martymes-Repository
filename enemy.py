from character import *
class enemy(character):
    def __init__(self, size, speed):
        super().__init__(size, speed)
        self.player_location_x = 0
        self.player_location_y = 0

    def player_location(self,x,y):
        self.player_location_x = x
        self.player_location_y = y

    def update(self):
        super().update()
        
        #go towards player
        if(self.player_location_y > self.getY()):
            self.moveY(1)
        else:
            self.moveY(-1)
        if(self.player_location_x > self.getX()):
            self.moveX(1)
        else:
            self.moveX(-1)
        
