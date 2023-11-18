import pygame
from numpy import random as rnd

class Mamam():
  
  def __init__(self, arena, color=(255, 0, 0), name="mamam"):
    self.name = name
    food_pos_x = rnd.randint(0, arena.get_column_sum() - 1) # mamam position
    food_pos_y = rnd.randint(0, arena.get_row_sum() - 1) # mamam position
    self.pos = (food_pos_x, food_pos_y)
    self.color = color
    self.surface = arena.get_surface()
    self.width = arena.get_column_distance()
    self.height = arena.get_row_distance()
    self.arena = arena
    arena.assign_member(self)
  
  def get_pos(self):
    return self.pos
  
  def change_pos(self):
    food_pos_x = rnd.randint(0, self.arena.get_column_sum() - 1)
    food_pos_y = rnd.randint(0, self.arena.get_row_sum() - 1)
    self.pos = (food_pos_x, food_pos_y)

  def draw(self):
    start_x = self.width * self.pos[0]
    start_y = self.height * self.pos[1]
    pygame.draw.rect(self.surface, self.color, (start_x, start_y, self.width, self.height))

  def __repr__(self):
    return self.name
