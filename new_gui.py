""" GUI application for Eternal Deck Tracker (EDT) """

import tkinter as tk
# from tkinter import ttk


class App(tk.Tk):
    """ master app """
    def __init__(self):

        # Initialize tk inheritance
        tk.Tk.__init__(self)
        self.wm_title("Eternal Deck Tracker")
        self.geometry("450x700+300+300")
        self.resizable(width=True, height=True)

class Window_1(tk.Frame):  # pylint: disable=too-many-ancestors

    """ first app """

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid(row=0, column=0)
        tk.Button(self, text=deck.deck[0][0].name).pack()
        # tk.Button(self, text="This is my first GUI").pack()

class Window_2(tk.Frame): # pylint: disable=too-many-ancestors
    """ window 2 """

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid(row=0, column=1)
        tk.Label(self, text="This is my second GUI").pack()
        


def main(deck):
    """ main function """
    print(deck.show_property('Name'))
    app = App()

    window_1 = Window_1(app)
    window_2 = Window_2(app)
    app.mainloop()


if __name__ == "__main__":
    import deck as dk
    DECKLIST = 'deck.csv'
    CARD_DB = 'eternal-cards-1.31.json'
    deck = dk.Deck(DECKLIST, CARD_DB)
    main(deck)

