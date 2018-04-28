""" GUI application for Eternal Deck Tracker (EDT) """
# pylint: disable=invalid-name
try:
    # python 3.x
    import tkinter as tk
    import tkinter.font as font
    from tkinter import ttk

except ImportError:
    # python 2.x
    import Tkinter as tk
    import tkFont as font


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
        # self.master.geometry("280x800")
        self.master.resizable(width=True, height=True)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i, weight=1)

    def create_widgets(self):
        """ initalizes widgets """
        padx = 10
        pady = 10

        font_family = 'Helvetica'
        gui_font = font.Font(family=font_family, size=12)

        self.cards_left = tk.StringVar()
        self.cards_left.set('You have ' + str(self.mydeck.count()[3]) + ' cards left!')
        self.card_count = tk.Label(self, textvariable=self.cards_left, font=gui_font)
        self.card_count.grid(row=3, column=0, padx=padx, pady=pady, sticky='NSEW')

        self.units_display = CardDisplays(self, self.mydeck, 'units')
        self.units_display.grid(row=0, column=0, padx=padx, pady=pady, sticky='NSEW')

        self.spells_display = CardDisplays(self, self.mydeck, 'spells')
        self.spells_display.grid(row=1, column=0, padx=padx, pady=pady, sticky='NSEW')

        self.power_display = CardDisplays(self, self.mydeck, 'power')
        self.power_display.grid(row=2, column=0, padx=padx, pady=pady, sticky='NSEW')

    def update_all_probability(self):
        """ calls update_probability on all obj """
        self.units_display.update_probability()
        self.spells_display.update_probability()
        self.power_display.update_probability()
        self.cards_left.set('You have ' + str(self.mydeck.count()[3]) + ' cards left!')


class CardDisplays(tk.Frame):
    """ Frame for spells """
    # pylint: disable=too-many-ancestors, too-many-instance-attributes

    def __init__(self, master, mydeck, display, **kwargs):
        tk.Frame.__init__(self, master, bg='#626262', **kwargs)

        self.master = master
        self.mydeck = mydeck

        if display.lower() in ['unit', 'units', '0', 'monsters', 0]:
            self.disp_type = 0
            self.section_label = 'Units'

        elif display.lower() in ['spell', 'spells', 'magic', '1', 1]:
            self.disp_type = 1
            self.section_label = 'Spells'

        elif display.lower() in ['power', 'power', 'land', 'sigil', 'sigils', '2', 2]:
            self.disp_type = 2
            self.section_label = 'Power'

        half_size = 30
        full_size = 120
        for i in range(100):
            self.grid_rowconfigure(i, weight=1)

        self.grid_columnconfigure(0, weight=1, minsize=half_size)
        self.grid_columnconfigure(1, weight=3, minsize=full_size)
        self.grid_columnconfigure(2, weight=1, minsize=half_size)

        self.create_buttons()

    def create_buttons(self):
        """ create buttons """
        # pylint: disable=too-many-locals
        font_family = 'Helvetica'
        gui_font = font.Font(family=font_family, size=12)
        title_font = font.Font(family=font_family, size=18, weight=font.BOLD)
        b_bg = '#626262'
        ipadx = 20
        ipady = 3
        padx = 0
        pady = 0

        self.card_name_button = []
        self.card_name_str = []

        self.card_quantity_button = []
        self.card_quantity_str = []

        self.card_prob_button = []
        self.card_prob_str = []

        # creating section title
        self.section_label_obj = tk.Label(
            self, text=self.section_label, background=b_bg, font=title_font,
            foreground='blue')
        self.section_label_obj.grid(row=0, column=0, columnspan=3, ipadx=100,
                                    ipady=ipady, padx=padx, pady=pady, sticky='NSEW')

        # creating column labels
        tk.Label(self, text='Probability',
                 background=b_bg, font=gui_font).grid(row=1, column=0, ipadx=ipadx,
                                                      ipady=ipady, padx=padx, pady=pady,
                                                      sticky='NSEW')

        tk.Label(self, text='Name',
                 background=b_bg, font=gui_font).grid(row=1, column=1, ipadx=ipadx,
                                                      ipady=ipady, padx=padx, pady=pady,
                                                      sticky='NSEW')

        tk.Label(self, text='Quantity',
                 background=b_bg, font=gui_font).grid(row=1, column=2, ipadx=ipadx,
                                                      ipady=ipady, padx=padx, pady=pady,
                                                      sticky='NSEW')

        for i, card in enumerate(self.mydeck.deck[self.disp_type]):

            num_colors = 0

            for influence in card.influence.lower():
                if influence == 'p':
                    text_color = 'navy'
                    num_colors += 1

                elif influence == 's':
                    text_color = 'purple'
                    num_colors += 1

                elif influence == 'f':
                    text_color = 'red'
                    num_colors += 1

                elif influence == 'j':
                    text_color = 'forest green'
                    num_colors += 1

                elif influence == 't':
                    text_color = 'gold'
                    num_colors += 1

                else:
                    text_color = 'black'

                if num_colors > 1:
                    text_color = 'gray18'

            # create probability button
            self.card_prob_str.append(tk.StringVar())
            self.card_prob_str[i].set('{0:0.2f}'.format(card.probability))
            self.card_prob_button.append(
                tk.Button(self, textvariable=self.card_prob_str[i], background=b_bg, font=gui_font,
                          foreground=text_color))
            self.card_prob_button[i].grid(row=i+2, column=0, sticky='NSEW')

            # create name button
            self.card_name_str.append(tk.StringVar())
            self.card_name_str[i].set(card.name)
            self.card_name_button.append(
                tk.Button(self, textvariable=self.card_name_str[i], background=b_bg,
                          command=lambda i=i: self.subtract_card(self.disp_type, i), font=gui_font, foreground=text_color))
            self.card_name_button[i].grid(row=i+2, column=1, sticky='NSEW')

            # create quantity button
            self.card_quantity_str.append(tk.StringVar())
            self.card_quantity_str[i].set(card.quantity)
            self.card_quantity_button.append(
                tk.Button(self, textvariable=self.card_quantity_str[i], background=b_bg,
                          command=lambda i=i: self.add_card(self.disp_type, i), font=gui_font, foreground=text_color))
            self.card_quantity_button[i].grid(
                row=i+2, column=2, sticky='NSEW')

    def add_card(self, card_type, index):
        """ add card and updating tk StringVar """
        self.mydeck.add_card(card_type, index)

        self.card_quantity_str[index].set(
            self.mydeck.deck[card_type][index].quantity)

        app.update_all_probability()

    def subtract_card(self, card_type, index):
        """ add card and updating tk StringVar """
        self.mydeck.subtract_card(card_type, index)

        self.card_quantity_str[index].set(
            self.mydeck.deck[card_type][index].quantity)

        app.update_all_probability()

    def update_probability(self):
        """ updates probability column """

        for i, card in enumerate(self.mydeck.deck[self.disp_type]):
            self.card_prob_str[i].set('{0:0.2f}'.format(card.probability))


def main(decklist, card_db):
    """ main function """
    # pylint: disable = global-variable-undefined, invalid-name
    import deck as dk
    global app

    mydeck = dk.Deck(decklist, card_db)

    root = tk.Tk()
    app = MainApplication(root, mydeck)

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.minsize(280, 800)

    # app.grid(row=0, column=0, sticky='NSEW')
    app.pack(fill='both')

    app.mainloop()


if __name__ == "__main__":
    DECKLIST = 'deck.csv'
    CARD_DB = 'eternal-cards-1.31.json'
    main(DECKLIST, CARD_DB)
