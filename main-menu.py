import customtkinter
from Classes import MainMenu

# inisiasi surface/GUI
app = customtkinter.CTk()
def disable_event(): pass
app.protocol("WM_DELETE_WINDOW", disable_event)
app.resizable(False, False)
app.title('Snake Game Main Menu')
app.geometry('450x400')
app.config(bg='#001220')

# membuat objek main_menu dari kelas MainMenu
main_menu = MainMenu(app)
main_menu.main_menu()

# looping surface/GUI
app.mainloop()
