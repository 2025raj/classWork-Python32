from tkinter import *
win = Tk()  # this provide screen/window/user interface in which we draw something
win.title("login registration")
win.iconbitmap('icon.ico')  # for changing icon on the screen


# for changing screensize
# 2 methods: maxsize,minsize,geometry

win.maxsize(width=1000, height=700)
win.minsize(width=500, height=600)


# win.geometry("200x500") # this is letter x : (200 letter'x' 500) x means times


win.mainloop()  # mainloop is infinite loop;
