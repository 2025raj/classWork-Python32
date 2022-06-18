from tkinter import *

root = Tk()
root.title("Simple Calculator")
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()

    compute = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_subtract():
    first_number = e.get()
    compute = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    compute = "multipilcation"
    f_num = int(first_number)
    e.delete(0, END)


def button_division():
    first_number = e.get()
    compute = "division"
    f_num = int(first_number)
    e.delete(0, END)


root.mainloop()
