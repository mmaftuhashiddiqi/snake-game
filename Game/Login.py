import customtkinter
from tkinter import *
from Game import Authentication, Register

class Login:
  
  def __init__(self, app):

    self.app = app
    
    self.font1 = ('Helvetica', 25, 'bold')
    self.font2 = ('Arial', 17, 'bold')
    self.font3 = ('Arial', 13, 'bold')
    self.font4 = ('Arial', 13, 'bold', 'underline')

    self.auth = Authentication()

  def login(self):
    
    # frame2.destroy()
    self.frame1 = customtkinter.CTkFrame(self.app, bg_color='#001220', fg_color='#001220', width=470, height=400)
    self.frame1.place(x=0, y=0)
    
    image1 = PhotoImage(file='img/bg2.png')
    image1_label = Label(self.frame1, image=image1, bg='#001220')
    image1_label.place(x=0, y=0)
    self.frame1.image1 = image1

    login_label = customtkinter.CTkLabel(self.frame1, font=self.font1, text='Login', text_color='#fff', bg_color='#001220')
    login_label.place(x=290, y=20)

    username_entry = customtkinter.CTkEntry(self.frame1, font=self.font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Username', placeholder_text_color='#a3a3a3', width=200, height=50)
    username_entry.place(x=230, y=80)

    password_entry = customtkinter.CTkEntry(self.frame1, font=self.font2, show='*', text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Password', placeholder_text_color='#a3a3a3', width=200, height=50)
    password_entry.place(x=230, y=150)

    login_button = customtkinter.CTkButton(self.frame1, command=lambda: self.auth.login_account(username_entry.get(), password_entry.get()),font=self.font2, text_color='#fff', text='Login', fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5, width=120)
    login_button.place(x=230, y=220)

    signup_label = customtkinter.CTkLabel(self.frame1, font=self.font3, text="Don't have an account yet?", text_color='#fff', bg_color='#001220')
    signup_label.place(x=230, y=260)

    signup_button = customtkinter.CTkButton(self.frame1, command=Register(self.app).signup, font=self.font4, text_color='#00bf77', text='Sign up', fg_color='#001220', hover_color='#001220', cursor='hand2', width=40)
    signup_button.place(x=222, y=280)
