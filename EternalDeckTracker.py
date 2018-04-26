""" main function for EternalDeckTracker """

import DeckTrackerGUI as dtg

DECKLIST = 'deck.csv'
CARD_DB = 'eternal-cards-1.31.json'

dtg.main(DECKLIST, CARD_DB)
