import pygame
from Game import Arena, Uler, Mamam, DBController

# initialisasi game
arena = Arena(500, 500, 20, 20)
uler = Uler(arena, (10, 10), arah_x=1)
mamam = Mamam(arena, nama="mamam")

# database
database = DBController()
conn = database.get_conn()
cursor = database.get_cursor()

# aplikasi sama renderring time
isRun = True
tick = 10
banyak_mamam = 0

# main loop
while isRun:
  # user window event
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      isRun = False
  
  # update
  uler.move()

  if uler.is_collide():
    arena.reset_member()
    uler.reset()
    
    # update score
    
    
    # reset tick & banyak mamam
    tick = 10
    banyak_mamam = 0

    # add mamam
    mamam = Mamam(arena, nama="mamam")
  
  if uler.get_pos() == mamam.get_pos():
    uler.tambah_kotak()
    mamam.ubah_pos()
    # for speed incremet
    banyak_mamam += 1
    if banyak_mamam == 10:
      # adding tick
      tick += 1
      banyak_mamam = 0    
    # print(tick)
    # print(banyak_mamam)

  # render
  arena.render(tick) # bikin grid nyee yee, parameter for speed

pygame.quit()
