""" Imports eternal cards and creates objects with card properties """

import csv
import json

DECKLIST = 'deck.csv'
CARD_DB = 'eternal-cards-1.31.json'


class Card():

    """ card object that links properties with names """
    # keywords -> SetNumber, EternalID, Name, CardText, Cost, Influence, Attack,
    # Health, Rarity, Type, ImageUrl

    def __init__(self, card_key, card_db):
        self.card_key = card_key
        self.card_db = card_db
        self.card_data = card_db[card_key[0]]
        self.quantity = card_key[1]
        self.probability = 0.0
        self.setnumber = self.card_data["SetNumber"]
        self.eternalid = self.card_data["EternalID"]
        self.name = self.card_data["Name"]
        self.cardtext = self.card_data["CardText"]
        self.cost = self.card_data["Cost"]
        self.influence = self.card_data["Influence"]
        self.attack = self.card_data["Attack"]
        self.health = self.card_data["Health"]
        self.rarity = self.card_data["Rarity"]
        self.card_type = self.card_data["Type"]
        self.imageurl = self.card_data["ImageUrl"]



def import_json(json_file):
    """ takes in json and outputs a dictionary """
    with open(json_file) as jsonfile:
        parsed_json = json.load(jsonfile)
    return parsed_json



def import_deck(decklist):
    """ import csv file to array
        deck = {card_name : quantity}
        card_name = [card_names] """
    deck = []
    with open(decklist, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Importting and formatting into [quantity, name]
        for card in csv_reader:
            # each line imports like this:
            # 2 Permafrost (Set1 #193)

            # isolating quantity of each card
            quantity = int(card[0][0:2])

            # paranthesis is first non-name char
            find_paranthesis = card[0].find("(")
            name = card[0][2:find_paranthesis]
            name = name.strip()

            deck.append([name, quantity])

    return deck


def create_keyed_decklist(deck, card_db):
    """ takes decklist csv and returns list of corresponding keys and quantities
    in dict """

    deck_keys = []
    keyed_decklist = []

    # make list of keys to link decklist and json
    for card in deck:
        for index, db_card in enumerate(card_db):
            if card[0] in db_card["Name"]:
                deck_keys.append(index)

    # make list of [card_key, quantity]
    # this is the new decklist since it can be used to retrieve all json data
    for index, card in enumerate(deck_keys):
        keyed_decklist.append([card, deck[index][1]])

    return keyed_decklist


def main():
    """ main function """
    # pylint: disable=unused-variable
    # keywords -> SetNumber, EternalID, Name, CardText, Cost, Influence, Attack,
    # Health, Rarity, Type, ImageUrl
    deck = import_deck(DECKLIST)
    card_db = import_json(CARD_DB)
    keyed_decklist = create_keyed_decklist(deck, card_db)
    card1 = Card(keyed_decklist[0], card_db)
    print(card1.name)


if __name__ == "__main__":
    main()
