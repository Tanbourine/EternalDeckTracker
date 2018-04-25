""" testing importing """
import deck as dk
import card as cd
import pprint

DECKLIST = 'deck.csv'
CARD_DB = 'eternal-cards-1.31.json'


def main():
    """ main """
    # pylint: disable=too-many-statements

    deck = dk.Deck(DECKLIST, CARD_DB)

    card_type = 0
    card_index = 3

    print('If you know the name of the card you can search for it')
    print('')
    searching_for = "Crystallize"
    print('Searching for card:', searching_for)
    print('')
    searched_card = deck.card_search(searching_for)
    print('You can now get any attribute you want for that card')
    print('Searched card name:', searched_card.name)
    print('Searched card cost:', searched_card.cost)
    print('')
    print('')
    print('')

    print('Selected card is:', deck.deck[card_type][card_index].name)
    print('Its cost is:',deck.deck[card_type][card_index].cost)
    print('Its rarity is:',deck.deck[card_type][card_index].rarity)
    print('Its influence requirement is:',deck.deck[card_type][card_index].influence)
    print('Its probability to draw in this deck is:', '{0: .2f}'.format(deck.deck[card_type][card_index].probability))

    print('')

    print('')
    deck.add_card(card_type, card_index)
    print('Its probability to draw in this deck is:', '{0: .2f}'.format(deck.deck[card_type][card_index].probability))

    print('')
    deck.subtract_card(card_type, card_index)
    print('Its probability to draw in this deck is:', '{0: .2f}'.format(deck.deck[card_type][card_index].probability))

    print('')
    deck.subtract_card(card_type, card_index)
    print('Its probability to draw in this deck is:', '{0: .2f}'.format(deck.deck[card_type][card_index].probability))

    print('')
    deck.subtract_card(card_type, card_index)
    print('Its probability to draw in this deck is:', '{0: .2f}'.format(deck.deck[card_type][card_index].probability))

    print('')
    deck.subtract_card(card_type, card_index)
    print('Its probability to draw in this deck is:', '{0: .2f}'.format(deck.deck[card_type][card_index].probability))

    print('')
    deck.subtract_card(card_type, card_index)
    print('Its probability to draw in this deck is:', '{0: .2f}'.format(deck.deck[card_type][card_index].probability))

    print('')
    print('')
    print('Printing list of all selected parameters')
    deck.deck_sort('type_alpha')
    print('List is sorted by:', deck.sort_method)
    print('')
    print('')

    # JSON Keywords -> SetNumber, EternalID, Name, CardText, Cost, Influence, Attack,
    # Health, Rarity, Type, ImageUrl, Quantity*, Probability*
    # *is custom!
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(deck.show_property('Name', 'Quantity', 'Cost', 'Rarity', 'Type', 'Probability'))




if __name__ == "__main__":
    main()
