""" testing importing """
import deck as dk
import card as cd

DECKLIST = 'deck.csv'
CARD_DB = 'eternal-cards-1.31.json'


def main():
    """ main """

    deck, card_names = cd.import_deck(DECKLIST)
    card_db = cd.import_json(CARD_DB)
    keyed_decklist = cd.create_keyed_decklist(deck, card_names, card_db)

    deck = dk.Deck(keyed_decklist, card_db)
    type_alpha_deck = deck.type_alpha()

    # returns list -> [name, type, cost, key, quantity]

    print('Sorted by TYPE, then by ALPHA')
    print('====================')
    print('')
    print('====================')
    print('====== UNITS =======')
    print('====================')
    print('')
    print(type_alpha_deck[0])
    print('')
    print('====================')
    print('====== SPELLS ======')
    print('====================')
    print('')
    print(type_alpha_deck[1])
    print('')
    print('====================')
    print('====== POWER =======')
    print('====================')
    print('')
    print(type_alpha_deck[2])
    print('')
    print('====================')
    print('====================')

    for i in range(5):
        print(type_alpha_deck[0][0][i])


if __name__ == "__main__":
    main()
