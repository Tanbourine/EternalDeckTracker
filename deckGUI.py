from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("300x600+300+300")
root.resizable(width=False, height=False)

frame = Frame(root)


card_names = ['abcd', 'bcde', 'cdef', 'defg', 'efgh']
card_quantity = [1, 2, 3, 4, 5]


cButton = []
label = []
cQuantity = []

# Create each entry in deck
for i in range(len(card_names)):
    cQuantity.append(StringVar())
    cQuantity[i].set(str(card_quantity[i]).zfill(2))

    # Create line
    cButton.append(Button(root, text=card_names[i], command=lambda i=i: addCard(i)))
    label.append(Button(root, textvariable=cQuantity[i], command=lambda i=i: subtractCard(i)))

    # Organize and pack lines
    cButton[i].grid(row=i, column=0, sticky=W)
    label[i].grid(row=i, column=1, sticky=W)


def addCard(index):
    newQuantity = card_quantity[index] + 1
    card_quantity[index] = newQuantity
    cQuantity[index].set(str(newQuantity).zfill(2))
    # updateLabel(index)


def subtractCard(index):
    newQuantity = card_quantity[index] - 1
    card_quantity[index] = newQuantity
    cQuantity[index].set(str(newQuantity).zfill(2))


root.mainloop()
