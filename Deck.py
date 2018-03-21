


#Deck Class

class Deck:
	cards = []
	totalCards = 0
	numLines = 0
	def __init__(self, deckName):
		self.deckName = deckName

	def addCard(self, card):
		self.cards.append(card)
		self.totalCards += card.quantity
		self.numLines += 1

	def findProb(self, card):
	 	probability = card.quantity / self.totalCards
	 	return probability



#Card Object

class Card(Deck):

	def __init__(self, cardName, quantity):
		self.cardName = cardName
		self.quantity = quantity




a = Deck('Pokemon')
x = Card('Name', 4)
y = Card('Nombre', 8)

print(a.totalCards)
print(x.cardName)
print(x.quantity)
print(y.cardName)
print(y.quantity)

a.addCard(x)
a.addCard(y)

print('total cards are: ' + str(a.totalCards))

for i in range(a.numLines):
	print(a.cards[i].cardName + ' ' + str(a.cards[i].quantity))

print('\n')
print(a.findProb(x))

