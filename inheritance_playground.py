'''learning about class and GUI inheritance'''

import tkinter as tk
from tkinter import ttk


class GUIInstance(tk.Tk):
    '''main gui class'''

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Inheritance Playground")

        master = tk.Frame(self)
        master.pack()


class ButtonWindow(tk.Frame):
    """ buttons section of GUI """

    def __init__(self, root):
        tk.Frame.__init__(self)
        self.root = root

    def create_button(self, root):
        """ create button """
        # takes array of cards and creates N number of buttons
        ttk.Button(root, text='yes', width="30").pack()


def main():
    '''main function'''

    master = tk.Tk()
    master.wm_title("testing")
    # gui = GUIInstance()
    button_frame = ButtonWindow(master)
    button_frame.create_button()
    master.geometry("450x700+300+300")
    master.resizable(width=True, height=True)
    master.mainloop()
    # gui.geometry("450x700+300+300")
    # gui.resizable(width=True, height=True)
    # gui.mainloop()


if __name__ == "__main__":
    main()
