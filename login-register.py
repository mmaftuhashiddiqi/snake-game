import customtkinter
from Game import Login


app = customtkinter.CTk()
app.resizable(False, False)
app.title('Snake Game Login & Register')
app.geometry('450x400')
app.config(bg='#001220')


login = Login(app)
login.login()


app.mainloop()
