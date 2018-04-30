#allows user to copy/paste exported deck from eternal into entry box to create a deck

class page2(tk.Frame):
    """page 2 window/application frame. Entry box, button, and label within"""

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.master = master
        self.create_widget()
        self.poop = 0
        
