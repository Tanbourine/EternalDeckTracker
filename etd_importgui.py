"""Creates page 2 function that allows user to import deck from eternal
# Ideal Page 2:
user copy/pastes deck into entry box
when hit <enter> key, popup will have them name the deck or replace one of their old decks
keeps up to 3 decks on save
button next to each display of saved deck that says "use" that will upload selected deck to main
page
label to the left of each saved-deck-button that says whether it is "in use" or not"""

import tkinter as tk



class ImportPage(tk.Frame):
    # pylint: disable=too-many-ancestors

    """Main Frame for page 2. Inside: Entry Box, Enter Button, Deck Select Buttons, In use label"""

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.master = master
        self.create_widget()
        self.entry_input = 0
        self.new_deck = []

    def create_widget(self):
        """Creates Opening Widget on Page 2"""

        self.master.bind('<Return>', self.get_entry)  # binds the enter key to get_entry method

        self.dialogue = tk.Entry(self)  # Creates entry box
        self.dialogue.grid(row=0, column=0)

        self.button_label = tk.StringVar()
        self.button_label.set("Enter")
        self.enter_key = tk.Button(self, textvariable=self.button_label, command=self.get_entry)
        self.enter_key.grid(row=0, column=1)

        self.deck1_label = tk.Label(self, text='label')
        self.deck1_label.grid(row=1, column=0)

        # buttons to load in saved decks
#        self.deck1_button = tk.Button(self, text = deckname, commmand=self.build_deck)

    def get_entry(self, event=0):
        """Gets data from dialogue box"""
        # pylint: disable=unused-argument
        self.entry_input = self.dialogue.get() + '\n'
        print(self.entry_input)


        self.new_deck = []
        start = 0
        end = 0
        for i in range(len(self.entry_input)):
            if self.entry_input[i] == '\n':
                end = i
                self.new_deck.append(self.entry_input[start:end])
                self.entry_input.replace(self.entry_input[i], 'x')
                start = end+1
                print (self.new_deck)

def main():
    """main"""
    root = tk.Tk()
    app = ImportPage(root)
    app.grid()


    app.mainloop()

if __name__ == "__main__":
    main()
