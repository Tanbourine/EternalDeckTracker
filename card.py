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

            # cards[i] = Card(name, quantity)
            # deckObj.addCard(cards[i])
            deck.append([quantity, name.strip()])

            num_lines = len(deck)

    return deck, num_lines


def print_all_json(jsonfile, keyword):
    """  whole json given a specific keyword """
    # keywords -> SetNumber, EternalID, Name, CardText, Cost, Influence, Attack,
    # Health, Rarity, Type, ImageUrl
    for card in enumerate(jsonfile):
        print(card[1][keyword])         # [index, json[keyword]]


def match_card_metadata(deck, card_database):
    """ matches card names pulled from csv with metadata from json library
    takes card names from deck and searches for it in card_database["Name"]
    Need to use a find() function to get json index of matched name to reference
    all metadata
    Also need to figure out how to fix 'int object is not scritable' """

    for card in deck:
        for index in card_database:
            if card[0][1] == index["Name"]:
                print(index["Name"])

    # for i, j in enumerate(deck):
        ## [[0, decklist], [1, num_lines]]
        # print(j[0][1])

        # print(i)
        # print(j)


def main():
    """ main function """
    decklist = 'deck.csv'
    card_database_json_file = 'eternal-cards-1.31.json'
    deck = import_deck(decklist)
    card_database = import_json(card_database_json_file)
    #print_all_json(parsed_json, "Name")
    match_card_metadata(deck, card_database)


main()
