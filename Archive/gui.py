import tkinter as tk
from tkinter import ttk
import csv

#https://stackoverflow.com/questions/14759444/pyinstaller-not-picking-up-tree-or-data-files

#

decklist = 'noIndex.csv'

LARGE_FONT = ("Verdana", 12)
# deck, num_lines = dt.importDeck(decklist)


class DeckGUI(tk.Tk):
    def __init__(self, *args, **kwargs):

        # Initialize tk inheritance
        tk.Tk.__init__(self, *args, **kwargs)
        #tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "Eternal Deck Tracker")

        # Create master frame
        master = tk.Frame(self)
        master.pack(side="top", fill="both", expand=True)
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        #--------MENUS---------#

        # Create main menu in master
        main_menu = tk.Menu(master)

        #-------FILE MENU------#

        # Create file_menu
        file_menu = tk.Menu(main_menu, tearoff=0)

        # Give file_menu its buttons
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.quit_app)

        # Add file_menu to main_menu
        main_menu.add_cascade(label="File", menu=file_menu)

        #-------OPTIONS MENU------#

        # Create options_menu
        options_menu = tk.Menu(main_menu, tearoff=0)

        # Give options_menu its buttons
        options_menu.add_command(label="Go Home", command=lambda: self.show_frame(StartPage))
        options_menu.add_command(label="Option 1", command=lambda: self.show_frame(PageOne))
        options_menu.add_command(label="Option 2", command=lambda: self.show_frame(PageTwo))
        options_menu.add_separator()
        options_menu.add_command(label="Quit", command=self.quit_app)

        # Add options_menu to main_menu
        main_menu.add_cascade(label="Options", menu=options_menu)

        # ------- Font Menu ---------#

        # Create variables for font_menu to manipulate
        text_font = tk.StringVar()
        text_font.set("Times")

        # function to display font when clicked
        def change_font(event=None):
            print("Font Picked :", text_font.get())

        # Create font_menu
        font_menu = tk.Menu(main_menu, tearoff=0)

        # Add checkbox buttons to font_menu
        font_menu.add_radiobutton(label="Times",
                                  variable=text_font,
                                  command=change_font)

        font_menu.add_radiobutton(label="Courier",
                                  variable=text_font,
                                  command=change_font)

        font_menu.add_radiobutton(label="Comic Sans",
                                  variable=text_font,
                                  command=change_font)

        # ------- View Menu ---------#

        line_numbers = tk.IntVar()
        line_numbers.set(1)

        # Create view_menu
        view_menu = tk.Menu(main_menu, tearoff=0)

        view_menu.add_checkbutton(label="Line Numbers",
                                  variable=line_numbers)

        view_menu.add_cascade(label="Fonts", menu=font_menu)

        main_menu.add_cascade(label="View", menu=view_menu)

        # Initialize Menus
        self.config(menu=main_menu)

        #-----DEFINE PAGES-----#
        self.frames = {}
        for page in (StartPage, PageOne, PageTwo):
            frame = page(master, self)
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show home page
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def quit_app(self):
        self.quit()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label = ttk.Label(self, text="Start Page", font=LARGE_FONT)
        # label.pack(pady=10, padx=10)

        # button1 = ttk.Button(self, text="Visit Page One",
        #                      command=lambda: controller.show_frame(PageOne))
        # button1.pack()

        # button2 = ttk.Button(self, text="Visit to Page Two",
        #                      command=lambda: controller.show_frame(PageTwo))
        # button2.pack()

        def initGUI(self, deck, num_lines):
            numCards = []
            addCard = []
            cardName = []

            for i in range(num_lines):
                numCards.append(tk.StringVar())
                numCards[i].set(str(deck[i][0]).zfill(2))

                # Create buttons
                cardName.append(ttk.Button(self, text=deck[i][1], width="30", command=lambda i=i: subtractCard(self, i)))
                addCard.append(ttk.Button(self, textvariable=numCards[i], width="3", command=lambda i=i: addCard(self, i)))

                # Organize and pack lines
                cardName[i].grid(row=i, column=0, sticky=tk.W)
                addCard[i].grid(row=i, column=1, sticky=tk.W)

            def addCard(self, index):
                currentQuantity = deck[index][0]
                newQuantity = currentQuantity + 1
                deck[index][0] = newQuantity
                numCards[index].set(str(newQuantity).zfill(2))

            def subtractCard(self, index):
                currentQuantity = deck[index][0]
                if currentQuantity > 0:
                    newQuantity = currentQuantity - 1
                    deck[index][0] = newQuantity
                    numCards[index].set(str(newQuantity).zfill(2))
                else:
                    print("Cards cannot be negative!")

        deck, num_lines = deckTracker.importDeck(decklist)
        initGUI(self, deck, num_lines)


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Page One!!1!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Back to Page Two",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Page Two!!2!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Back to Page One",
                             command=lambda: controller.show_frame(PageOne))
        button2.pack()


