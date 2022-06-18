
# from tkinter import *
# from PIL import Image, ImageTk

# window = Tk()

# window.title("LOGIN")


# my_image = ImageTk.PhotoImage(Image.open("stamp.png"))

# my_label = Label(window, image=my_image)
# my_label.pack()


# button_quit = Button(window, text="Exit", command=window.quit, width=20)
# button_quit.pack()

# window.mainloop()

#################################################################################################################

# for resizing the image
###############################

# from tkinter import *
# from PIL import Image, ImageTk

# window = Tk()

# window.title("LOGIN")

# window.maxsize(width=1000, height=1000)
# window.minsize(width=500, height=500)

# my_image = Image.open("ornament.png")


# resized_image = my_image.resize((300, 250))

# converted_image = ImageTk.PhotoImage(resized_image)

# mylabel = Label(window, image=converted_image, width=300, height=100)
# mylabel.pack()

# button_quit = Button(window, text="Exit", command=window.quit, width=20)
# button_quit.pack()

# window.mainloop()


#####################################################################################################################
from tkinter import *

from PIL import Image, ImageTk

interface = Tk()

interface.title("Homepage")

interface.maxsize(width=1400, height=1080)
# interface.geometry("1020x1080")


img_load = Image.open("stamp.png")

pht_obj = ImageTk.PhotoImage(img_load)

label = Label(interface, image=pht_obj)
label.pack()


interface.mainloop()
