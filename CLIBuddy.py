import tkinter
from tkinter import ttk, messagebox
from tkinter import *
from PIL import ImageTk, Image
from pymongo import MongoClient
import subprocess

root = Tk()

class CLIBuddy:

    def __init__(self, master):
        # configure window properties
        self.master = master
        master.title("CLI-Buddy")
        ttk.Style().theme_use('clam')

        self.values = []

        # establish connection to MongoDB instance (NOTE: you will need to specify your own instance here)
        self.client = MongoClient("<<Insert Connection URI here>>")
        self.db = self.client.command_db

        # configure the properties of each widget
        self.combo = ttk.Combobox(
            master,
            width=75,
            values=self.values,
            height=20,
            postcommand=self.find_commands,
        )
        self.combo.bind('<Return>', lambda event : self.combo.event_generate("<Down>"))
        self.combo.bind('<<ComboboxSelected>>', self.display_man_page)

        self.img = ImageTk.PhotoImage(Image.open("CLI-Buddy/Logo.png"))
        self.logo = Label(master, image=self.img, borderwidth=0, highlightthickness=0)

        self.clear_button = ttk.Button(text='Clear Text', command=self.clear_text)

        self.info_button = ttk.Button(text='Info About CLI-Buddy', command=self.display_info)

        self.quit_button = ttk.Button(text='Quit', command=lambda: sys.exit())

        self.message_label = Label(
            text='Enter key words related to your command here. (Leave it empty to see all commands)',
            bg="#b3fbc8",
            font='Helvetica 11 bold'
        )

        # set the layout of each widget
        self.combo.place(x=30, y=40)
        self.logo.place(x=60, y=150)
        self.clear_button.place(x=225, y=350)
        self.info_button.place(x=370, y=350)
        self.quit_button.place(x=80, y=350)
        self.message_label.place(x=25, y=20)
    
    # clear text in Combobox when button is selected
    def clear_text(self):
        self.combo.set('')
    
    # take the user's entry and find the list of matching commands in the database,
    # update the list of values in the Combobox
    def find_commands(self):
        self.values = []
        double_quoted = False
        single_quoted = False

        # determine if user has quoted expression, quit if not properly quoted
        if self.combo.get().startswith("\"") or self.combo.get().endswith("\""):
            if not (self.combo.get().startswith("\"") and self.combo.get().endswith("\"")):
                messagebox.showerror("Error", "Missing double quotation!")
                self.combo['values'] = self.values
                return
            double_quoted = True
        elif self.combo.get().startswith("'") or self.combo.get().endswith("'"):
            if not (self.combo.get().startswith("'") and self.combo.get().endswith("'")):
                messagebox.showerror("Error", "Missing single quotation!")
                self.combo['values'] = self.values
                return
            single_quoted = True

        # search for entire string if quoted, search for each word otherwise
        if double_quoted:
            keyword_string = self.combo.get().strip("\"")
            self.update_values(keyword_string)
        elif single_quoted:
            keyword_string = self.combo.get().strip("'")
            self.update_values(keyword_string)
        else:
            keywords = self.combo.get().split(" ")
            for word in keywords:
                self.update_values(word)

        self.values.sort()
        self.combo['values'] = self.values

    # given a string, find all commands in the database that contain it, and add them to the
    # list of values in the Combobox if they have not already been added
    def update_values(self, word):
        command_query = { "command": { "$regex": ".*{}.*".format(word)}}
        matched_commands = self.db.commands.find(command_query)
        for matched_command in matched_commands:
            if matched_command.get('command') not in self.values:
                self.values.append(matched_command.get('command'))

    # display a series of message boxes containing info about CLI-Buddy when the info
    # button is clicked, giving the user the option to cancel at any time
    def display_info(self):
        messages = [
            'CLI-Buddy is an application that allows you to search for command line commands.',
            'Simply enter some keywords into the box and click the arrow button (or hit Enter) and the application '
            'will return a list of all commands that contain at least one of the words. Leaving the box empty will '
            'return all of the commands stored in CLI-Buddy.',
            'If you wish to exactly match multiple words, encase everything in double/single quotes, and the application will look '
            'for an exact match of the string you have input. Note that you cannot mix and match both quoted and non-quoted '
            'keywords in the same search.',
            'Clicking on a command from the list will open up its man page on the command line, ' 
            'where you can read up on further information.',
            'Disclaimer: This is by no means a comprehensive list of command line commands, '
            'and it only contains the commands in section 1 of the man pages. Hope you find this tool useful!'
        ]
        counter = 0
        while True:
            if not messagebox.askokcancel("Info About CLI-Buddy", messages[counter], icon='info'):
                break
            counter += 1
            if counter >= len(messages):
                break
    
    # open the man page of the user's selected command, hide the application window until user has exited
    # the man page
    def display_man_page(self, event):
        command_name = self.combo.get().split(":")[0]
        root.withdraw()
        subprocess.call(["man", command_name])
        root.deiconify()


# configure proerties of the window
root.geometry('600x400')
root.resizable(False, False)
root.configure(bg="#b3fbc8")
my_gui = CLIBuddy(root)
root.mainloop()
