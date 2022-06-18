from tkinter import *

root = Tk()

root.maxsize(width=700, height=500)

root.title("simple calculator")

e = Entry(root, text="", width=80, fg="black", borderwidth=10, bg="yellow")
e.grid(row=0,  column=0, columnspan=10, padx=20, pady=20)


def button_click(number):

    current = e.get()
    e.delete(0, END)  # screen clear
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()

    global calculate
    calculate = "addition"

    global f_num
    f_num = int(first_number)

    e.delete(0, END)


def button_sub():
    first_number = e.get()

    global calculate
    calculate = "subtract"

    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_multi():
    first_number = e.get()

    global calculate
    calculate = "multiply"

    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_div():
    first_number = e.get()

    global calculate
    calculate = "divison"

    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_expo():
    first_number = e.get()

    global calculate
    calculate = "exponent"

    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    sec_value = int(second_number)
    e.delete(0, END)
    if calculate == "addition":
        e.insert(0, f_num + sec_value)

    elif calculate == "subtract":
        e.insert(0, f_num - sec_value)

    elif calculate == "multiply":
        e.insert(0, f_num * sec_value)

    elif calculate == "divison":
        e.insert(0, f_num / sec_value)

    elif calculate == "exponent":
        e.insert(0, f_num ** sec_value)


# defining the buttons:
button_1 = Button(root, bg="pink", text="1", padx=40, pady=20,
                  command=lambda: button_click(1))
button_2 = Button(root, bg="pink", text="2", padx=40, pady=20,
                  command=lambda: button_click(2))
button_3 = Button(root, bg="pink", text="3", padx=40, pady=20,
                  command=lambda: button_click(3))

button_4 = Button(root, bg="pink", text="4", padx=40, pady=20,
                  command=lambda: button_click(4))

button_5 = Button(root, bg="pink", text="5", padx=40, pady=20,
                  command=lambda: button_click(5))

button_6 = Button(root, bg="pink", text="6", padx=40, pady=20,
                  command=lambda: button_click(6))

button_7 = Button(root, bg="pink", text="7", padx=40, pady=20,
                  command=lambda: button_click(7))

button_8 = Button(root, bg="pink", text="8", padx=40, pady=20,
                  command=lambda: button_click(8))

button_9 = Button(root, bg="pink", text="9", padx=40, pady=20,
                  command=lambda: button_click(9))

button_0 = Button(root, bg="pink", text="0", padx=40, pady=20,
                  command=lambda: button_click(0))


button_add = Button(root, bg="blue", text="+", padx=39,
                    pady=20, command=button_add)

button_sub = Button(root, bg="blue", text="-", padx=39,
                    pady=20, command=button_sub)


button_multi = Button(root, bg="blue", text="*", padx=39,
                      pady=20, command=button_multi)

button_power = Button(root, bg="blue", text="exponent", padx=39,
                      pady=20, command=button_expo)


button_divison = Button(root, bg="blue", text="/",
                        padx=39, pady=20, command=button_div)


button_equal = Button(root, bg="red", text="=", padx=50,
                      pady=20, command=button_equal)


button_clear = Button(root, bg="red", text="clear", padx=40,
                      pady=20, command=button_clear)


# putting buttons on the screen

button_1.grid(row=1, column=0, padx=20, pady=20)
button_2.grid(row=1, column=1,  padx=20, pady=20)
button_3.grid(row=1, column=2, padx=20, pady=20)
button_clear.grid(row=1, column=3, padx=20, pady=20)

button_4.grid(row=2, column=0, padx=20, pady=20)
button_5.grid(row=2, column=1, padx=20, pady=20)
button_6.grid(row=2, column=2, padx=20, pady=20)
button_add.grid(row=2, column=3, padx=20, pady=20)

button_7.grid(row=3, column=0, padx=20, pady=20)
button_8.grid(row=3, column=1, padx=20, pady=20)
button_9.grid(row=3, column=2, padx=20, pady=20)
button_sub.grid(row=3, column=3, padx=20, pady=20)


button_0.grid(row=4, column=0, padx=20, pady=20)

button_multi.grid(row=4, column=1, padx=20, pady=20)
button_divison.grid(row=4, column=2, padx=20, pady=20)

button_power.grid(row=4, column=3, padx=20, pady=20)

button_equal.grid(row=3, column=4, padx=20, pady=20, columnspan=2)


root.mainloop()
