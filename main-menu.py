import customtkinter
from tkinter import *
from tkinter import messagebox
from subprocess import run
from sys import exit


# initiate the gui
app = customtkinter.CTk()
app.resizable(False, False)
app.title('Snake Game Main Menu')
app.geometry('450x400')
app.config(bg='#001220')

font1 = ('Helvetica', 25, 'bold')
font2 = ('Arial', 17, 'bold')
font3 = ('Arial', 13, 'bold')
font4 = ('Arial', 13, 'bold', 'underline')


def play_game():
  run(['python', 'game.py'])

def leaderboard():
  pass


# main menu page
frame = customtkinter.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=470, height=400)
frame.place(x=0, y=0)

image = PhotoImage(file='img/bg2.png')
image_label = Label(frame, image=image, bg='#001220')
image_label.place(x=0, y=0)

play_game_button = customtkinter.CTkButton(frame, command=play_game, font=font2, text_color='#fff', text='Play Game', fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5, width=130)
play_game_button.place(x=265, y=150)

leaderboard_button = customtkinter.CTkButton(frame, command=leaderboard, font=font2, text_color='#fff', text='Leaderboard', fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5, width=130)
leaderboard_button.place(x=265, y=190)

exit_button = customtkinter.CTkButton(frame, command=exit, font=font2, text_color='#fff', text='Exit', fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5, width=130)
exit_button.place(x=265, y=230)


app.mainloop()
