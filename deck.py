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
        self.raw_deck = self.create_card_obj_deck()


        # default deck sorting is type_alpha
        self.sort_method = 'type_alpha'
        self.deck = self.deck_sort(self.sort_method)

        # initalize card probability
        self.update_probability()

        # save starting quantities of power cards
        self.starting_power = self.get_starting_power()

    def create_card_obj_deck(self):
        """ takes keyed decklist and returns a list of Card objects """
        self.deck_obj = []
        for card in self.keyed_decklist:
            self.deck_obj.append(cd.Card(card, self.card_db))

        return self.deck_obj

    def get_starting_power(self):
        """ creates dict of {power name : starting quantity} """
        starting_power = {}
        for card_type in self.deck:
            for card in card_type:
                if card.card_type == 'Power':
                    starting_power[card.name] = card.quantity

        return starting_power

    def cost_alpha(self):  # pylint: disable=no-self-use
        """ comes as is from eternal """
        cost_alpha_arr = sorted(self.raw_deck, key=lambda x: x.cost)
        return cost_alpha_arr

    def alpha(self):
        """ sorts alphabetical """
        alpha_arr = sorted(self.raw_deck, key=lambda x: x.name)
        return alpha_arr

    def type_alpha(self):
        """ sorts by type then alpha then cost
            returns [units, spells, power] """

        units_arr, spells_arr, power_arr = self.type_cost()

        units_arr.sort(key=lambda x: x.name)
        spells_arr.sort(key=lambda x: x.name)
        power_arr.sort(key=lambda x: x.name)

        return units_arr, spells_arr, power_arr

    def type_cost(self):
        """ sorts by type then color then alpha
            returns [units, spells, power] """
        spells_arr = []
        power_arr = []
        units_arr = []


        # organize by type
        for card in self.raw_deck:
            if card.card_type.lower(
            ) in ["spell", "fast spell", "curse", "cursed relic",
                  "relic", "weapon", "relic weapon"]:
                spells_arr.append(card)

            elif card.card_type.lower() in ["power"]:
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
            self.sort_method = 'type_alpha'

        elif sort_method == 'type_cost':
            self.deck = self.type_cost()
            self.sort_method = 'type_cost'

        elif sort_method == 'alpha':
            self.deck = self.alpha()
            self.sort_method = 'alpha'

        elif sort_method == 'cost_alpha':
            self.deck = self.cost_alpha()
            self.sort_method = 'cost_alpha'

        else:
            print("ERROR: Sort method not available")

        return self.deck

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
            units += card.quantity

        for card in spells_arr:
            spells += card.quantity

        for card in power_arr:
            power += card.quantity

        total_cards = units + spells + power

        return units, spells, power, total_cards

    def subtract_card(self, card_type, index):
        """ subtract one to the card given the index in the deck
            card_type = 0 for units, 1 for spells, 2 for power
            index = position in deck array
            return -> decklist with updated quantity
            NOTE: This is not the json key! """

        if self.deck[card_type][index].quantity > 0:
            self.deck[card_type][index].quantity -= 1
            print("Subtracted", self.deck[card_type][index].name, ':', 'You have',
                  self.deck[card_type][index].quantity, 'left')

        else:
            print("SUBTRACT_ERROR: Cannot have less than zero cards")

        self.update_probability()

    def add_card(self, card_type, index):
        """ add one to the card given the index in the deck
            card_type = 0 for units, 1 for spells, 2 for power
            index = position in deck array
            return -> decklist with updated quantity
            NOTE: This is not the json key! """

        if self.deck[card_type][index].quantity < 4:
            self.deck[card_type][index].quantity += 1
            print("Added", self.deck[card_type][index].name, ':', 'You have',
                  self.deck[card_type][index].quantity, 'left')

        elif self.deck[card_type][index].card_type == 'Power':
            # check how many lands are in original deck
            # to make sure cannot go more than max

            if self.deck[card_type][index].name in ['Fire Sigil', 'Primal Sigil',
                                                  'Shadow Sigil',
                                                  'Justice Sigil', 'Time Sigil']:

                # if current num of pwr cards is less than starting num of pwr
                if self.deck[card_type][index].quantity < self.starting_power[self.deck[card_type][index].name]:
                    self.deck[card_type][index].quantity += 1
                    print(
                        "Added", self.deck[card_type][
                            index].name, ':', 'You have', self.deck[card_type][index].quantity, 'left')
                else:
                    print(
                        "ADD_ERROR: Cannot have more power cards than starting amount")

            elif self.deck[card_type][index].quantity < 4:
                self.deck[card_type][index].quantity += 1
                print("Added", self.deck[card_type][index].name, ':', 'You have',
                      self.deck[card_type][index].quantity, 'left')

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
                probability = card.quantity / card_count[3]
                card.probability = probability * 100

    def merge_types(self):
        """ merges the three type sections into one large array """
        merged_deck = []
        if self.sort_method in ['type_cost', 'type_alpha']:
            for card in self.deck:
                merged_deck.extend(card)

        if self.sort_method in ['alpha', 'cost_alpha']:
            for card in self.deck:
                merged_deck.append(card)
        return merged_deck


    def card_names(self):
        """ returns array of card names in index order """
        name_arr = []

        for card in self.merge_types():
            name_arr.append(card.name)

        return name_arr

    def show_property(self, *args):
        """ returns a list of whatever keys you input """ 
        # keywords -> SetNumber, EternalID, Name, CardText, Cost, Influence, Attack,
        # Health, Rarity, Type, ImageUrl
        output_arr = []


        for card in self.merge_types():
            properties = []
            for keys in args:
                if keys == 'Quantity':
                    properties.append(card.quantity)

                elif keys == 'Probability':
                    properties.append(card.probability)

                else:
                    properties.append(card.card_data[keys])

            output_arr.append(properties)

        return output_arr

    def card_search(self, card_name):
        """ Given the name of a card, return a card object """
        found_card = 0
        for card_types in self.deck:
            for card in card_types:
                if card.name == card_name:
                    found_card = card
        if found_card:
            return found_card

        else:
            print('Card does not exist. Check spelling!')
            return None
            





