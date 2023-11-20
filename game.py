import pygame
from Classes import Arena, Snake, Mamam, DBController

# inisialisasi game
arena = Arena(500, 500, 20, 20)
snake = Snake(arena, (10, 10), x_dir=1)
mamam = Mamam(arena, name="mamam")

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
  snake.move()

  # mendeteksi tabrakan (collide)
  if snake.is_collide():
    arena.reset_member()
    snake.reset()
    
    cursor.execute('SELECT score FROM leaderboard WHERE username=?', [user_active])
    high_score = cursor.fetchone()[0]

    # update score jika kondisi terpenuhi
    if high_score == None or score > high_score:
      cursor.execute('UPDATE leaderboard SET score=? WHERE username=?', [score, user_active])
      conn.commit()
    
    # reset tick & score
    tick = 10
    score = 0

    # add mamam
    mamam = Mamam(arena, name="mamam")
  
  if snake.get_pos() == mamam.get_pos():
    snake.add_box()
    mamam.change_pos()
    # speed incremet
    score += 1
    if score % 10 == 0:
      # adding tick
      tick += 1  

  # render
  arena.render(tick)

pygame.quit()
