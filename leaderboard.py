import customtkinter
from Game import Leaderboard


# initiate the gui
app = customtkinter.CTk()
app.resizable(False, False)
app.title('Snake Game Leaderboard')
app.geometry('450x400')
app.config(bg='#001220')


leaderboard = Leaderboard(app)
leaderboard.leaderboard()


app.mainloop()
