import customtkinter
from Game import Login

# inisiasi surface/GUI
app = customtkinter.CTk()
app.resizable(False, False)
app.title('Snake Game Login & Register')
app.geometry('450x400')
app.config(bg='#001220')

# membuat objek login dari kelas Login
login = Login(app)
login.login()

# looping surface/GUI
app.mainloop()
