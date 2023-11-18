import bcrypt
from tkinter import messagebox
from subprocess import run
from Game import DBController

class Authentication:
  
  # inisialisasi atribut pada class Authentication
  def __init__(self):
    self.database = DBController()
    self.conn = self.database.get_conn()
    self.cursor = self.database.get_cursor()

  # autentikasi untuk login user
  def login_account(self, username, password):
    if username != '' and password != '':
      self.cursor.execute('SELECT password FROM users WHERE username=?', [username])
      password_result = self.cursor.fetchone()

      if password_result:
        if bcrypt.checkpw(password.encode('utf-8'), password_result[0]):
          self.cursor.execute('UPDATE users SET login_status=1 WHERE username=?', [username])
          self.conn.commit()
          messagebox.showinfo('Success', 'Logged in successfully.')
          run(['python', 'main-menu.py'])
        else:
          messagebox.showerror('Error', 'Invalid password.')
      else:
        messagebox.showerror('Error', 'Invalid username.')

    else:
      messagebox.showerror('Error', 'Enter all data.')

  # autentikasi untuk regiser user
  def signup_account(self, username, password, repeat_password):
    if username != '' and password != '' and repeat_password != '':
      self.cursor.execute('SELECT username FROM users WHERE username=?', [username])

      if self.cursor.fetchone() is not None:
        messagebox.showerror('Error', 'Username already axists.')
      elif password != repeat_password:
        messagebox.showerror('Error', 'Password and repeat password are not the same.')
      else:
        encoded_password = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
        self.cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', [username, hashed_password])
        self.conn.commit()
        self.cursor.execute('INSERT INTO leaderboard (username) VALUES (?)', [username])
        self.conn.commit()
        messagebox.showinfo('Success', 'Account has been created.')

    else:
      messagebox.showerror('Error', 'Enter all data.')
