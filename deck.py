""" deck object to self sort ALPHA, TYPE_alpha_cost, TYPE_cost_alpha, COST_alpha
    caps is major category, lower is tiebreakers
    returns list -> [name, type, cost, key, quantity]"""

import card as cd

DECKLIST = 'deck.csv'
CARD_DB = 'eternal-cards-1.31.json'


class Deck():

    """ self sorting list of cards """

    def __init__(self, keyed_decklist, card_db):
        self.keyed_decklist = keyed_decklist
        self.card_db = card_db
        self.decklist = cd.create_card_obj_deck(keyed_decklist, card_db)

        self.holding_arr = []

        for index, card in enumerate(self.decklist):
            self.holding_arr.append(
                [card.name(), card.type(), card.cost(),
                 self.keyed_decklist[index][0], self.keyed_decklist[index][1]])

    def cost_alpha(self):  # pylint: disable=no-self-use
        """ comes as is from eternal """
        # for index, card in enumerate(self.decklist):
            # cost_alpha_arr.append(
                # [card.name(), card.type(), card.cost(),
                 # self.keyed_decklist[index][0],
                 # self.keyed_decklist[index][1]])

        return self.holding_arr

    def alpha(self):
        """ sorts alphabetical """
        # alpha_arr = []
        # for index, card in enumerate(self.decklist):
            # alpha_arr.append(
                # [card.name(), card.type(), card.cost(),
                 # self.keyed_decklist[index][0],
                 # self.keyed_decklist[index][1]])

        alpha_arr = sorted(self.holding_arr)

        return alpha_arr

    def type_alpha_cost(self):
        """ sorts by type then alpha then cost
            returns [units, spells, power] """
        spells_arr = []
        power_arr = []
        units_arr = []

        # for index, card in enumerate(self.decklist):
            # alpha_arr.append(
                # [card.name(), card.type(), card.cost(),
                 # self.keyed_decklist[index][0],
                 # self.keyed_decklist[index][1]])

            # holding_arr.append(
                # [card.name(), card.type(), card.cost(), self.keyed_decklist[index]])

        # organize by type
        for card in self.holding_arr:
            if card[1].lower(
            ) in ["spell", "fast spell", "curse", "cursed relic",
                  "relic"]:
                spells_arr.append(card)

            elif card[1].lower() in ["power"]:
                power_arr.append(card)

            else:
                units_arr.append(card)

        spells_arr.sort()
        power_arr.sort()
        units_arr.sort()

        type_alpha_cost_arr = [units_arr, spells_arr, power_arr]
        return type_alpha_cost_arr

    def type_cost_alpha(self):
        """ sorts by type then color then alpha
            returns [units, spells, power] """
        spells_arr = []
        power_arr = []
        units_arr = []

        # holding_arr = []
        # for index, card in enumerate(self.decklist):
            # holding_arr.append(
                # [card.name(), card.type(), card.cost(),
                 # self.keyed_decklist[index][0],
                 # self.keyed_decklist[index][1]])

            # holding_arr.append([card.name(), card.type(), card.cost(),
                                # self.keyed_decklist[index]])

        # organize by type
        for card in self.holding_arr:
            if card[1].lower(
            ) in ["spell", "fast spell", "curse", "cursed relic",
                  "relic"]:
                spells_arr.append(card)

            elif card[1].lower() in ["power"]:
                power_arr.append(card)

            else:
                units_arr.append(card)

        type_alpha_cost_arr = [units_arr, spells_arr, power_arr]
        return type_alpha_cost_arr


def main():
    """ main function """
    deck, card_names = cd.import_deck(DECKLIST)
    card_db = cd.import_json(CARD_DB)
    keyed_decklist = cd.create_keyed_decklist(deck, card_names, card_db)

    deck = Deck(keyed_decklist, card_db)
    cost_alpha_deck = deck.cost_alpha()
    alpha_deck = deck.alpha()
    type_cost_deck = deck.type_cost_alpha()
    type_alpha_deck = deck.type_alpha_cost()

    print('Cost Alpha')
    print(cost_alpha_deck)
    print('')
    print('===============')
    print('===============')
    print('')

    print('Alpha')
    print(alpha_deck)
    print('')
    print('===============')
    print('===============')
    print('')

    print('Type, Alpha')
    print(type_alpha_deck[0])
    print('------------')
    print(type_alpha_deck[1])
    print('------------')
    print(type_alpha_deck[2])

    print('')
    print('===============')
    print('===============')
    print('')

    print('Type, Cost')
    print(type_cost_deck[0])
    print('------------')
    print(type_cost_deck[1])
    print('------------')
    print(type_cost_deck[2])

    print('')
    print('===============')
    print('===============')
    print('')

    print('To get quantity of a card...')
    print(type_alpha_deck[0][0][4])


if __name__ == "__main__":
    main()
