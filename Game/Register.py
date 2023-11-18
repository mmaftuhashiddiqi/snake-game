import customtkinter
from tkinter import *
from Game import Authentication, Login

class Register:
  
  def __init__(self, app):

    self.app = app
    
    self.font1 = ('Helvetica', 25, 'bold')
    self.font2 = ('Arial', 17, 'bold')
    self.font3 = ('Arial', 13, 'bold')
    self.font4 = ('Arial', 13, 'bold', 'underline')

    self.auth = Authentication()

  def signup(self):
    
    # frame1.destroy()
    self.frame2 = customtkinter.CTkFrame(self.app, bg_color='#001220', fg_color='#001220', width=470, height=400)
    self.frame2.place(x=0, y=0)
    
    image2 = PhotoImage(file='img/bg2.png')
    image2_label = Label(self.frame2, image=image2, bg='#001220')
    image2_label.place(x=0, y=0)
    self.frame2.image2 = image2
    
    signup_label2 = customtkinter.CTkLabel(self.frame2, font=self.font1, text='Sign up', text_color='#fff', bg_color='#001220')
    signup_label2.place(x=280, y=20)
    
    username_entry2 = customtkinter.CTkEntry(self.frame2, font=self.font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Username', placeholder_text_color='#a3a3a3', width=200, height=50)
    username_entry2.place(x=230, y=80)
    
    password_entry2 = customtkinter.CTkEntry(self.frame2, font=self.font2, show='*', text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Password', placeholder_text_color='#a3a3a3', width=200, height=50)
    password_entry2.place(x=230, y=150)
    
    repeat_password_entry = customtkinter.CTkEntry(self.frame2, font=self.font2, show='*', text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Repeat password', placeholder_text_color='#a3a3a3', width=200, height=50)
    repeat_password_entry.place(x=230, y=220)
    
    signup_button = customtkinter.CTkButton(self.frame2, command=lambda: self.auth.signup_account(username_entry2.get(), password_entry2.get(), repeat_password_entry.get()), font=self.font2, text_color='#fff', text='Sign up', fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5, width=120)
    signup_button.place(x=230, y=290)
    
    login_label2 = customtkinter.CTkLabel(self.frame2, font=self.font3, text='Already have an account?', text_color='#fff', bg_color='#001220')
    login_label2.place(x=230, y=330)
    
    login_button2 = customtkinter.CTkButton(self.frame2, command=Login(self.app).login, font=self.font4, text_color='#00bf77', text='Login', fg_color='#001220', hover_color='#001220', cursor='hand2', width=40)
    login_button2.place(x=395, y=330)
