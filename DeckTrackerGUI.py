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

        bg_color = '#626262'

        self.gui_disp_options = [text_font, title_font, bg_color]

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
            self, textvariable=self.cards_left, font=self.gui_disp_options[0])
        self.card_count.grid(
            row=3, column=0, padx=padx, pady=pady, sticky='NSEW')

        # create quit app button
        tk.Button(
            self, text='Quit', font=self.gui_disp_options[0], command=self.quit_app).grid(
                row=4, column=0, padx=padx, pady=pady, sticky='NSEW')

        # create units widget
        self.units_display = CardDisplay(self, self.mydeck, 'units', self.gui_disp_options)
        self.units_display.grid(
            row=0, column=0, padx=padx, pady=pady, sticky='NSEW')

        # create spells widget
        self.spells_display = CardDisplay(self, self.mydeck, 'spells', self.gui_disp_options)
        self.spells_display.grid(
            row=1, column=0, padx=padx, pady=pady, sticky='NSEW')

        # create power widget
        self.power_display = CardDisplay(self, self.mydeck, 'power', self.gui_disp_options)
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

    def __init__(self, master, mydeck, display, gui_disp_options, **kwargs):

        self.master = master
        self.mydeck = mydeck
        self.text_font = gui_disp_options[0]
        self.title_font = gui_disp_options[1]
        self.bg_color = gui_disp_options[2]
        self.prob_color = []

        tk.Frame.__init__(self, master, bg=self.bg_color, **kwargs)

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
        self.update_probability()

    def create_buttons(self):
        """ create buttons """
        # pylint: disable=too-many-locals
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
            self, text=self.section_label, background=self.bg_color, font=self.title_font,
            foreground='blue')
        self.section_label_obj.grid(row=0, column=0, columnspan=3, ipadx=100,
                                    ipady=ipady, padx=padx, pady=pady, sticky='NSEW')

        # creating column labels
        tk.Label(self, text='Probability',
                 background=self.bg_color, font=self.text_font).grid(
                     row=1, column=0, ipadx=ipadx, ipady=ipady, padx=padx,
                     pady=pady, sticky='NSEW')

        tk.Label(self, text='Name',
                 background=self.bg_color, font=self.text_font).grid(
                     row=1, column=1, ipadx=ipadx, ipady=ipady, padx=padx, pady=pady,
                     sticky='NSEW')

        tk.Label(self, text='Quantity',
                 background=self.bg_color, font=self.text_font).grid(
                     row=1, column=2, ipadx=ipadx,
                     ipady=ipady, padx=padx, pady=pady, sticky='NSEW')

        for i, card in enumerate(self.mydeck.deck[self.disp_type]):

            # create probability button
            self.card_prob_str.append(tk.StringVar())
            self.card_prob_str[i].set('{0:0.2f}'.format(card.probability))
            self.card_prob_button.append(
                tk.Button(
                    self, textvariable=self.card_prob_str[
                        i], background=self.bg_color, font=self.text_font,
                    fg=self.text_colors[i]))
            self.card_prob_button[i].grid(row=i + 2, column=0, sticky='NSEW')

            # create name button
            self.card_name_str.append(tk.StringVar())
            self.card_name_str[i].set(card.name)
            self.card_name_button.append(
                tk.Button(
                    self, textvariable=self.card_name_str[i], background=self.bg_color,
                    command=lambda i=i: self.subtract_card(self.disp_type, i), font=self.text_font,
                    fg=self.text_colors[i]))
            self.card_name_button[i].grid(row=i + 2, column=1, sticky='NSEW')

            # create quantity button
            self.card_quantity_str.append(tk.StringVar())
            self.card_quantity_str[i].set(card.quantity)
            self.card_quantity_button.append(
                tk.Button(
                    self, textvariable=self.card_quantity_str[
                        i], background=self.bg_color,
                    command=lambda i=i: self.add_card(self.disp_type, i), font=self.text_font,
                    fg='black'))
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

        self.assign_prob_color()

        for i, card in enumerate(self.mydeck.deck[self.disp_type]):
            self.card_prob_str[i].set('{0:0.2f}'.format(card.probability))
            self.card_prob_button[i].configure(fg=self.prob_color[self.disp_type][i])

    def assign_prob_color(self):
        """ assigns probability colors """
        # pylint: disable = too-many-branches

        # evaluate probability range
        prob_arr = []
        prob_dict = {}
        num_colors = 3
        hysteresis = 25

        for card_type in self.mydeck.deck:
            for card in card_type:
                prob_arr.append(card.probability)

        # get unique probabilities and sort
        prob_arr = sorted(list(set(prob_arr)))

        increment = int(255 / len(prob_arr) * num_colors)

        # assign colors to probability
        pos_color_var = 0
        neg_color_var = 0
        for prob in prob_arr:

            # if prob is turning yellow
            if prob < prob_arr[-1] / 2:

                # set 0% as red
                if prob == prob_arr[0]:
                    prob_dict[prob] = (255, 0, 0)

                else:
                    # if color does not exceed (255,255,0)
                    if pos_color_var + increment < 255 - hysteresis:
                        # increase color towards yellow
                        pos_color_var += increment
                        prob_dict[prob] = (255, pos_color_var, 0)
                    else:
                        # if color exceeds (255, 255, 0), cap it!
                        prob_dict[prob] = (255, 255, 0)

            # if prob is turning green
            else:

                # set highest prob as green
                if prob == prob_arr[-1]:
                    prob_dict[prob] = (0, 255, 0)

                else:
                    # if color does not exceed (0, 255, 0)
                    if neg_color_var + increment < 255 - hysteresis:
                        # decrease color towards green
                        neg_color_var += increment
                        prob_dict[prob] = (255 - neg_color_var, 255, 0)
                    else:
                        # if color exceeds (0, 255, 0), cap it!
                        prob_dict[prob] = (0, 255, 0)

        # reset self.prob_color
        self.prob_color = []
        for i, card_type in enumerate(self.mydeck.deck):
            self.prob_color.append([])
            for card in card_type:
                # convert RGB to HEX
                self.prob_color[i].append('#%02x%02x%02x' % prob_dict[card.probability])

    def update_text_color(self):
        """ reads card influence and returns card text color """
        # pylint:disable=too-many-branches
        self.text_colors = []
        color_instance = ''
        primal = 'dodger blue'
        shadow = 'medium purple'
        fire = 'red'
        justice = 'forest green'
        time = 'gold'
        neutral = 'gray18'
        multi = 'pink'

        for card in self.mydeck.deck[self.disp_type]:
            influence_list = ''
            num_colors = 0
            for influence in card.influence.upper():
                if influence in ['F', 'S', 'J', 'P', 'T']:
                    influence_list += influence
            influence_list = set(influence_list)

            color_instance = neutral

            if 'P' in influence_list:
                # if color isn't already this
                if color_instance != primal:
                    num_colors += 1
                color_instance = primal

            if 'S' in influence_list:
                # if color isn't already this
                if color_instance != shadow:
                    num_colors += 1
                color_instance = shadow

            if 'F' in influence_list:
                # if color isn't already this
                if color_instance != fire:
                    num_colors += 1
                color_instance = fire

            if 'J' in influence_list:
                # if color isn't already this
                if color_instance != justice:
                    num_colors += 1
                color_instance = justice

            if 'T' in influence_list:
                # if color isn't already this
                if color_instance != time:
                    num_colors += 1
                color_instance = time

            if num_colors > 1:
                color_instance = multi
                self.text_colors.append(color_instance)
            else:
                self.text_colors.append(color_instance)


def main(decklist, card_db):
    """ main function """
    # pylint: disable = global-variable-undefined, invalid-name
    import deck as dk
    global app

    mydeck = dk.Deck(decklist, card_db, sort='type_cost')

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
