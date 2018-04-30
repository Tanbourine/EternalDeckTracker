#Creates page 2 function that allows user to import deck from eternal

# Ideal Page 2:
#user copy/pastes deck into entry box
#when hit <enter> key, popup will have them name the deck or replace one of their old decks
#keeps up to 3 decks on save
#button next to each display of saved deck that says "use" that will upload selected deck to main
#page
#label to the left of each saved-deck-button that says whether it is "in use" or not
import tkinter as tk

# pylint: disable=too-many-ancestors
# pylint: disable=bad-whitespace
# pylint: disable=invalid-name

class page2(tk.Frame):
    """Main Frame for page 2. Inside: Entry Box, Enter Button, Deck Select Buttons, In use label"""
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.master = master
        self.create_widget()
        self.entry_input = 0

    def create_widget(self):
        """Creates Opening Widget on Page 2"""

      #  self.master.bind('<Return>', self.get_entry) #binds the enter key to get_entry method

        self.dialogue = tk.Entry(self) #Creates entry box
        self.dialogue.grid(row = 0, column = 0 )

        self.button_label = tk.StringVar()
        self.button_label.set("Enter")
        self.enterKey = tk.Button(self, textvariable=self.button_label, command=self.get_entry)
        self.enterKey.grid(row = 0, column = 1)

        #buttons to load in saved decks
#        self.deck1_button = tk.Button(self, text = deckname, commmand=self.build_deck)

    def get_entry(self, event):
        """Gets data from dialogue box"""
        # pylint: disable=unused-argument
        self.entry_input = self.dialogue.get()
        print(self.entry_input)

        self.button_label.set(self.entry_input)
def main():
    """main"""
    root = tk.Tk()
    app = page2(root)
    app.grid()

    app.mainloop()

if __name__ == "__main__":
    main()
