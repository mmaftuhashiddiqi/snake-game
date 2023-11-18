import sqlite3

class DBController:
  
  def __init__(self):

    self.conn = sqlite3.connect('database/data.db')
    self.cursor = self.conn.cursor()

    self.cursor.execute(
      '''
        CREATE TABLE IF NOT EXISTS users (
          user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          username TEXT NOT NULL,
          password TEXT NOT NULL
        )
      '''
    )

    self.cursor.execute(
      '''
        CREATE TABLE IF NOT EXISTS leaderboard (
          leaderboard_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          user_id INTEGER,
          score INTEGER,
          FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
      '''
    )
    
  def get_conn(self):
    return self.conn
  
  def get_cursor(self):
    return self.cursor
