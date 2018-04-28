""" GUI application for Eternal Deck Tracker (EDT) """
# pylint: disable=invalid-name
try:
    # python 3.x
    import tkinter as tk
    import tkinter.font as font
    # from tkinter import ttk

except ImportError:
    # python 2.x
    import Tkinter as tk
    import tkFont as font


class MainApplication(tk.Frame):

    """ master app """
    # pylint: disable = too-many-ancestors, too-many-instance-attributes

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

        font_family = 'Helvetica'
        text_font = font.Font(family=font_family, size=12)
        title_font = font.Font(family=font_family, size=18, weight=font.BOLD)

        self.gui_fonts = [text_font, title_font]

    def create_widgets(self):
        """ initalizes widgets """
        padx = 10
        pady = 10

        font_family = 'Helvetica'
        self.text_font = font.Font(family=font_family, size=12)

        # create card count label
        self.cards_left = tk.StringVar()
        self.cards_left.set(
            'You have ' + str(self.mydeck.count()[3]) + ' cards left!')
        self.card_count = tk.Label(
            self, textvariable=self.cards_left, font=self.gui_fonts[0])
        self.card_count.grid(
            row=3, column=0, padx=padx, pady=pady, sticky='NSEW')

        # create quit app button
        tk.Button(
            self, text='Quit', font=self.gui_fonts[0], command=self.quit_app).grid(
                row=4, column=0, padx=padx, pady=pady, sticky='NSEW')

        # create units widget
        self.units_display = CardDisplay(self, self.mydeck, 'units', self.gui_fonts)
        self.units_display.grid(
            row=0, column=0, padx=padx, pady=pady, sticky='NSEW')

        # create spells widget
        self.spells_display = CardDisplay(self, self.mydeck, 'spells', self.gui_fonts)
        self.spells_display.grid(
            row=1, column=0, padx=padx, pady=pady, sticky='NSEW')

        # create power widget
        self.power_display = CardDisplay(self, self.mydeck, 'power', self.gui_fonts)
        self.power_display.grid(
            row=2, column=0, padx=padx, pady=pady, sticky='NSEW')

    def update_all_probability(self):
        """ calls update_probability on all obj """
        self.units_display.update_probability()
        self.spells_display.update_probability()
        self.power_display.update_probability()
        self.cards_left.set(
            'You have ' + str(self.mydeck.count()[3]) + ' cards left!')

    def quit_app(self):
        """ closes screen """
        self.master.destroy()


