""" GUI application for Eternal Deck Tracker (EDT) """

import tkinter as tk
# from tkinter import ttk


class App(tk.Frame):  # pylint: disable=too-many-ancestors

    """ first app """

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        self.master.title("Hello")
        tk.Label(self, text="This is my first GUI").pack()

        self.master.tk_setPalette(background='#ececec')

        # x_location = (self.master.winfo_screenwidth()
                      # - self.master.winfo_reqwidth()) / 2
        # y_location = (
            # self.master.winfo_screenwidth() - self.master.winfo_reqwidth()) / 3
        # self.master.geometry("+{}+{}".format(x_location, y_location))
        # self. master.config(menu=tk.Menu(self.master))


def main():
    """ main function """
    root = tk.Tk()
    app = App(root)
    # root.resizeable(width=True, height=True)
    app.mainloop()


if __name__ == "__main__":
    main()

    # https://www.youtube.com/watch?v=Wb1YFgHqUZ8