class DeckTracker():
    def __init__(self, decklist):

        self.decklist = decklist

    endgame = False

    # OPTIONS
    display_deck_after_action = False

    # class Card():
    #     def __init__(self, name, quantity):
    #         self.name = name
    #         self.quantity = quantity

    # cards = []
    # deckObj = Deck()
    def importDeck(self, decklist):
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

    def getName(self, deck, index):
        # input index to get name of card
        cardName = deck[index][1]
        # print(cardName)
        return cardName

    def getQuantity(self, deck, index):
        cardQuantity = deck[index][0]
        return cardQuantity

    def cardInfo(self, deck, index):
        cardQuantity = self.getQuantity(index)
        cardName = self.getName(index)
        print('You have ' + str(cardQuantity) + ' of ' + cardName)

    def deckSize(self, num_lines):
        deckSize = 0
        for i in range(0, num_lines):
            deckSize += self.getQuantity(i)
        return deckSize

    def displayDeck(self, deck, num_lines):
        for i in range(0, num_lines):
            print(str(i).zfill(2) + ' - ' + str(deck[i][0]) + ' - ' + deck[i][1])

    def subtractCard(self, deck, index, numCards):
        deck[index][0] = deck[index][0] - 1

        # newQuantity = deck[index][0] - 1
        # deck[index][0] = newQuantity
        # numCards[index].set(str(newQuantity).zfill(2))

    def addCard(self, deck, index, numCards):
        deck[index][0] = deck[index][0] + 1

        # newQuantity = deck[index][0] + 1
        # deck[index][0] = newQuantity
        # numCards[index].set(str(newQuantity).zfill(2))

    def drawProb(self, deck, index):
        global probability
        probability = self.getQuantity(index) / self.deckSize() * 100
        return probability

    def userInteract(self):
        # Main user input section
        global display_deck_after_action
        action = input("What would you like to do? >>> ")

        if action == 'dd':  # Display what's left in the deck
            self.displayDeck()

        elif action == 's':  # Subtract a card - it's being played!
            index = input("Which card is being played? >>> ")
            if index.isdigit():  # if it's able to be an int
                index = int(index)
                self.subtractCard(index)
                print('---')
                print('Removed 1 of ' + self.getName(index))
                print('You have ' + str(self.getQuantity(index)) + ' left')

        elif action == 'a':  # Add a card - you messed up!
            index = input("Which card is being added? >>> ")
            if index.isdigit():
                index = int(index)
                self.addCard(index)
                print('---')
                print('Added 1 of ' + self.getName(index))
                print('You have ' + str(self.getQuantity(index)) + ' left')

        elif action == 'i':
            index = input("Which card would you like more info about? >>> ")
            if index.isdigit():
                index = int(index)
                print('---')
                self.cardInfo(index)

        elif action == 'p':  # Probability page!
            index = input("What do you want to check the probability of? >>> ")
            if index.isdigit():
                index = int(index)
                print('---')
                cardName = self.getName(index)
                print("The probability of drawing %s is %.2f%%" % (cardName, self.drawProb(index)))

        elif action == 'ddon':
            display_deck_after_action = True

        elif action == 'ddoff':
            display_deck_after_action = False

        elif action == 'r':  # Reset deck!
            self.importDeck(decklist)
            print('The deck has been reset!')

        else:  # catch all typos
            print('Not Allowed')

        # Each cycle checks
        if (display_deck_after_action) & (action != 'dd'):
            print('---')
            self.displayDeck()
            print('---')
            print('You have ' + str(self.deckSize()) + ' cards left')


if __name__ == "__main__":
    global deck
    global num_lines

    deckTracker = DeckTracker(decklist)

    deckGUI = DeckGUI()
    deckGUI.geometry("300x700+300+300")
    deckGUI.resizable(width=True, height=True)
    deckGUI.mainloop()