class CardDisplay(tk.Frame):

    """ Frame for card name and quantity """
    # pylint: disable=too-many-ancestors, too-many-instance-attributes

    def __init__(self, master, mydeck, display, gui_fonts, **kwargs):
        tk.Frame.__init__(self, master, bg='#626262', **kwargs)

        self.master = master
        self.mydeck = mydeck
        self.text_font = gui_fonts[0]
        self.title_font = gui_fonts[1]

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

        self.update_text_color()

        self.create_buttons()

    def create_buttons(self):
        """ create buttons """
        # pylint: disable=too-many-locals
        font_family = 'Helvetica'
        self.text_font = font.Font(family=font_family, size=12)
        self.title_font = font.Font(family=font_family, size=18, weight=font.BOLD)
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
            self, text=self.section_label, background=b_bg, font=self.title_font,
            foreground='blue')
        self.section_label_obj.grid(row=0, column=0, columnspan=3, ipadx=100,
                                    ipady=ipady, padx=padx, pady=pady, sticky='NSEW')

        # creating column labels
        tk.Label(self, text='Probability',
                 background=b_bg, font=self.text_font).grid(row=1, column=0, ipadx=ipadx,
                                                            ipady=ipady, padx=padx, pady=pady,
                                                            sticky='NSEW')

        tk.Label(self, text='Name',
                 background=b_bg, font=self.text_font).grid(row=1, column=1, ipadx=ipadx,
                                                            ipady=ipady, padx=padx, pady=pady,
                                                            sticky='NSEW')

        tk.Label(self, text='Quantity',
                 background=b_bg, font=self.text_font).grid(row=1, column=2, ipadx=ipadx,
                                                            ipady=ipady, padx=padx, pady=pady,
                                                            sticky='NSEW')

        for i, card in enumerate(self.mydeck.deck[self.disp_type]):

            # create probability button
            self.card_prob_str.append(tk.StringVar())
            self.card_prob_str[i].set('{0:0.2f}'.format(card.probability))
            self.card_prob_button.append(
                tk.Button(
                    self, textvariable=self.card_prob_str[
                        i], background=b_bg, font=self.text_font,
                    foreground=self.text_colors[i]))
            self.card_prob_button[i].grid(row=i + 2, column=0, sticky='NSEW')

            # create name button
            self.card_name_str.append(tk.StringVar())
            self.card_name_str[i].set(card.name)
            self.card_name_button.append(
                tk.Button(
                    self, textvariable=self.card_name_str[i], background=b_bg,
                    command=lambda i=i: self.subtract_card(self.disp_type, i), font=self.text_font,
                    foreground=self.text_colors[i]))
            self.card_name_button[i].grid(row=i + 2, column=1, sticky='NSEW')

            # create quantity button
            self.card_quantity_str.append(tk.StringVar())
            self.card_quantity_str[i].set(card.quantity)
            self.card_quantity_button.append(
                tk.Button(
                    self, textvariable=self.card_quantity_str[
                        i], background=b_bg,
                    command=lambda i=i: self.add_card(self.disp_type, i), font=self.text_font,
                    foreground=self.text_colors[i]))
            self.card_quantity_button[i].grid(
                row=i + 2, column=2, sticky='NSEW')

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

        # evaluate probability range
        prob_arr = []
        prob_dict = {}
        num_steps = 3
        for card in self.mydeck.deck[self.disp_type]:
            prob_arr.append(card.probability)

        prob_arr = sorted(list(set(prob_arr)))
                          # super paranoid just to be sure for diff ver
        print('prob_arr', prob_arr)
        increment = int(255 / len(prob_arr) * num_steps)
        print('increment', increment)

        for i, prob in enumerate(prob_arr):
            print('prob', prob)
            print('prob_arr', prob_arr[-i])
            if prob < prob_arr[-i] / 2:
                if i + 1 * increment < 255:
                    prob_dict[prob] = [255, i * increment, 0]
                else:
                    prob_dict[prob] = [255, 255, 0]

            elif prob < prob_arr[-i]:
                if 255 - i + 1 * increment > 0:
                    prob_dict[prob] = [255 - i * increment, 255, 0]
                else:
                    prob_dict[prob] = [0, 255, 0]

            else:
                print('error')

        print('prob_dict', prob_dict.items())
        print('')
        print('------------')

        for i, card in enumerate(self.mydeck.deck[self.disp_type]):
            self.card_prob_str[i].set('{0:0.2f}'.format(card.probability))

    def update_text_color(self):
        """ reads card influence and returns card text color """
        # pylint:disable=too-many-branches
        text_colors = []
        color_instance = ''

        for card in self.mydeck.deck[self.disp_type]:
            influence_list = ''
            num_colors = 0
            for influence in card.influence.upper():
                if influence in ['F', 'S', 'J', 'P', 'T']:
                    influence_list += influence
            influence_list = set(influence_list)

            color_instance = 'black'

            if 'P' in influence_list:
                if color_instance != 'dodger blue':
                    num_colors += 1
                color_instance = 'dodger blue'

            if 'S' in influence_list:
                if color_instance != 'medium purple':
                    num_colors += 1
                color_instance = 'medium purple'

            if 'F' in influence_list:
                if color_instance != 'red':
                    num_colors += 1
                color_instance = 'red'

            if 'J' in influence_list:
                if color_instance != 'forest green':
                    num_colors += 1
                color_instance = 'forest green'

            if 'T' in influence_list:
                if color_instance != 'gold':
                    num_colors += 1
                color_instance = 'gold'

            if num_colors > 1:
                color_instance = 'black'
                text_colors.append(color_instance)
            else:
                text_colors.append(color_instance)

        self.text_colors = text_colors
        return text_colors


class ProbDisplay(tk.Frame):

    """ Displays probability for card """
    # pylint: disable = too-many-ancestors

    def __init__(self, master, mydeck, display, **kwargs):
        tk.Frame.__init__(self, master, bg='#626262', **kwargs)

        self. master = master
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
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

        self.create_buttons()

    def create_buttons(self):
        """ create probability buttons """


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
