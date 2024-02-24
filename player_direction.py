class Player_Direction:
    def __init__(self, direction) -> None:
        self.down = False
        self.up = False
        self.left = False
        self.right = False
        self.change_direction(direction)

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