import pygame
from character_frames import hp_bar_assets
from player import Player
from var_setup import SCREEN_HEIGHT, SCREEN_WIDTH, INV_HEIGHT_OFFSET, player_hp
class Hp_Bar(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.max_hp = player_hp
    asset_names = hp_bar_assets()

    self.anim_100 = [pygame.image.load(asset_names[0]).convert_alpha()]
    self.anim_90 = [pygame.image.load(asset_names[1]).convert_alpha()]
    self.anim_80 = [pygame.image.load(asset_names[2]).convert_alpha()]
    self.anim_70 = [pygame.image.load(asset_names[3]).convert_alpha()]
    self.anim_60 = [pygame.image.load(asset_names[4]).convert_alpha()]
    self.anim_50 = [pygame.image.load(asset_names[5]).convert_alpha()]
    self.anim_40 = [pygame.image.load(asset_names[6]).convert_alpha()]
    self.anim_30 = [pygame.image.load(asset_names[7]).convert_alpha(), pygame.image.load(asset_names[8]).convert_alpha()]
    self.anim_20 = [pygame.image.load(asset_names[9]).convert_alpha(), pygame.image.load(asset_names[10]).convert_alpha()]
    self.anim_10 = [pygame.image.load(asset_names[11]).convert_alpha(), pygame.image.load(asset_names[12]).convert_alpha()]

    self.anim_time = 0
    self.current_anim = self.anim_100
    self.current_animation_index = 0
    self.current_animation_speed = 100 # Speed of animation change
    self.last_animation_time = pygame.time.get_ticks()

    self.image = self.anim_100[0]
    self.rect = self.image.get_rect()
    self.rect.center = (SCREEN_WIDTH/2 + 8,SCREEN_HEIGHT/2 + INV_HEIGHT_OFFSET)

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
