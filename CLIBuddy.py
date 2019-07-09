from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

class CLIBuddy:
    def __init__(self, master):
        self.master = master
        master.title("CLI-Buddy")

        self.combo = ttk.Combobox(master, width=75)
        self.combo.set('Enter key words related to your command here. (Type \"all\" to see all commands)')
        self.img = ImageTk.PhotoImage(Image.open("CLI-Buddy/Logo.png"))
        self.label2 = Label(master, image=self.img, borderwidth=0, highlightthickness=0)

        # LAYOUT

        self.combo.place(x=30, y=40)
        self.label2.place(x=60,y=150)

    #     self.greet_button = Button(master, text="Greet", command=self.greet)
    #     self.greet_button.pack()

    # self.close_button = Button(master, text="Close", command=master.quit)
    # self.close_button.pack()

    # def greet(self):
    #     print("Greetings!")


root = Tk()
root.geometry('600x400')
root.resizable(False, False)
root.configure(bg = "#b3fbc8")
my_gui = CLIBuddy(root)
root.mainloop()
