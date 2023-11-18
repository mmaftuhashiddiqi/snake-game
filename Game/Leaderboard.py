import customtkinter
from tkinter import *
from sys import exit
from Game import DBController

class Leaderboard:
  
  def __init__(self, app):
    
    self.app = app
    
    self.font1 = ('Helvetica', 25, 'bold')
    self.font2 = ('Arial', 17, 'bold')
    self.font3 = ('Arial', 13, 'bold')
    self.font4 = ('Arial', 13, 'bold', 'underline')
    
    self.database = DBController()
  
  def leaderboard(self):
    
    # frame for leaderboard
    frame = customtkinter.CTkScrollableFrame(self.app, bg_color='#001220', fg_color='#001220', width=470, height=400)
    frame.pack(padx=0, pady=0, anchor='center')

    # leaderboard label
    leaderboard_label = customtkinter.CTkLabel(frame, font=self.font1, text='Leaderboard', text_color='#fff', bg_color='#001220')
    leaderboard_label.pack(pady=20)

    cursor = self.database.get_cursor()

    cursor.execute('SELECT * FROM leaderboard ORDER BY score DESC')
    leaderboard_result = cursor.fetchall()

    # looping for data dummies
    for i in range(len(leaderboard_result)):
      customtkinter.CTkLabel(frame, text=f'{i+1}. {leaderboard_result[i][1]}: {leaderboard_result[i][2]}', fg_color='#001a2e', corner_radius=5).pack(pady=5, ipadx=70)

    back_button = customtkinter.CTkButton(frame, command=exit, font=self.font4, text_color='#00bf77', text='<< back to main menu', fg_color='#001220', hover_color='#001220', cursor='hand2', width=40)
    back_button.pack(pady=20)