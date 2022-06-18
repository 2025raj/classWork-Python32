from tkinter import *

"""
screen = Tk()


screen.maxsize(width=500, height=300)
screen.minsize(width=500, height=300)


# screen.title("Login")
# mylabel = Label(screen, text="UserName")
# mylabel.pack()
# mybutton = Button(screen, text="enter your username")
# mybutton.pack()


# mylabel = Label(screen, text="password")
# mylabel.pack()
def func():
    print("button is clicked")


mybutton = Button(screen, text="login", command=func)  # CLI ma show hunxa
mybutton.pack()


screen.mainloop()
"""

"""
from tkinter import *

screen = Tk()


screen.maxsize(width=500, height=300)
screen.minsize(width=500, height=300)


def myclick():
    mylabel = Label(screen, text="look i clicked a button", fg="red", bg="", font=50)
    mylabel.pack()



mybutton = Button(screen, text="login", command=func)  # CLI ma show hunxa
mybutton.pack()

screen.mainloop()



"""


"""
screen = Tk()


screen.maxsize(width=500, height=300)
screen.minsize(width=500, height=300)

mybutton = Button(screen, text="Button1")
mybutton.pack()

mybutton = Button(screen, text="Button2") # automatically enabled button
mybutton.pack()

mybutton = Button(screen, text="login", state=DISABLED) # button is disabled . 

mybutton = Button(screen, text="signup")
mybutton.pack()

screen.mainloop()

"""


"""

screen = Tk()


screen.maxsize(width=500, height=300)
screen.minsize(width=500, height=300)

e = Entry(screen, width=50, bg="blue", fg="white", borderwidth=5, font=20)

e.pack()


def myclick():
    mylabel = Label(screen, text="Hello" + e.get())
    mylabel.pack()


button = Button(screen, text="clickme", padx=10, pady=10, command=myclick)
button.pack()
screen.mainloop()
"""


# data passing in a single line in the entry box
"""
screen = Tk()
screen.title("Interface")
screen.maxsize(width=500, height=300)
screen.minsize(width=500, height=300)


# function
def add():
    x = var.get()
    print(x)
    mylabel.config(text=x, bg="green")


# label 1

mylabel = Label(screen, text="user name", fg="red", bg="yellow")
mylabel.place(x=10, y=10)


# label 2
mylabell = Label(screen, text="nothing", fg="red", bg="yellow")
mylabel.place(x=40, y=120)


# entry

var = StringVar()
ent = Entry(screen, bg="pink", fg="white", textvariable = var)
ent.place(x=80, y=10)

# button

btn = Button(screen, text="submit", bg="green", fg="white", command=add)
btn.place(x=20, y=80)
screen.mainloop()

"""


# data passing in multiple line in the entry box

#label1 mileko xaina check this out

'''
screen = Tk()
screen.title("Interface")
screen.maxsize(width=500, height=300)
screen.minsize(width=500, height=300)


def click():
    text1 = "Address" + mytext.get("1.0", END)
    lb1.config(text=str(text1))


mytext = Text(screen, font=20, width=20, height=10)
mytext.place(x=0, y=50)


# button
btn = Button(screen, text="click me", font=30, command=click)
btn.place(x=200, y=200)


screen.mainloop()


'''

'''
# frame

#Adding frames to program

window = Tk()
frame = LabelFrame(window, text = "this is my 1st frame", padx = 10, pady = 10)
frame.pack(padx = 50 , pady = 50)
b = Button(frame, text = "dont click here")
b2 = Button(frame,text = "...here")
b3 = Button(window,text ="hello  will be shown in the interface area")
b.grid(row =10 , colum = 20 )
b2.grid(row = 20, colum = 10)
b3.grid(row = 30, column = 40)
window.mainloop()


'''


# radio button

'''
window = Tk()
def add():
    print(var.get())

var = IntVar()
r1 = Radiobutton(window, text ="Male", variable = var , value = 1, command = add)

r2 = Radiobutton(window, text ="female", variable = var , value = 2, command = add)

r3 = Radiobutton(window, text ="others", variable = var , value = 3, command = add)

r1.pack(anchor = N)


window.mainloop()



'''