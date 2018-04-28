""" GUI application for Eternal Deck Tracker (EDT) """
# pylint: disable=invalid-name
try:
    # python 3.x
    import tkinter as tk
    import tkinter.font as font

except ImportError:
    # python 2.x
    import Tkinter as tk
    import tkFont as font
# from tkinter import ttk


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
        self.master.resizable(width=True, height=True)
        for i in range(4):
            tk.Grid.rowconfigure(self, i, weight=1)
            tk.Grid.columnconfigure(self, i, weight=1)

    def myfunction(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"), width=500,height=1000)

    def create_widgets(self):
        """ initalizes widgets """
        padx = 10
        pady = 10

        self.canvas = tk.Canvas(self)
        myframe = tk.Frame(self.canvas)
        myscrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=myscrollbar.set)

        myscrollbar.grid(row=0, column=1, rowspan=3, sticky=tk.N+tk.S+tk.E)
        self.canvas.grid(rowspan=4)
        self.canvas.create_window((0,0),window=myframe,anchor='nw')
        myframe.bind("<Configure>", self.myfunction)

        self.cards_left = tk.StringVar()
        self.cards_left.set('You have ' + str(self.mydeck.count()[3]) + ' cards left!')
        self.card_count = tk.Label(myframe,  textvariable=self.cards_left)
        self.card_count.grid(row=3, column=0, padx=padx, pady=pady, sticky=tk.N+tk.S+tk.E+tk.W)

        self.units_display = CardDisplays(myframe,  self.mydeck, 'units')
        self.units_display.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N+tk.S+tk.E+tk.W)

        self.spells_display = CardDisplays(myframe,  self.mydeck, 'spells')
        self.spells_display.grid(row=1, column=0, padx=padx, pady=pady, sticky=tk.N+tk.S+tk.E+tk.W)

        self.power_display = CardDisplays(myframe,  self.mydeck, 'power')
        self.power_display.grid(row=2, column=0, padx=padx, pady=pady, sticky=tk.N+tk.S+tk.E+tk.W)


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
        tk.Frame.__init__(self, master, bg='#626262',**kwargs)

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

        for i in range(100):
            tk.Grid.rowconfigure(self, i, weight=1)

        tk.Grid.columnconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 1, weight=1)
        tk.Grid.columnconfigure(self, 2, weight=1)

        self.create_buttons()

    def create_buttons(self):
        """ create buttons """
        # pylint: disable=too-many-locals
        font_family = 'Helvetica'
        gui_font = font.Font(family=font_family, size=8)
        title_font = font.Font(family=font_family, size=12, weight=font.BOLD) 
        b_width = 20
        b_bg = '#626262'
        l_width = 6
        q_width = 3
        b_height = 0
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
            self, text=self.section_label, background=b_bg, font=title_font)
        self.section_label_obj.grid(row=0, column=0, columnspan=3, ipadx=100,
                                    ipady=ipady, padx=padx, pady=pady, sticky=tk.N+tk.S+tk.E+tk.W)

        # creating column labels
        tk.Label(self, text='Probability', 
                 background=b_bg, font=gui_font).grid(row=1, column=0, ipadx=ipadx,
                                       ipady=ipady, padx=padx, pady=pady, sticky=tk.N+tk.S+tk.E+tk.W)

        tk.Label(self, text='Name', 
                 background=b_bg, font=gui_font).grid(row=1, column=1, ipadx=ipadx,
                                       ipady=ipady, padx=padx, pady=pady, sticky=tk.N+tk.S+tk.E+tk.W)

        tk.Label(self, text='Quantity',
                 background=b_bg, font=gui_font).grid(row=1, column=2, ipadx=ipadx,
                                       ipady=ipady, padx=padx, pady=pady, sticky=tk.N+tk.S+tk.E+tk.W)


        for i, card in enumerate(self.mydeck.deck[self.disp_type]):

            # create probability button
            self.card_prob_str.append(tk.StringVar())
            self.card_prob_str[i].set('{0:0.2f}'.format(card.probability))
            self.card_prob_button.append(
                tk.Button(self, textvariable=self.card_prob_str[i], background=b_bg, font=gui_font))
            self.card_prob_button[i].grid(row=i+2, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

            # create name button
            self.card_name_str.append(tk.StringVar())
            self.card_name_str[i].set(card.name)
            self.card_name_button.append(
                tk.Button(self, textvariable=self.card_name_str[i], background=b_bg,
                          command=lambda i=i: self.subtract_card(self.disp_type, i), font=gui_font))
            self.card_name_button[i].grid(row=i+2, column=1, sticky=tk.N+tk.S+tk.E+tk.W)

            # create quantity button
            self.card_quantity_str.append(tk.StringVar())
            self.card_quantity_str[i].set(card.quantity)
            self.card_quantity_button.append(
                tk.Button(self, textvariable=self.card_quantity_str[i], background=b_bg,
                          command=lambda i=i: self.add_card(self.disp_type, i), font=gui_font))
            self.card_quantity_button[i].grid(
                row=i+2, column=2, sticky=tk.N+tk.S+tk.E+tk.W)

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

    tk.Grid.rowconfigure(root, 0, weight=1)
    tk.Grid.columnconfigure(root, 0, weight=1)

    app.grid(sticky=tk.N+tk.S+tk.E+tk.W)
    app.mainloop()


if __name__ == "__main__":
    DECKLIST = 'deck.csv'
    CARD_DB = 'eternal-cards-1.31.json'
    main(DECKLIST, CARD_DB)
