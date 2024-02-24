import pygame
from character_frames import hp_bar_assets
from player import Player
from var_setup import SCREEN_HEIGHT, SCREEN_WIDTH, INV_HEIGHT_OFFSET, player_hp
class Hp_Bar(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.max_hp = player_hp
    asset_names = hp_bar_assets()

    width = 400
    height = 400

    self.anim_100 = [pygame.transform.scale(pygame.image.load(asset_names[0]).convert_alpha(), (width, height))]
    self.anim_90 = [pygame.transform.scale(pygame.image.load(asset_names[1]).convert_alpha(), (width,height))]
    self.anim_80 = [pygame.transform.scale(pygame.image.load(asset_names[2]).convert_alpha(), (width,height))]
    self.anim_70 = [pygame.transform.scale(pygame.image.load(asset_names[3]).convert_alpha(), (width,height))]
    self.anim_60 = [pygame.transform.scale(pygame.image.load(asset_names[4]).convert_alpha(), (width,height))]
    self.anim_50 = [pygame.transform.scale(pygame.image.load(asset_names[5]).convert_alpha(), (width,height))]
    self.anim_40 = [pygame.transform.scale(pygame.image.load(asset_names[6]).convert_alpha(), (width,height))]
    self.anim_30 = [pygame.transform.scale(pygame.image.load(asset_names[7]).convert_alpha(), (width,height)), pygame.image.load(asset_names[8]).convert_alpha()]
    self.anim_20 = [pygame.transform.scale(pygame.image.load(asset_names[9]).convert_alpha(), (width, height)), pygame.transform.scale(pygame.image.load(asset_names[10]).convert_alpha(), (width, height))]
    self.anim_10 = [pygame.transform.scale(pygame.image.load(asset_names[11]).convert_alpha(), (width, height)), pygame.transform.scale(pygame.image.load(asset_names[12]).convert_alpha(), (width, height))]

    self.anim_time = 0
    self.current_anim = self.anim_100
    self.current_animation_index = 0
    self.current_animation_speed = 100 # Speed of animation change
    self.last_animation_time = pygame.time.get_ticks()

    self.image = self.anim_100[0]
    self.rect = self.image.get_rect()
    self.rect.center = (SCREEN_WIDTH - 1050, SCREEN_HEIGHT - 100)

  def render_image(self, assets, size):
        loaded_pictures = []
        for pic_name in assets:
            loaded_pictures.append(pygame.image.load(pic_name).convert_alpha())
        scaled_width = size  # New width for the scaled image
        scaled_height = size  # New height for the scaled image

        scaled_pictures = []
        for pic in loaded_pictures:
            scaled_pictures.append(pygame.transform.scale(pic, (scaled_width, scaled_height)))

        return scaled_pictures

  def update_hp(self, hp):
    if float(hp)/self.max_hp >= 1:
       self.current_anim = self.anim_100
    if float(hp)/self.max_hp <= 0.9:
       self.current_anim = self.anim_90
    if float(hp)/self.max_hp <= 0.8:
       self.current_anim = self.anim_80
    if float(hp)/self.max_hp <= 0.7:
       self.current_anim = self.anim_70
    if float(hp)/self.max_hp <= 0.6:
       self.current_anim = self.anim_60
    if float(hp)/self.max_hp <= 0.50:
       self.current_anim = self.anim_50
    if float(hp)/self.max_hp <= 0.40:
       self.current_anim = self.anim_40
    if float(hp)/self.max_hp <= 0.30:
       self.current_anim = self.anim_30
    if float(hp)/self.max_hp <= 0.20:
       self.current_anim = self.anim_20
    if float(hp)/self.max_hp <= 0.10:
       self.current_anim = self.anim_10

  def update(self):
      current_time = pygame.time.get_ticks()
      if current_time - self.last_animation_time > self.current_animation_speed:
          self.current_animation_index = (self.current_animation_index + 1) % len(self.current_anim)
          self.image = self.current_anim[self.current_animation_index]
          self.last_animation_time = current_time
          self.last_animation_time = current_time
