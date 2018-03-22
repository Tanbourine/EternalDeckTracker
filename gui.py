import tkinter as tk
from tkinter import ttk
import DeckTracker as dt

decklist = 'noIndex.csv'

LARGE_FONT = ("Verdana", 12)
deck, num_lines = dt.importDeck(decklist)


class DeckGUI(tk.Tk):
    def __init__(self, *args, **kwargs):

        # Initialize tk inheritance
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default="clienticon.ico")
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


if __name__ == "__main__":

    deckGUI = DeckGUI()
    deckGUI.geometry("300x700+300+300")
    deckGUI.resizable(width=True, height=True)
    deckGUI.mainloop()
