""" testing importing """
import deck as dk
import card as cd

DECKLIST = 'deck.csv'
CARD_DB = 'eternal-cards-1.31.json'


def main():
    """ main """

    deck= cd.import_deck(DECKLIST)
    card_db = cd.import_json(CARD_DB)
    keyed_decklist = cd.create_keyed_decklist(deck, card_db)

    deck = dk.Deck(keyed_decklist, card_db)
    print(deck.deck)



if __name__ == "__main__":
    main()
