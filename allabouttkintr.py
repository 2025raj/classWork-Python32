from tkinter import *

screen = Tk()  # screen

screen.maxsize(width=1000, height=1000)

# max and min method le hamro screen ko size set garna help garxa
screen.minsize(width=500, height=500)


# geometry method: used to place/positioning widget on the gui/screen

'''

label1 = Label(screen, text=("East"))
#label1.place(x=10, y=10)
#label1.grid(row=5, column=10)
label1.pack()

label2 = Label(screen, text=("west"))
label2.pack()


'''

# positioning using grid method
'''
label1 = Label(screen, text="hi")
label2 = Label(screen, text="hello")
label3 = Label(screen, text="hey")

label1.grid(row=0, column=0)
label2.grid(row=2, column=2)
label3.grid(row=1, column=4)

'''


# creating a button using different padding values:

# button has ; many parameter/properties : text, state, padx, pady, state,

'''
Redbutton = Button(screen, text="click now", padx=100, pady=50,
                   fg="white", bg="red", font="lato" )  # by default here is automatically enabled.
Redbutton.pack(side=TOP)

Bluebutton = Button(screen, state=DISABLED, text="click now", padx=10, pady=50,
                    fg="blue", bg="pink", font="lato")                          # state = DISABLED means cannot able to click button.
Bluebutton.pack(side=BOTTOM)
'''


# button event means when we a click button an event/action occurs.
'''
def click():
   # print("clicked right now") # to show message on Command line interface we use: print()

    # but to print/show on our Gui we have to do

    label1 = Label(screen, text="clicked right now") # to show message on our GUI WE use Label widget.
    label1.pack()


Redbutton = Button(screen, command=click, text="click now", padx=100, pady=50,
                   fg="white", bg="red", font="lato", )  # by default here is automatically enabled.
Redbutton.pack(side=TOP)


'''

# Entry widget is a single line inputfield


#check_track = StringVar
single_line = Entry(screen,
                    fg="black", bg="yellow")  # user input data ko datatype track or check garna hamile StringVar class use gareko
single_line.pack()


def click():
    display = single_line.get()
    print(display)
    mylabel = Label(screen, text=display)
    mylabel.pack()


button = Button(screen, text="submit", command=click)
button.pack()


screen.mainloop()
