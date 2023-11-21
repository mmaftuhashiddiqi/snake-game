import customtkinter
from PIL import Image
from subprocess import run
from sys import exit
from Classes import DBController

class MainMenu:
  
  # inisialisasi atribut pada class MainMenu
  def __init__(self, app):    
    self.app = app
    
    self.font1 = ('Helvetica', 25, 'bold')
    self.font2 = ('Arial', 17, 'bold')
    self.font3 = ('Arial', 13, 'bold')
    self.font4 = ('Arial', 13, 'bold', 'underline')
    
    self.database = DBController()
  
  # method untuk running game.py jika tombol Play Game ditekan
  def play_game(self):
    run(['python', 'game.py'])

  # method untuk running leaderboard.py jika tombol Leaderboard ditekan
  def leaderboard(self):
    run(['python', 'leaderboard.py'])
  
  # method untuk logout jika tombol Logout ditekan
  def logout(self):
    conn = self.database.get_conn()
    cursor = self.database.get_cursor()
    cursor.execute('UPDATE users SET login_status=0 WHERE login_status=1')
    conn.commit()
    exit()
  
  # method untuk memunculkan GUI main menu
  def main_menu(self):
    frame = customtkinter.CTkFrame(self.app, bg_color='#001220', fg_color='#001220', width=450, height=400)
    frame.place(x=0, y=0)

    image = customtkinter.CTkImage(light_image=Image.open("img/bg2.png"), dark_image=Image.open("img/bg2.png"), size=(205, 400))
    image_label = customtkinter.CTkLabel(frame, image=image, bg_color='#001220', text='')
    image_label.place(x=0, y=0)
    frame.image = image

    play_game_button = customtkinter.CTkButton(frame, command=self.play_game, font=self.font2, text_color='#fff', text='Play Game', fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5, width=130)
    play_game_button.place(x=265, y=150)

    leaderboard_button = customtkinter.CTkButton(frame, command=self.leaderboard, font=self.font2, text_color='#fff', text='Leaderboard', fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5, width=130)
    leaderboard_button.place(x=265, y=190)

    exit_button = customtkinter.CTkButton(frame, command=self.logout, font=self.font2, text_color='#fff', text='Logout', fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5, width=130)
    exit_button.place(x=265, y=230)
