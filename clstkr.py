# radio button

from tkinter import *

window = Tk

'''
def add():
    if var.get() == 1:
        print("male")
    else:
        print("Female")

var = IntVar 

r1 = Radiobutton(window, text = "male", variable = var, value = 1, command = add)
r1.pack(anchor = W)
r2 = Radiobutton(window, text = "female", variable = var, value = 1, command = add)
r2.pack(anchor = W)


window.mainloop()
'''


# radio button

'''
def add():
    selection = "you have selected the option" + str(var.get())
    label.config(text = selection)


var = IntVar

r1 = Radiobutton(window, text = "button 1", variable = var, value = 1, command = add)
r1.pack(anchor = W)

r2 = Radiobutton(window, text = "button 2", variable = var, value = 2, command = add)
r2.pack(anchor = W)

r3 = Radiobutton(window, text = "button 3", variable = var, value = 3, command = add)
r3.pack(anchor = W)

label = Label(window)
label.pack()

window.mainloop()

'''


def add():
    label.config(text = CheckVar1.get())
CheckVar1 = IntVar()

c1 = checkbutton(,text = "Music")

