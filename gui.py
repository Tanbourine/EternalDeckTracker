from tkinter import *
from tkinter import ttk

root = Tk()

frame = Frame(root)

# a = 1

Label(root, text="Qnty: 1").grid(row=0, column=0, sticky=W)
Label(root, text="Dark Return").grid(row=0, column=1, sticky=W)
Button(root, text="-").grid(row=0, column=2, sticky=E)
Button(root, text="+").grid(row=0, column=3, sticky=E)

Label(root, text="2").grid(row=1, column=0, sticky=W)
Label(root, text="3").grid(row=2, column=0, sticky=W)


# def addQnty(event):
#     a += 1

# ###
# def get_sum(event):
#     num1 = int(num1Entry.get())
#     num2 = int(num2Entry.get())

#     sum = num1 + num2

#     sumEntry.delete(0, "end")
#     sumEntry.insert(0, sum)


# num1Entry = Entry(root)
# num1Entry.pack(side=LEFT)
# Label(root, text="+").pack(side=LEFT)

# num2Entry = Entry(root)
# num2Entry.pack(side=LEFT)

# equalButton = Button(root, text="=")
# equalButton.bind("<Button-1>", get_sum)
# equalButton.pack(side=LEFT)

# sumEntry = Entry(root)
# sumEntry.pack(side=LEFT)

# ####
# Label(root, text="Description").grid(row=0, column=0, sticky=W)
# Entry(root, width=50).grid(row=0, column=1)
# Button(root, text="Submit").grid(row=0, column=8)

# Label(root, text="Quality").grid(row=1, column=0, sticky=W)
# Radiobutton(root, text="New", value=1).grid(row=2, column=0, sticky=W)
# Radiobutton(root, text="Good", value=2).grid(row=3, column=0, sticky=W)
# Radiobutton(root, text="Poor", value=3).grid(row=4, column=0, sticky=W)
# Radiobutton(root, text="Damaged", value=4).grid(row=5, column=0, sticky=W)

# Label(root, text="Benefits").grid(row=1, column=1, sticky=W)
# Checkbutton(root, text="Free Shipping").grid(row=2, column=1, sticky=W)
# Checkbutton(root, text="Bonus Gift").grid(row=3, column=1, sticky=W)


# ####
# Label(root, text="First name").grid(row=0, sticky=W, padx=4)
# Entry(root).grid(row=0, column=1, sticky=E, pady=4)

# Label(root, text="Last name").grid(row=1, sticky=W, padx=4)
# Entry(root).grid(row=1, column=1, sticky=E, pady=4)

# Button(root, text="Submit").grid(row=3)


#####
# Label(frame, text="A bunch of buttons").pack()

# Button(frame, text="B1").pack(side=LEFT, fill=Y)
# Button(frame, text="B2").pack(side=TOP, fill=X)
# Button(frame, text="B3").pack(side=RIGHT, fill=X)
# Button(frame, text="B4").pack(side=LEFT, fill=X)

# frame.pack()


#####
# labelText = StringVar()

# label = Label(frame, textvariable=labelText)
# button = Button(frame, text="Click Me")

# labelText.set("I am a label")

# label.pack()
# button.pack()
# frame.pack()


root.mainloop()
