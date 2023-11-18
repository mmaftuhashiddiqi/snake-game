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

cursor.execute('SELECT username FROM users WHERE login_status=1')
user_active = cursor.fetchone()[0]

# aplikasi sama renderring time
isRun = True
tick = 10
score = 0

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
    
    cursor.execute('SELECT score FROM leaderboard WHERE username=?', [user_active])
    high_score = cursor.fetchone()[0]

    if high_score == None or score > high_score:
      # update score
      cursor.execute('UPDATE leaderboard SET score=? WHERE username=?', [score, user_active])
      conn.commit()
    
    # reset tick & score
    tick = 10
    score = 0

    # add mamam
    mamam = Mamam(arena, nama="mamam")
  
  if uler.get_pos() == mamam.get_pos():
    uler.tambah_kotak()
    mamam.ubah_pos()
    # for speed incremet
    score += 1
    if score % 10 == 0:
      # adding tick
      tick += 1  
    print(tick)
    print(score)

  # render
  arena.render(tick) # bikin grid nyee yee, parameter for speed

pygame.quit()
