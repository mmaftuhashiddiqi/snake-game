import pygame

class Box():
  
  def __init__(self, arena, start_pos, x_dir=0, y_dir=0, color=(0,150,93), name="kotak"):
    self.name = name
    self.pos = start_pos
    self.x_dir = x_dir # arah positif kanan
    self.y_dir = y_dir # arah positif bawah
    self.color = color
    self.surface = arena.get_surface()
    self.width = arena.get_column_distance()
    self.height = arena.get_row_distance()
    self.arena = arena
    arena.assign_member(self)

  def get_pos(self):
    return self.pos
  
  def get_x_dir(self):
    return self.x_dir

  def get_y_dir(self):
    return self.y_dir

  def move(self, x_dir, y_dir):
    self.x_dir = x_dir
    self.y_dir = y_dir
    self.pos = (self.pos[0] + self.x_dir, self.pos[1] + self.y_dir)

    if self.pos[0] == self.arena.get_column_sum():
      self.pos = (0, self.pos[1])
    elif self.pos[0] < 0:
      self.pos = (self.arena.get_column_sum() - 1, self.pos[1])

    if self.pos[1] == self.arena.get_row_sum():
      self.pos = (self.pos[0], 0)
    elif self.pos[1] < 0:
      self.pos = (self.pos[0], self.arena.get_row_sum() - 1)
  
  def draw(self):
    start_x = self.width * self.pos[0]
    start_y = self.height * self.pos[1]
    pygame.draw.rect(self.surface, self.color, (start_x, start_y, self.width, self.height))

  def __repr__(self):
    return self.name
