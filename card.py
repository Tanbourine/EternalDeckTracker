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
        self.card_info = card_db[card_key]

        # output_value = []
        # for card in deck_keys:
            # output_value.append(card_database[card][value])

    def setnumber(self):
        """ returns card setnumber """
        return self.card_info["SetNumber"]

    def eternalid(self):
        """ returns card eternalid """
        return self.card_info["EternalID"]

    def name(self):
        """ returns card name """
        return self.card_info["Name"]

    def cardtext(self):
        """ returns card text """
        return self.card_info["CardText"]

    def cost(self):
        """ returns card cost """
        return self.card_info["Cost"]

    def influence(self):
        """ returns card influence """
        return self.card_info["Influence"]

    def attack(self):
        """ returns card attack """
        return self.card_info["Attack"]

    def health(self):
        """ returns card health """
        return self.card_info["Health"]

    def rarity(self):
        """ returns card rarity """
        return self.card_info["Rarity"]

    def type(self):
        """ returns card type """
        return self.card_info["Type"]

    def imageurl(self):
        """ returns card imageurl """
        return self.card_info["ImageUrl"]


def import_json(json_file):
    """ takes in json and outputs a dictionary """
    with open(json_file) as jsonfile:
        parsed_json = json.load(jsonfile)
    return parsed_json


def import_deck(decklist):
    """ import csv file to array
        deck = {card_name : quantity}
        card_name = [card_names] """
    card_names = []
    deck = {}
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

            card_names.append(name)
            deck[name] = quantity

    return deck, card_names


def print_all_json(jsonfile, keyword):
    """  whole json given a specific keyword """
    # keywords -> SetNumber, EternalID, Name, CardText, Cost, Influence, Attack,
    # Health, Rarity, Type, ImageUrl
    for card in enumerate(jsonfile):
        print(card[1][keyword])         # [index, json[keyword]]


def match_card_keys(card_names, card_database):
    """ takes decklist csv and returns dict of {cardname:index} """

    card_key = {}

    for card in card_names:
        for index, db_card in enumerate(card_database):
            if card in db_card["Name"]:
                card_key[card_database[index]["Name"]] = index

    print(card_key)
    return card_key


def get_card_keys(deck, card_names, card_database):
    """ takes decklist csv and returns list of corresponding keys and quantities
    in dict """

    deck_keys = []
    keyed_decklist = {}

    # make list of keys to link decklist and json
    for card in deck:
        for index, db_card in enumerate(card_database):
            if card in db_card["Name"]:
                deck_keys.append(index)


    # make dictionary of {card_key : quantity}
    # this is the new decklist since it can be used to retrieve all json data
    for index, card in enumerate(deck_keys):
        keyed_decklist[card] = deck[card_names[index]]

    return keyed_decklist




def card_index_to_name(deck_keys, card_database):
    """ takes deck_keys and translates back to names to print """

    decklist_to_print = []
    for card in deck_keys:
        decklist_to_print.append(card_database[card]["Name"])

    return decklist_to_print


def get_value(deck_keys, value, card_database):
    """ takes deck keys and returns cost and names """

    output_value = []
    for card in deck_keys:
        output_value.append(card_database[card][value])

    print(output_value)

    return output_value


def main():
    """ main function """
    # keywords -> SetNumber, EternalID, Name, CardText, Cost, Influence, Attack,
    # Health, Rarity, Type, ImageUrl
    deck, card_names = import_deck(DECKLIST)
    card_database = import_json(CARD_DB)

    # print_all_json(card_database, "Name")
    # print(card_database[0]["Name"])
    # card_keys = match_card_keys(card_names, card_database)
    deck_keys = get_card_keys(deck, card_names, card_database)
    # decklist_to_print = card_index_to_name(deck_keys, card_database)
    # output_value = get_value(deck_keys, "Name", card_database)
    # card1 = Card(deck_keys[0], card_database)
    # print(card1.type())


if __name__ == "__main__":
    main()
    # IMPORTED_DECK, CARD_NAMES = import_deck(DECKLIST)
