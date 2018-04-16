'''learning about class and GUI inheritance'''

import tkinter as tk


class GUIInstance(tk.Tk):
    '''main gui class'''

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Inheritance Playground")

        master = tk.Frame(self)
        master.grid(row=0, column=0, sticky=tk.W)


def main():
    '''main function'''

    gui = GUIInstance()
    gui.geometry("450x700+300+300")
    gui.resizable(width=True, height=True)
    gui.mainloop()


if __name__ == "__main__":
    main()
