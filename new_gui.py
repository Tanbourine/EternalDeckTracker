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


class Window_One(tk.Frame):  # pylint: disable=too-many-ancestors

    """ first app """

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid(row=0, column=0, sticky=tk.W, padx=4)
        tk.Button(self, text=deck.deck[0][0].name).grid(row=0, column=0)


class Window_Two(tk.Frame):  # pylint: disable=too-many-ancestors

    """ window 2 """

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid(row=1, column=0)
        tk.Label(self, text="This is my second GUI").grid(row=1, column=0)


def main(deck):
    """ main function """
    app = App()

    window_1 = Window_One(app)
    window_2 = Window_Two(app)
    app.mainloop()


if __name__ == "__main__":
    import deck as dk
    DECKLIST = 'deck.csv'
    CARD_DB = 'eternal-cards-1.31.json'
    deck = dk.Deck(DECKLIST, CARD_DB)
    main(deck)
