import tkinter as tk


class DeckGUI(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(master, text="yes")


class MainApplication(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.deckGUI = DeckGUI(self)

        self.deckGUI.pack()


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root)
    #.pack(side="top", fill="both", expand=True)
    root.mainloop()


# https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application
