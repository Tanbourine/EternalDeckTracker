""" testing importing """
import deck as dk
import card as cd

DECKLIST = 'deck.csv'
CARD_DB = 'eternal-cards-1.31.json'


def main():
    """ main """


    deck = dk.Deck(DECKLIST, CARD_DB)
    print(deck.card_names())



if __name__ == "__main__":
    main()
