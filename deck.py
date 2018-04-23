""" deck object to self sort ALPHA, TYPE_cost_alpha, COST_alpha
    caps is major category, lower is tiebreakers"""

import card as cd

DECKLIST = 'deck.csv'
CARD_DB = 'eternal-cards-1.31.json'


class Deck():
    """ self sorting list of cards """

    def __init__(self, keyed_decklist, card_database):
        self.decklist = cd.create_card_obj_deck(keyed_decklist, card_database)

    def alpha_sort(self):
        """ sorts alphabetical """
        alpha_arr = []
        for card in self.decklist:
            alpha_arr.append(card.name())

        alpha_arr.sort()
        return alpha_arr

    def type_cost_alpha(self):
        """ sorts by type then color then alpha """
        holding_arr = []
        spells_arr = []
        power_arr = []
        units_arr = []

        for card in self.decklist:
            holding_arr.append([card.name(), card.type(), card.cost()])

        # organize into spells
        for card in holding_arr:
            card[1] = card[1].lower()
            if card[1] in ["spell", "fast spell", "curse", "cursed relic",
                           "relic"]:
                spells_arr.append(card[0])

            elif card[1] in ["power"]:
                power_arr.append(card[0])

            else:
                units_arr.append(card[0])

        # print(spells_arr)
        # print('------------')
        # print(power_arr)
        # print('------------')
        # print(units_arr)
        # print('------------')


def main():
    """ main function """
    deck, card_names = cd.import_deck(DECKLIST)
    card_db = cd.import_json(CARD_DB)
    keyed_decklist = cd.create_keyed_decklist(deck, card_names, card_db)

    deck = Deck(keyed_decklist, card_db)
    # alpha_deck = deck.alpha_sort()
    type_deck = deck.type_cost_alpha()


if __name__ == "__main__":
    main()
