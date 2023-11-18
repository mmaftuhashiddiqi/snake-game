import pygame

class Arena():

  # inisialisasi atribut pada class Arena
  def __init__(self, arena_width, arena_height, row_sum, column_sum):
    pygame.init()
    self.arena_width = arena_width
    self.arena_height = arena_height
    self.row_sum = row_sum
    self.column_sum = column_sum
    self.row_distance = self.arena_width // self.row_sum
    self.column_distance = self.arena_height // self.column_sum
    self.clock = pygame.time.Clock()
    self.objects = []
  
    self.surface = pygame.display.set_mode((self.arena_width, self.arena_height))

  # method untuk assign member objek-objek seperti box dan mamam pada objek arena
  def assign_member(self, member):
    self.objects.append(member)
  
  # method untuk reset member seperti box dan mamam yang sebelumnya telah di assign member
  def reset_member(self):
    self.objects = []

  # getter untuk surface (gui)
  def get_surface(self):
    return self.surface
  
  # getter untuk jarak baris
  def get_row_distance(self):
    return self.row_distance
  
  # getter untuk jarak kolom
  def get_column_distance(self):
    return self.column_distance
  
  # getter untuk jumlah kolom
  def get_column_sum(self):
    return self.column_sum

  # getter untuk jumlah baris
  def get_row_sum(self):
    return self.row_sum

  # method draw grid untuk merender grid pada surface
  def draw_grid(self):
    for row_to in range(self.row_sum):
      x = self.row_distance * row_to
      y = self.column_distance * row_to
      pygame.draw.line(self.surface, (0, 0, 0), (x, 0), (x, self.arena_height))
      pygame.draw.line(self.surface, (0, 0, 0), (0, y), (self.arena_width, y))
  
  # method render untuk merender surface
  def render(self, tick):
    self.surface.fill((0, 18, 32)) # agar surface berwarna biru
    for obj in self.objects:
      obj.draw() # gambar objek-objeknya

    self.draw_grid()
    pygame.display.update()

    # timing
    pygame.time.delay(50) # delay
    self.clock.tick(tick) # satuan clock
