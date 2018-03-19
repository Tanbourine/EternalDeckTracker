import csv

decklist = 'deck.csv'
data = []
deck = []


def importDeck(decklist):
    global num_lines
    with open(decklist, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            index = line[0]
            card = line[1]

            data.append([index, card])

    num_lines = int(data[-1][0])
    # Formatting into [quantity, name]
    for i in range(0, num_lines):
        quantity = int(data[i][1][0:2])
        name_with_setnumber = data[i][1][2:-11]
        deck.append([quantity, name_with_setnumber.strip()])


def getName(index):
    # input index to get name of card
    cardName = deck[index][1]
    # print(cardName)
    return cardName


def getQuantity(index):
    cardQuantity = deck[index][0]
    return cardQuantity


def cardInfo(index):
    cardQuantity = getQuantity(index)
    cardName = getName(index)
    print('You have ' + str(cardQuantity) + ' of ' + cardName)


def deckSize():
    deckSize = 0
    for i in range(0, num_lines):
        deckSize += getQuantity(i)
    return deckSize


def displayDeck():
    for i in range(0, num_lines):
        print(str(i).zfill(2) + ' - ' + str(deck[i][0]) + ' - ' + deck[i][1])


def subtractCard(index):
    deck[index][0] = deck[index][0] - 1


def addCard(index):
    deck[index][0] = deck[index][0] + 1


def userInteract():
    action = input("What would you like to do? >>> ")

    if action == 'dd':  # Display what's left in the deck
        displayDeck()

    elif action == 's':  # Subtract a card - it's being played!
        index = input("Which card is being played? >>> ")
        if index.isdigit():  # if it's able to be an int
            index = int(index)
            subtractCard(index)
            print('---')
            print('Removed 1 of ' + getName(index))
            print('You have ' + str(getQuantity(index)) + ' left')
            print('---')
            displayDeck()

    elif action == 'a':  # Add a card - you messed up!
        index = input("Which card is being added? >>> ")
        if index.isdigit():
            index = int(index)
            addCard(index)
            print('---')
            print('Added 1 of ' + getName(index))
            print('You have ' + str(getQuantity(index)) + ' left')
            print('---')
            displayDeck()

    elif action == 'p':  # Probability page!
        print('in work, need more metadata')

    elif action == 'r':  # Reset deck!
        importDeck(decklist)

    else:  # catch all typos
        print('Not Allowed')

    print('---')
    print('You have ' + str(deckSize()) + ' cards left')


def main():
    importDeck(decklist)
    while(True):
        userInteract()


main()
