from tkinter import *


from PIL import Image, ImageTk

screen = Tk()  # since class Tk provides gui in the screen


# for changing the title of a gui we use title method
screen.title("HOME page")  # this is gui using gui prog lang


# for changing icon of the gui/screen
screen.iconbitmap('login.ico')


# 1.win = Tk()

# 2.win.title("registration")

# 3. screen.mainloop()


# we can save our screen/interface's maximum width and height
screen.maxsize(width=500, height=200)
screen.minsize(width=1000, height=2000)


# widget

# 1. Label : it is a text box used to (show/displaying) text(which may be information or message) in the display/ screen.

mylabel = Label(screen, text="this is text ")
mylabel.place(x=50, y=50)





# for showing screen/interface for infinty until we don't close it by ourself it runs for loop run to infinity
screen.mainloop()