def main():
    # pylint: disable=too-many-statements, unused-variable, too-many-locals
    """ main function """

    DECKLIST = 'deck.csv'
    CARD_DB = 'eternal-cards-1.31.json'

    # create deck from keyed_decklist
    deck = Deck(DECKLIST, CARD_DB)


    # print(deck.show_property('Name'))

    card_type = 2
    card_index = 3

    print('You have', deck.deck[card_type][card_index].quantity,
          deck.deck[card_type][card_index].name)
    print('')



    deck.subtract_card(card_type, card_index)
    print('Probabilty of drawing', deck.deck[card_type][card_index].name, ':',
          '{0: .2f}'.format(deck.deck[card_type][card_index].probability), '%')
    print('')


    deck.subtract_card(card_type, card_index)
    print('Probabilty of drawing', deck.deck[card_type][card_index].name, ':',
          '{0: .2f}'.format(deck.deck[card_type][card_index].probability), '%')
    print('')

    deck.subtract_card(card_type, card_index)
    print('Probabilty of drawing', deck.deck[card_type][card_index].name, ':',
          '{0: .2f}'.format(deck.deck[card_type][card_index].probability), '%')
    print('')


    deck.add_card(card_type, card_index)
    print('Probabilty of drawing', deck.deck[card_type][card_index].name, ':',
          '{0: .2f}'.format(deck.deck[card_type][card_index].probability), '%')
    print('')

    deck.add_card(card_type, card_index)
    print('Probabilty of drawing', deck.deck[card_type][card_index].name, ':',
          '{0: .2f}'.format(deck.deck[card_type][card_index].probability), '%')
    print('')

    deck.add_card(card_type, card_index)
    print('Probabilty of drawing', deck.deck[card_type][card_index].name, ':',
          '{0: .2f}'.format(deck.deck[card_type][card_index].probability), '%')
    print('')

    deck.add_card(card_type, card_index)
    print('Probabilty of drawing', deck.deck[card_type][card_index].name, ':',
          '{0: .2f}'.format(deck.deck[card_type][card_index].probability), '%')
    print('')

    deck.add_card(card_type, card_index)
    print('Probabilty of drawing', deck.deck[card_type][card_index].name, ':',
          '{0: .2f}'.format(deck.deck[card_type][card_index].probability), '%')
    print('')

if __name__ == "__main__":
    main()
