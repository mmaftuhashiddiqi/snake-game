import customtkinter
from Game import MainMenu


# initiate the gui
app = customtkinter.CTk()
def disable_event(): pass
app.protocol("WM_DELETE_WINDOW", disable_event)
app.resizable(False, False)
app.title('Snake Game Main Menu')
app.geometry('450x400')
app.config(bg='#001220')


main_menu = MainMenu(app)
main_menu.main_menu()


app.mainloop()
