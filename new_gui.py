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
    # pylint: disable = too-many-ancestors

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
        padx = 10
        pady = 20

        self.units_display = CardDisplays(self, self.mydeck, 'units')
        self.units_display.grid(row=0, column=0, padx=padx, pady=pady)

        self.spells_display = CardDisplays(self, self.mydeck, 'spells')
        self.spells_display.grid(row=1, column=0, padx=padx, pady=pady)

        self.units_display = CardDisplays(self, self.mydeck, 'power')
        self.units_display.grid(row=2, column=0, padx=padx, pady=pady)


class CardDisplays(tk.Frame):  # pylint: disable=too-many-ancestors

    """ Frame for spells """

    def __init__(self, master, mydeck, display, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        self.master = master
        self.mydeck = mydeck
        self.display = display
        self.grid(row=0, column=0, sticky=tk.E+tk.W)
        self.create_buttons()

    def create_buttons(self):
        """ create buttons """
        # pylint: disable=too-many-locals
        b_width = 20
        b_bg = '#626262'
        l_width = 6
        q_width = 3
        b_height = 1
        ipadx = 30
        ipady = 10
        padx = 5
        pady = 5

        card_name_button = []
        card_name_str = []

        card_quantity_button = []
        card_quantity_str = []

        card_prob_button = []
        card_prob_str = []

        if self.display.lower() in ['unit', 'units', '0', 'monsters', 0]:
            disp_type = 0
            section_label = 'Units'

        elif self.display.lower() in ['spell', 'spells', 'magic', '1', 1]:
            disp_type = 1
            section_label = 'Spells'

        elif self.display.lower() in ['power', 'power', 'land', 'sigil',
                                      'sigils', '2', 2]:
            disp_type = 2
            section_label = 'Power'

        # creating section title
        section_label_obj = tk.Label(self, text=section_label, back=b_bg)
        section_label_obj.grid(row=0, column=0, columnspan=3, ipadx=100,
                               ipady=ipady, padx=padx, pady=pady,
                               sticky=tk.E+tk.W)

        # creating column labels
        tk.Label(self, text='Probability', width=l_width,
                 background=b_bg).grid(row=1, column=0, ipadx=ipadx,
                                       ipady=ipady, padx=padx, pady=pady)

        tk.Label(self, text='Name', width=b_width,
                 background=b_bg).grid(row=1, column=1, ipadx=ipadx,
                                       ipady=ipady, padx=padx, pady=pady)

        tk.Label(self, text='Quantity', width=q_width,
                 background=b_bg).grid(row=1, column=2, ipadx=ipadx,
                                       ipady=ipady, padx=padx, pady=pady)

        for i, card in enumerate(self.mydeck.deck[disp_type]):

            card_prob_str.append(tk.StringVar())
            card_prob_str[i].set('{0:0.2f}'.format(card.probability))
            card_prob_button.append(
                tk.Button(self, textvariable=card_prob_str[i], width=l_width,
                          height=b_height, background=b_bg))
            card_prob_button[i].grid(row=i+2, column=0, sticky=tk.E+tk.W)

            card_name_str.append(tk.StringVar())
            card_name_str[i].set(card.name)
            card_name_button.append(
                tk.Button(self, textvariable=card_name_str[i], width=b_width,
                          height=b_height, background=b_bg))
            card_name_button[i].grid(row=i+2, column=1, sticky=tk.E+tk.W)

            card_quantity_str.append(tk.StringVar())
            card_quantity_str[i].set(card.quantity)
            card_quantity_button.append(
                tk.Button(self, textvariable=card_quantity_str[i],
                          width=q_width, height=b_height, background=b_bg))
            card_quantity_button[i].grid(
                row=i+2, column=2, sticky=tk.E+tk.W)

    def add_card(self, card_type, index):
        """ add card and updating tk StringVar """
        self.mydeck.add_card(card_type, index)


def main():
    """ main function """
    decklist = 'deck.csv'
    card_db = 'eternal-cards-1.31.json'
    mydeck = dk.Deck(decklist, card_db)

    root = tk.Tk()
    app = MainApplication(root, mydeck)
    app.pack(fill="both", expand=True)
    app.mainloop()


if __name__ == "__main__":
    import deck as dk
    main()
