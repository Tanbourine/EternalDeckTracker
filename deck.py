""" deck object to self sort ALPHA, TYPE_alpha_cost, TYPE_cost_alpha, COST_alpha
    caps is major category, lower is tiebreakers
    returns list -> [name, type, cost, key, quantity]"""

import card as cd



class Deck():

    """ deck object to self sort ALPHA, TYPE_alpha_cost, TYPE_cost_alpha, COST_alpha
        caps is major category, lower is tiebreakers
        returns list -> [name, type, cost, key, quantity]"""


    def __init__(self, decklist_file, card_db_file):

        self.csv_deck = cd.import_deck(decklist_file)
        self.card_db = cd.import_json(card_db_file)
        self.keyed_decklist = cd.create_keyed_decklist(self.csv_deck, self.card_db)

        # create deck
        self.decklist = self.create_card_obj_deck()

        self.holding_arr = []

        for index, card in enumerate(self.decklist):
            self.holding_arr.append(
                [card.name, card.card_type, card.cost,
                 self.keyed_decklist[index][0], self.keyed_decklist[index][1],
                 0.0])

        # default deck sorting is type_alpha
        self.deck_sort('type_alpha')

        # initalize card probability
        self.update_probability()

        # save starting quantities of power cards
        temp_deck = self.deck
        self.starting_power = temp_deck

    def create_card_obj_deck(self):
        """ takes keyed decklist and returns a list of Card objects """
        self.deck_obj = []
        for card in self.keyed_decklist:
            self.deck_obj.append(cd.Card(card, self.card_db))

        return self.deck_obj

    def cost_alpha(self):  # pylint: disable=no-self-use
        """ comes as is from eternal """
        return self.holding_arr

    def alpha(self):
        """ sorts alphabetical """
        alpha_arr = sorted(self.holding_arr)
        return alpha_arr

    def type_alpha(self):
        """ sorts by type then alpha then cost
            returns [units, spells, power] """

        units_arr, spells_arr, power_arr = self.type_cost()

        units_arr.sort()
        spells_arr.sort()
        power_arr.sort()

        return units_arr, spells_arr, power_arr

    def type_cost(self):
        """ sorts by type then color then alpha
            returns [units, spells, power] """
        spells_arr = []
        power_arr = []
        units_arr = []

        # organize by type
        for card in self.holding_arr:
            if card[1].lower(
            ) in ["spell", "fast spell", "curse", "cursed relic",
                  "relic", "weapon", "relic weapon"]:
                spells_arr.append(card)

            elif card[1].lower() in ["power"]:
                power_arr.append(card)

            else:
                units_arr.append(card)

        return units_arr, spells_arr, power_arr

    def deck_sort(self, sort_method):
        """ sorts the deck by specified method
            Available sorts:
            'type_alpha', 'type_cost', 'alpha', 'cost_alpha' """

        if sort_method == 'type_alpha':
            self.deck = self.type_alpha()

        elif sort_method == 'type_cost':
            self.deck = self.type_cost()

        elif sort_method == 'alpha':
            self.deck = self.alpha()

        elif sort_method == 'cost_alpha':
            self.deck = self.cost_alpha()

        else:
            print("ERROR: Sort method not available")

    def count_unique(self):
        """ counts number of unique cards in deck """
        units_arr, spells_arr, power_arr = self.type_cost()

        units = len(units_arr)
        spells = len(spells_arr)
        power = len(power_arr)

        total_cards = units + spells + power

        return units, spells, power, total_cards

    def count(self):
        """ counts quantity of cards left in deck """

        units = 0
        spells = 0
        power = 0

        units_arr, spells_arr, power_arr = self.type_cost()

        for card in units_arr:
            units += card[4]

        for card in spells_arr:
            spells += card[4]

        for card in power_arr:
            power += card[4]

        total_cards = units + spells + power

        return units, spells, power, total_cards

    def subtract_card(self, card_type, index):
        """ subtract one to the card given the index in the deck
            card_type = 0 for units, 1 for spells, 2 for power
            index = position in deck array
            return -> decklist with updated quantity
            NOTE: This is not the json key! """

        if self.deck[card_type][index][4] > 0:
            self.deck[card_type][index][4] -= 1
            print("Subtracted", self.deck[card_type][index][0], ':', 'You have',
                  self.deck[card_type][index][4], 'left')

        else:
            print("SUBTRACT_ERROR: Cannot have less than zero cards")

        self.update_probability()

    def add_card(self, card_type, index):
        """ add one to the card given the index in the deck
            card_type = 0 for units, 1 for spells, 2 for power
            index = position in deck array
            return -> decklist with updated quantity
            NOTE: This is not the json key! """

        if self.deck[card_type][index][4] < 4:
            self.deck[card_type][index][4] += 1
            print("Added", self.deck[card_type][index][0], ':', 'You have',
                  self.deck[card_type][index][4], 'left')

        elif self.deck[card_type][index][1] == 'Power':
            # check how many lands are in original deck
            # to make sure cannot go more than max

            if self.deck[card_type][index][0] in ['Fire Sigil', 'Primal Sigil',
                                                  'Shadow Sigil',
                                                  'Justice Sigil', 'Time Sigil']:
                self.deck[card_type][index][4] += 1
                print("Added", self.deck[card_type][index][0], ':', 'You have',
                      self.deck[card_type][index][4], 'left')


                # # if current num of pwr cards is less than starting num of pwr
                # print(self.starting_power[2][index][4])
                # if self.deck[card_type][index][4] < self.starting_power[card_type][index][4]:
                    # self.deck[card_type][index][4] += 1
                    # print(
                        # "Added", self.deck[card_type][
                            # index][0], ':', 'You have', self.deck[card_type][index][4], 'left')
                # else:
                    # print(
                        # "ADD_ERROR: Cannot have more power cards than starting amount")

            elif self.deck[card_type][index][4] < 4:
                self.deck[card_type][index][4] += 1
                print("Added", self.deck[card_type][index][0], ':', 'You have',
                      self.deck[card_type][index][4], 'left')

            else:
                print("ADD_ERROR: Cannot have more than 4 of the same cards")

        else:
            print("ADD_ERROR: Cannot have more than 4 of the same cards")

        self.update_probability()

    def update_probability(self):
        """ updates probabilty of drawing cards """

        card_count = self.count()

        for card_type in self.deck:
            for card in card_type:
                probability = card[4] / card_count[3]
                card[5] = probability * 100

    def merge_types(self):
        """ merges the three type sections into one large array """
        merged_deck = []
        for card_type in self.deck:
            merged_deck.extend(card_type)
        return merged_deck

    def probability(self):
        """ returns a list of probabilities """
        prob_arr = []
        merged_deck = self.merge_types()
        for card in merged_deck:
            prob_arr.append(card[5])

        return prob_arr

    def card_names(self):
        """ returns array of card names in index order """
        name_arr = []

        for card in self.merge_types():
            name_arr.append(card[0])

        return name_arr





def main():
    # pylint: disable=too-many-statements, unused-variable, too-many-locals
    """ main function """

    DECKLIST = 'deck.csv'
    CARD_DB = 'eternal-cards-1.31.json'

    # create deck from keyed_decklist
    deck = Deck(DECKLIST, CARD_DB)

    print(deck.deck_obj[0].name)


    # card_type = 2
    # card_index = 4

    # print('You have', deck.deck[card_type][card_index][4],
          # deck.deck[card_type][card_index][0])
    # print('')

    # deck.subtract_card(card_type, card_index)
    # print('Probabilty of drawing', deck.deck[card_type][card_index][0], ':',
          # '{0: .2f}'.format(deck.deck[card_type][card_index][5]), '%')
    # print('')
    # deck.add_card(card_type, card_index)
    # print('Probabilty of drawing', deck.deck[card_type][card_index][0], ':',
          # '{0: .2f}'.format(deck.deck[card_type][card_index][5]), '%')
    # print('')
    # deck.add_card(card_type, card_index)
    # print('Probabilty of drawing', deck.deck[card_type][card_index][0], ':',
          # '{0: .2f}'.format(deck.deck[card_type][card_index][5]), '%')
    # print('')

if __name__ == "__main__":
    main()
