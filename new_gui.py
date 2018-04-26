""" GUI application for Eternal Deck Tracker (EDT) """

try:
    # python 3.x
    import tkinter as tk
except ImportError:
    # python 2.x
    import Tkinter as tk
    
# from tkinter import ttk

# https://stackoverflow.com/questions/47306956/inheritance-from-tkinter-frame-in-varying-implementations?rq=1&utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa


class MainApplication(tk.Frame):

    """ master app """

    def __init__(self, master, mydeck):
        tk.Frame.__init__(self, master)

        self.master = master
        self.mydeck = mydeck

        self.configure_gui()
        self.create_widgets()

    def configure_gui(self):
        """ configure gui settings """
        self.master.title("Eternal Deck Tracker")
        # self.master.geometry("450x700")
        self.master.resizable(width=False, height=False)

    def create_widgets(self):
        """ initalizes widgets """
        self.spells_window = SpellsWindow(self)
        self.spells_window.pack()


class SpellsWindow(tk.Frame):  # pylint: disable=too-many-ancestors

    """ Frame for spells """

    def __init__(self, master, **kwargs):
        self.master = master
        tk.Frame.__init__(self, master, **kwargs)
        self.grid(row=0, column=0, sticky=tk.E+tk.W)
        self.create_buttons()

    def create_buttons(self):
        """ create buttons """
        b_width = 30
        b_bg = '#626262'
        l_width = 6
        q_width = 3
        b_height = 1
        ipadx = 15
        ipady = 5

        card_name_button = []
        card_name_str = []

        card_quantity_button = []
        card_quantity_str = []

        card_prob_button = []
        card_prob_str = []
        
        for i, card in enumerate(mydeck.deck[1]):

            card_prob_str.append(tk.StringVar())
            card_prob_str[i].set('{0:0.2f}'.format(card.probability))
            card_prob_button.append(
                    tk.Button(self, textvariable=card_prob_str[i], width=l_width, height=b_height, background=b_bg))
            card_prob_button[i].grid(row=i, column=0, sticky=tk.E+tk.W)

            card_name_str.append(tk.StringVar())
            card_name_str[i].set(card.name)
            card_name_button.append(
                    tk.Button(self, textvariable=card_name_str[i], width=b_width, height=b_height, background=b_bg))
            card_name_button[i].grid(row=i, column=1, sticky=tk.E+tk.W)

            card_quantity_str.append(tk.StringVar())
            card_quantity_str[i].set(card.quantity)
            card_quantity_button.append(
                    tk.Button(self, textvariable=card_quantity_str[i], width=q_width, height=b_height, background=b_bg))
            card_quantity_button[i].grid(row=i, column=2, sticky=tk.E+tk.W)

    def add_card(card_type, index):
        """ add card and updating tk StringVar """
        mydeck.add_card(card_type, index)
        




        
    # tk.Button(self, text=mydeck.deck[0][0].name).grid(row=0, column=0, padx=20, pady=20, ipadx=5, ipady=5)


class Window_Two(tk.Frame):  # pylint: disable=too-many-ancestors

    """ window 2 """

    def __init__(self, master):
        tk.Frame.__init__(self, master, **kwargs)
        self.grid(row=1, column=0)
        tk.Label(self, text="This is my second GUI").grid(row=1, column=0)


def main(deck):
    """ main function """

    root = tk.Tk()
    app = MainApplication(root, deck)
    app.pack(fill="both", expand=True)
    app.mainloop()


if __name__ == "__main__":
    import deck as dk
    DECKLIST = 'deck.csv'
    CARD_DB = 'eternal-cards-1.31.json'
    mydeck = dk.Deck(DECKLIST, CARD_DB)
    main(mydeck)
