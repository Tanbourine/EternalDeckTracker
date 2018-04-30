""" test """
import tkinter as tk

# https://stackoverflow.com/questions/16996432/how-do-i-bind-the-enter-key-to-a-function-in-tkinter


class ImportApplication(tk.Frame):

    """ main application frame. build other frames into this"""
    # pylint: disable=too-many-ancestors

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.master = master
        self.create_widget()
        self.poop = 0

    def create_widget(self):
        """ create stuff here """

        self.master.bind('<Return>', self.get_entry)

        # creating entry
        self.dialog = tk.Entry(self)
        self.dialog.grid(row=0, column=0)

        # creating button
        self.string = tk.StringVar()
        self.string.set('hello')
        self.butts = tk.Button(self, textvariable=self.string, command=self.get_entry)
        self.butts.grid(row=0, column=1)

        # creating label
        self.labelmaker = tk.Label(self, text='label')
        self.labelmaker.grid(row=1, column=0)

        # creating quit button
        self.quit_button = tk.Button(self, text='QUIT', command=self.quit_app)
        self.quit_button.grid(row=2, column=1)

    def quit_app(self):
        """ closes app"""
        self.master.destroy()

    def get_entry(self, event):
        """sdjkfjd"""
        # pylint: disable=unused-argument
        self.poop = self.dialog.get()
        print(self.poop)

        # set StringVar in button to goodbye
        self.string.set(self.poop)


def main():
    """ fdjfkalsdj """

    root = tk.Tk()
    app = ImportApplication(root)
    app.grid()

    app.mainloop()

if __name__ == "__main__":
    main()
