import sqlite3

class DBController:
  
  # inisialisasi atribut pada class DBController
  def __init__(self):
    self.conn = sqlite3.connect('database/data.db')
    self.cursor = self.conn.cursor()

    self.cursor.execute(
      '''
        CREATE TABLE IF NOT EXISTS users (
          user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          username TEXT NOT NULL,
          password TEXT NOT NULL,
          login_status INT DEFAULT 0
        )
      '''
    )

    self.cursor.execute(
      '''
        CREATE TABLE IF NOT EXISTS leaderboard (
          leaderboard_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          username TEXT,
          score INTEGER,
          FOREIGN KEY (username) REFERENCES users(username)
        )
      '''
    )
    
  # getter untuk connection database
  def get_conn(self):
    return self.conn
  
  # getter untuk cursor (untuk mengeksekusi perintah SQL)
  def get_cursor(self):
    return self.cursor
