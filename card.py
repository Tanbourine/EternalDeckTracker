""" Imports eternal cards and creates objects with card properties """

import csv
import json

# class Card():
# """ card object that links properties with names """

# def __init__(self, card_name):
# self.card_name = card_name


def import_json(json_file):
    """ takes in json and outputs a dictionary """
    with open(json_file) as jsonfile:
        parsed_json = json.load(jsonfile)
    return parsed_json


def import_deck(decklist):
    """ import csv file to array """
    deck = []
    with open(decklist, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Importting and formatting into [quantity, name]
        for card in csv_reader:

            quantity = int(card[0][0:2])

            find_parathesis = card[0].find("(")
            name = card[0][2:find_parathesis]

            deck.append([quantity, name.strip()])

    return deck


def print_all_json(jsonfile, keyword):
    """  whole json given a specific keyword """
    # keywords -> SetNumber, EternalID, Name, CardText, Cost, Influence, Attack,
    # Health, Rarity, Type, ImageUrl
    for card in enumerate(jsonfile):
        print(card[1][keyword])         # [index, json[keyword]]


def match_card_keys(deck, card_database):
    """ takes decklist csv and returns dict of {cardname:index} """

    card_names = []
    card_key = {}
    for card in deck:
        card_names.append(card[1])

    for card in card_names:
        for index, db_card in enumerate(card_database):
            if card in db_card["Name"]:
                card_key[card_database[index]["Name"]] = index

    print(card_key)
    return card_key


def get_card_keys(deck, card_database):
    """ takes decklist csv and returns list of corresponding keys """

    card_names = []
    deck_keys = []

    # strip card quantity
    for card in deck:
        card_names.append(card[1])

    for card in card_names:
        for index, db_card in enumerate(card_database):
            if card in db_card["Name"]:
                deck_keys.append(index)

    return deck_keys


def card_index_to_name(deck_keys, card_database):
    """ takes deck_keys and translates back to names to print """

    decklist_to_print = []
    for card in deck_keys:
        decklist_to_print.append(card_database[card]["Name"])

    return decklist_to_print

# def get_cost(card, card_key, card_database):
    # """ takes car


def main():
    """ main function """
    decklist = 'deck.csv'
    card_database_json_file = 'eternal-cards-1.31.json'
    deck = import_deck(decklist)
    card_database = import_json(card_database_json_file)
    # print_all_json(card_database, "Name")
    # print(card_database[0]["Name"])
    # card_keys = match_card_keys(deck, card_database)
    deck_keys = get_card_keys(deck, card_database)
    decklist_to_print = card_index_to_name(deck_keys, card_database)
    print(decklist_to_print)


if __name__ == "__main__":
    main()
