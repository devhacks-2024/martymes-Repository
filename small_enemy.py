from enemy import Enemy
from player_direction import *
class Small_Enemy(Enemy):
  def __init__(self, size, speed, hp, starting_position, idle_animation):
    super().__init__(size, speed, hp, starting_position, idle_animation[0])
    
    self.walking_right = self.render_image(idle_animation[0], size)
    self.walking_left = self.render_image(idle_animation[1], size)
    self.direction = Player_Direction("right")
    self.current_direction = "right"

  def update(self):
    super().update()

    if(self.direction.get_direction() != self.current_direction):
      if(self.direction.get_direction() == "left"):
        self.current_animation = self.walking_left
        self.current_direction = "left"
      if(self.direction.get_direction() == "right"):
        self.current_animation = self.walking_right
        self.current_direction = "right"