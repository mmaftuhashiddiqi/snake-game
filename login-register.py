import customtkinter
from tkinter import *
from Game import Authentication, Register


app = customtkinter.CTk()
app.resizable(False, False)
app.title('Snake Game Login & Register')
app.geometry('450x400')
app.config(bg='#001220')

font1 = ('Helvetica', 25, 'bold')
font2 = ('Arial', 17, 'bold')
font3 = ('Arial', 13, 'bold')
font4 = ('Arial', 13, 'bold', 'underline')


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

login_button = customtkinter.CTkButton(frame1, command=lambda: Authentication().login_account(username_entry.get(), password_entry.get()),font=font2, text_color='#fff', text='Login', fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5, width=120)
login_button.place(x=230, y=220)

signup_label = customtkinter.CTkLabel(frame1, font=font3, text="Don't have an account yet?", text_color='#fff', bg_color='#001220')
signup_label.place(x=230, y=260)

signup_button = customtkinter.CTkButton(frame1, command=Register(app).signup, font=font4, text_color='#00bf77', text='Sign up', fg_color='#001220', hover_color='#001220', cursor='hand2', width=40)
signup_button.place(x=222, y=280)


app.mainloop()
