import customtkinter
import sqlite3
import bcrypt
from tkinter import *
from tkinter import messagebox
from subprocess import run
from sys import exit


# initiate the gui
app = customtkinter.CTk()
app.resizable(False, False)
app.title('Snake Game Login & Register')
app.geometry('450x400')
app.config(bg='#001220')

font1 = ('Helvetica', 25, 'bold')
font2 = ('Arial', 17, 'bold')
font3 = ('Arial', 13, 'bold')
font4 = ('Arial', 13, 'bold', 'underline')


# database
conn = sqlite3.connect('database/data.db')
cursor = conn.cursor()

cursor.execute(
  '''
  CREATE TABLE IF NOT EXISTS users (
    username TEXT NOT NULL,
    password TEXT NOT NULL
  )
  '''
)


def login_account():
  
  username = username_entry.get()
  password = password_entry.get()
  
  if username != '' and password != '':
    cursor.execute('SELECT password FROM users WHERE username=?', [username])
    result = cursor.fetchone()
    if result:
      if bcrypt.checkpw(password.encode('utf-8'), result[0]):
        messagebox.showinfo('Success', 'Logged in successfully.')
        run(['python', 'main-menu.py'])
        exit()
      else:
        messagebox.showerror('Error', 'Invalid password.')
    else:
      messagebox.showerror('Error', 'Invalid username.')
  else:
    messagebox.showerror('Error', 'Enter all data.')

def signup_account():
  
  username = username_entry2.get()
  password = password_entry2.get()
  repeat_password = repeat_password_entry.get()
  
  if username != '' and password != '' and repeat_password != '':
    cursor.execute('SELECT username FROM users WHERE username=?', [username])
    if cursor.fetchone() is not None:
      messagebox.showerror('Error', 'Username already axists.')
    elif password != repeat_password:
      messagebox.showerror('Error', 'Password and repeat password are not the same.')
    else:
      encoded_password = password.encode('utf-8')
      hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
      # print(hashed_password)
      cursor.execute('INSERT INTO users VALUES (?, ?)', [username, hashed_password])
      conn.commit()
      messagebox.showinfo('Success', 'Account has been created.')
  else:
    messagebox.showerror('Error', 'Enter all data.')

def login():
  
  global frame1

  frame2.destroy()
  frame1 = customtkinter.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=470, height=400)
  frame1.place(x=0, y=0)
  
  image1 = PhotoImage(file='img/bg2.png')
  image1_label = Label(frame1, image=image1, bg='#001220')
  image1_label.place(x=0, y=0)
  frame1.image1 = image1

  login_label = customtkinter.CTkLabel(frame1, font=font1, text='Login', text_color='#fff', bg_color='#001220')
  login_label.place(x=290, y=20)
  
  global username_entry
  global password_entry

  username_entry = customtkinter.CTkEntry(frame1, font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Username', placeholder_text_color='#a3a3a3', width=200, height=50)
  username_entry.place(x=230, y=80)

  password_entry = customtkinter.CTkEntry(frame1, font=font2, show='*', text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Password', placeholder_text_color='#a3a3a3', width=200, height=50)
  password_entry.place(x=230, y=150)

  login_button = customtkinter.CTkButton(frame1, command=login_account,font=font2, text_color='#fff', text='Login', fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5, width=120)
  login_button.place(x=230, y=220)

  signup_label = customtkinter.CTkLabel(frame1, font=font3, text="Don't have an account yet?", text_color='#fff', bg_color='#001220')
  signup_label.place(x=230, y=260)

  signup_button = customtkinter.CTkButton(frame1, command=signup, font=font4, text_color='#00bf77', text='Sign up', fg_color='#001220', hover_color='#001220', cursor='hand2', width=40)
  signup_button.place(x=222, y=280)

def signup():
  
  global frame2
  
  frame1.destroy()
  frame2 = customtkinter.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=470, height=400)
  frame2.place(x=0, y=0)
  
  image2 = PhotoImage(file='img/bg2.png')
  image2_label = Label(frame2, image=image2, bg='#001220')
  image2_label.place(x=0, y=0)
  frame2.image2 = image2
  
  signup_label2 = customtkinter.CTkLabel(frame2, font=font1, text='Sign up', text_color='#fff', bg_color='#001220')
  signup_label2.place(x=280, y=20)
  
  global username_entry2
  global password_entry2
  global repeat_password_entry
  
  username_entry2 = customtkinter.CTkEntry(frame2, font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Username', placeholder_text_color='#a3a3a3', width=200, height=50)
  username_entry2.place(x=230, y=80)
  
  password_entry2 = customtkinter.CTkEntry(frame2, font=font2, show='*', text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Password', placeholder_text_color='#a3a3a3', width=200, height=50)
  password_entry2.place(x=230, y=150)
  
  repeat_password_entry = customtkinter.CTkEntry(frame2, font=font2, show='*', text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Repeat password', placeholder_text_color='#a3a3a3', width=200, height=50)
  repeat_password_entry.place(x=230, y=220)
  
  signup_button = customtkinter.CTkButton(frame2, command=signup_account, font=font2, text_color='#fff', text='Sign up', fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5, width=120)
  signup_button.place(x=230, y=290)
  
  login_label2 = customtkinter.CTkLabel(frame2, font=font3, text='Already have an account?', text_color='#fff', bg_color='#001220')
  login_label2.place(x=230, y=330)
  
  login_button2 = customtkinter.CTkButton(frame2, command=login, font=font4, text_color='#00bf77', text='Login', fg_color='#001220', hover_color='#001220', cursor='hand2', width=40)
  login_button2.place(x=395, y=330)


# login page
frame1 = customtkinter.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=470, height=400)
frame1.place(x=0, y=0)

image1 = PhotoImage(file='img/bg2.png')
image1_label = Label(frame1, image=image1, bg='#001220')
image1_label.place(x=0, y=0)

login_label = customtkinter.CTkLabel(frame1, font=font1, text='Login', text_color='#fff', bg_color='#001220')
login_label.place(x=290, y=20)

username_entry = customtkinter.CTkEntry(frame1, font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Username', placeholder_text_color='#a3a3a3', width=200, height=50)
username_entry.place(x=230, y=80)

password_entry = customtkinter.CTkEntry(frame1, font=font2, show='*', text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Password', placeholder_text_color='#a3a3a3', width=200, height=50)
password_entry.place(x=230, y=150)

login_button = customtkinter.CTkButton(frame1, command=login_account,font=font2, text_color='#fff', text='Login', fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5, width=120)
login_button.place(x=230, y=220)

signup_label = customtkinter.CTkLabel(frame1, font=font3, text="Don't have an account yet?", text_color='#fff', bg_color='#001220')
signup_label.place(x=230, y=260)

signup_button = customtkinter.CTkButton(frame1, command=signup, font=font4, text_color='#00bf77', text='Sign up', fg_color='#001220', hover_color='#001220', cursor='hand2', width=40)
signup_button.place(x=222, y=280)


app.mainloop()
