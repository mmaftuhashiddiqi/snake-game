import customtkinter
from Game import Leaderboard

# inisiasi surface/GUI
app = customtkinter.CTk()
app.resizable(False, False)
app.title('Snake Game Leaderboard')
app.geometry('450x400')
app.config(bg='#001220')

# membuat objek login dari kelas Leaderboard
leaderboard = Leaderboard(app)
leaderboard.leaderboard()

# looping surface/GUI
app.mainloop()
