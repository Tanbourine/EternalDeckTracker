""" testing importing """
import deck as dk
import card as cd
import pprint

DECKLIST = 'deck.csv'
CARD_DB = 'eternal-cards-1.31.json'


def main():
    """ main """
    # pylint: disable=too-many-statements

    mydeck = dk.Deck(DECKLIST, CARD_DB)

    card_type = 1
    card_index = 3

    print('If you know the name of the card you can search for it')
    print('')
    searching_for = "Crystallize"
    print('Searching for card:', searching_for)
    print('')
    searched_card = mydeck.card_search(searching_for)
    print('You can now get any attribute you want for that card')
    print('Searched card name:', searched_card.name)
    print('Searched card cost:', searched_card.cost)
    print('')
    print('')
    print('')

    print('Selected card is:', mydeck.deck[card_type][card_index].name)
    print('Its cost is:',mydeck.deck[card_type][card_index].cost)
    print('Its rarity is:',mydeck.deck[card_type][card_index].rarity)
    print('Its influence requirement is:',mydeck.deck[card_type][card_index].influence)
    print('You currently have', mydeck.deck[card_type][card_index].quantity, 'of', mydeck.deck[card_type][card_index].name)
    print('Its probability to draw in this deck is:', '{0: .2f}'.format(mydeck.deck[card_type][card_index].probability))

    print('')

    print('')
    mydeck.add_card(card_type, card_index)
    print('Its probability to draw in this deck is:', '{0: .2f}'.format(mydeck.deck[card_type][card_index].probability))

    print('')
    mydeck.add_card(card_type, card_index)
    print('Its probability to draw in this deck is:', '{0: .2f}'.format(mydeck.deck[card_type][card_index].probability))

    print('')
    mydeck.add_card(card_type, card_index)
    print('Its probability to draw in this deck is:', '{0: .2f}'.format(mydeck.deck[card_type][card_index].probability))

    print('')
    mydeck.add_card(card_type, card_index)
    print('Its probability to draw in this deck is:', '{0: .2f}'.format(mydeck.deck[card_type][card_index].probability))

    print('')
    mydeck.subtract_card(card_type, card_index)
    print('Its probability to draw in this deck is:', '{0: .2f}'.format(mydeck.deck[card_type][card_index].probability))

    print('')
    mydeck.subtract_card(card_type, card_index)
    print('Its probability to draw in this deck is:', '{0: .2f}'.format(mydeck.deck[card_type][card_index].probability))

    print('')
    mydeck.subtract_card(card_type, card_index)
    print('Its probability to draw in this deck is:', '{0: .2f}'.format(mydeck.deck[card_type][card_index].probability))

    print('')
    mydeck.subtract_card(card_type, card_index)
    print('Its probability to draw in this deck is:', '{0: .2f}'.format(mydeck.deck[card_type][card_index].probability))

    print('')
    mydeck.subtract_card(card_type, card_index)
    print('Its probability to draw in this deck is:', '{0: .2f}'.format(mydeck.deck[card_type][card_index].probability))

    print('')
    print('')
    print('Printing list of all selected parameters')
    mydeck.deck_sort('type_alpha')
    print('List is sorted by:', mydeck.sort_method)
    print('')
    print('')

    # JSON Keywords -> SetNumber, EternalID, Name, CardText, Cost, Influence, Attack,
    # Health, Rarity, Type, ImageUrl, Quantity*, Probability*
    # *is custom!
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(mydeck.show_property('Name', 'Quantity', 'Cost', 'Rarity', 'Type', 'Probability'))




if __name__ == "__main__":
    main()
