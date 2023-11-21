from Classes import Box
import pygame

class Snake():

  body = [] # kumpulan objek dari kotak-kotak
  dir_set = {} # key = posisi, valuenya = arah pergeraan

  # inisialisasi atribut pada class Snake
  def __init__(self, arena, start, x_dir=1, y_dir=0, color=(0,150,93)):
    self.arena = arena
    self.start = start
    self.color = color
    self.x_dir = x_dir
    self.y_dir = y_dir
    self.head = Box(arena, start, x_dir, y_dir, color, name="head")
    self.body.append(self.head)

    self.isPause = False

  # getter untuk posisi
  def get_pos(self):
    return self.head.get_pos()
  
  # method untuk menambah kotak pada snake
  def add_box(self):
    tail = self.body[-1]
    tail_x_dir = tail.get_x_dir()
    tail_y_dir = tail.get_y_dir()
    tail_pos = tail.get_pos()
    tail_pos_x = tail_pos[0]
    tail_pos_y = tail_pos[1]

    if tail_x_dir == 1 and tail_y_dir == 0:
      # lagi kekanan
      new_tail = Box(self.arena, (tail_pos_x - 1, tail_pos_y), tail_x_dir, tail_y_dir)
      self.body.append(new_tail)

    elif tail_x_dir == -1 and tail_y_dir == 0:
      # lagi kekiri
      new_tail = Box(self.arena, (tail_pos_x + 1, tail_pos_y), tail_x_dir, tail_y_dir)
      self.body.append(new_tail)

    elif tail_x_dir == 0 and tail_y_dir == 1:
      # lagi kebawah
      new_tail = Box(self.arena, (tail_pos_x, tail_pos_y - 1), tail_x_dir, tail_y_dir)
      self.body.append(new_tail)

    elif tail_x_dir == 0 and tail_y_dir == -1:
      # lagi keatas
      new_tail = Box(self.arena, (tail_pos_x, tail_pos_y + 1), tail_x_dir, tail_y_dir)
      self.body.append(new_tail)

  # method untuk reset panjang snake jika collide
  def reset(self):
    self.head = Box(self.arena, self.start, x_dir=1, color=self.color, name="head")
    self.body = []
    self.body.append(self.head)
    self.dir_set = {}
    self.x_dir = 1
    self.y_dir = 0

  # method untuk mengarahkan snake
  def move (self):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
      self.isPause = not self.isPause

    # jika isPause = True -> pause
    if self.isPause:
      pass
    # jika isPause = False -> unpause
    else:
      if keys[pygame.K_RIGHT]:
        self.x_dir = 1
        self.y_dir = 0
        self.dir_set[self.head.pos] = [self.x_dir, self.y_dir]
      elif keys[pygame.K_LEFT]:
        self.x_dir = -1
        self.y_dir = 0
        self.dir_set[self.head.pos] = [self.x_dir, self.y_dir]
      elif keys[pygame.K_UP]:
        self.y_dir = -1
        self.x_dir = 0
        self.dir_set[self.head.pos] = [self.x_dir, self.y_dir]
      elif keys[pygame.K_DOWN]:
        self.y_dir = 1
        self.x_dir = 0
        self.dir_set[self.head.pos] = [self.x_dir, self.y_dir]

      for index, box in enumerate(self.body):
        box_pos = box.get_pos()
        if box_pos in self.dir_set:
          arah = self.dir_set[box_pos]
          x_dir = arah[0]
          y_dir = arah[1]
          box.move(x_dir, y_dir)
          if index == len(self.body) - 1:
            self.dir_set.pop(box_pos)
        else:
          box.move(box.get_x_dir(), box.get_y_dir())

  # method untuk mendeteksi collide (tabrakan)
  def is_collide(self):
    head_pos = self.head.get_pos()
    is_collide = False
    for index, box in enumerate(self.body):
      if index > 0 and head_pos == box.get_pos():
        is_collide = True
        break

    return is_collide

  # method untuk terus merender atau menggambar ular
  def draw(self):
    for body_member in self.body:
      body_member.draw()
