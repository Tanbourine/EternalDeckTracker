""" testing importing """
import deck as dk
import card as cd

DECKLIST = 'deck.csv'
CARD_DB = 'eternal-cards-1.31.json'


def main():
    """ main """


    deck = dk.Deck(DECKLIST, CARD_DB)
    print(deck.card_names())
    print('First card of deck is:', deck.deck_obj[0].name())
    print('Its cost is:',deck.deck_obj[0].cost())
    print('Its probability to draw in this deck is:', '{0: .2f}'.format(deck.probability()[0]))

    deck.add_card(0,0)
    print('Its probability to draw in this deck is:', '{0: .2f}'.format(deck.probability()[0]))



if __name__ == "__main__":
    main()
