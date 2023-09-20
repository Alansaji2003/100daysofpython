import random
from tkinter import *

window = Tk()

window.title("Test with tkinter")
window.minsize(height=100, width=300)


def calculate():
    n = int(entry.get())
    label3["text"] = n/16



entry = Entry(width=10)
entry.grid(column=1,row=1)


label = Label(text="Kilometers",font=("Ariel",24,"bold"))
label.grid(column=2,row=1)


label2 = Label(text="Is Equal To ",font=("Ariel",24,"bold"))
label2.grid(column=0,row=2)

label3 = Label(text="0",font=("Ariel",24,"bold"))
label3.grid(column=1,row=2)

label = Label(text="Miles",font=("Ariel",24,"bold"))
label.grid(column=2,row=2)

button = Button(text="Convert", command=calculate)
button.grid(column=1, row=3)
#
# #label
# label = Label(text="Whatchu waiting for?", font=("Ariel",24,"bold"))
#
# label.grid(column=0, row=0)
# def changeText():
#
#     label.config(text=entry.get())
#
# #button
#
# button = Button(text="Click Me", command=changeText)
# button2 = Button(text="New Button")
# button.grid(column=1, row=2)
# button2.grid(column=3,row=1)
#
#
#
# #entry
#
# entry = Entry(width=18)
# entry.grid(column=4, row=4)
#
#

window.mainloop()




