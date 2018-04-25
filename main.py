import new_gui as ng
import deck as dk


DECKLIST = 'deck.csv'
CARD_DB = 'eternal-cards-1.31.json'
mydeck = dk.Deck(DECKLIST, CARD_DB)

ng.main(mydeck)
