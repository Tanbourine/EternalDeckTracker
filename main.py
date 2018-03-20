import DeckTracker as dt
import tkinter as tk

decklist = 'noIndex.csv'

# Init Tkinter


def initGUI(deck, num_lines):
    numCards = []
    addCard = []
    cardName = []

    root = tk.Tk()
    root.geometry("300x800+300+300")
    root.resizable(width=True, height=True)
    frame = tk.Frame(root)

    for i in range(num_lines):
        numCards.append(tk.StringVar())
        numCards[i].set(str(deck[i][0]).zfill(2))

        # Create line
        cardName.append(tk.Button(root, text=deck[i][1], command=lambda i=i: subtractCard(i)))

        addCard.append(tk.Button(root, textvariable=numCards[i], command=lambda i=i: addCard(i)))

        # Organize and pack lines
        cardName[i].grid(row=i, column=0, sticky=tk.W)
        addCard[i].grid(row=i, column=1, sticky=tk.W)

    def addCard(index):
        newQuantity = deck[index][0] + 1
        deck[index][0] = newQuantity
        numCards[index].set(str(newQuantity).zfill(2))

    def subtractCard(index):
        newQuantity = deck[index][0] - 1
        deck[index][0] = newQuantity
        numCards[index].set(str(newQuantity).zfill(2))

    root.mainloop()


def main():
    deck, num_lines = dt.importDeck(decklist)
    initGUI(deck, num_lines)


main()
