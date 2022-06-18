

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

#########################################################################################


from tkinter import *

from PIL import Image, ImageTk

screen = Tk()

screen.title("LOGIN")

my_image = Image.open("flower.jpg")

resized_image = my_image.resize(300,500)




'''
#########################################################################

'''
# for creating pop up box we import messagebox

from tkinter import *

from tkinter import messagebox

screen = Tk()

def popup():
    messagebox.showinfo("this is message box :title",
                        "this is message or information that what we want to deliever in our box")


button = Button(screen, text = "popup",command = popup)
button.pack()

'''
######################################################################

# screen = Tk()

# def popup():
#     response = messagebox.askyesno("this is popup", "hello world")
#     Label(screen, text=response).pack()

#     if response == 1:
#         Label(screen, text="clicked yes"). pack()
#     else:
#         Label(screen, text="clicked no"). pack()


# button = Button(screen, text="popup", command=popup) .pack()


# screen.mainloop()


##################################################################################

window = Tk()

def open():
    global my_img
    top = Toplevel()
    my_img = ImageTk.PhotoImage(Image.open("flower.jpg"))
    mylabel = Label(top, image=my_img)
    mylabel.pack(pady=10)
    btn = Button(top, text="close window", command=top.destroy)
    btn.pack()


btnn = Button(window, text="open", command=open)
btnn.pack()

window.mainloop()
