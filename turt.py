import turtle

# class activity
#################################################
# # for making square
'''import turtle
wn = turtle.Screen()
pen = turtle.Turtle()
for i in range(4):
    pen.forward(50)
    pen.left(90)
turtle.mainloop()
'''

'''
import turtle
wn = turtle.Screen()
pen = turtle.Turtle()
for i in range(6):

    pen.right(60)
    pen.forward(50)
turtle.mainloop()
'''

'''
import turtle
t = turtle.Turtle()
t.Screen()

t.up()
t.goto(0,-100)
t.down()
t.circle(100)
turtle.done()
turtle.mainloop()
'''

'''
import turtle
turtle.set(0)

turtle.forward(80)
turtle.write("east")

turtle.forward(80)
turtle.write("north")
turtle.home()
turtle.seth(180)
'''


'''
wn = turtle.Screen()
t = turtle.Turtle()

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
while(True):
    for i in range(6):
        for colors in ["red", "blue", "magenta", "green", "yellow", "white"]:
            turtle.color(colors)
            turtle.circle(100)
            turtle.left(10)

turtle.mainloop()
'''


"""w = turtle.Screen()
t = turtle.Turtle()
turtle.mainloop()"""

#####################################


'''we use turtle module's "Screen" and " 'T'urtle" built-in function for creating a dedicated screen for my attractive pictures and  shapes '''


'''
# for changing the screensize
# use this command:
turtle.screensize()
turtle.screensize(4000, 5000)
turtle.screensize()
'''  # this doesnot work
turtle.Screen()

# do comment this code using '#' before pen to see differnce
pen = turtle.Turtle()  # this command is used for pen


# pen is (a variable or an object) whereas Turtle built-in function gives us a pen and turtle.Turtle is an (class)
# turtle modules gives a pen to draw objects in that blank screen


# next
# turtle(pen) has 6 shapes given upper one is classic one

# there are (arrow,turtle, circle, square, triangle, classic)


# 1.we can use this by using this given code.

pen.shape("turtle")  # for turtle shape as a pen


pen.shape("arrow")  # for arrow shape as a pen

pen.shape("circle")  # for circle as pen

pen.shape("square")  # for square as pen


# for changing color of a pen

# use this (object.color"input field" built-in function ) where object is pen


pen.color("black")
pen.forward(50)  # put 0 once to see


# pen.color("green")
# pen.forward(100)

# pen.color("black")
# pen.forward(100)


# for changing the screen color
# use this code:

turtle.bgcolor("green")  # background color built-in function

# turtle.bgcolor("black")

# turtle.bgcolor("pink")

# for changing the pen size
pen.pensize(5)
pen.forward(50)


# for changing the pen speed

pen.speed(0)  # speed is used for controlling speed of a pen ;  0 is fastest
pen.color("black")
pen.forward(50)

pen.speed(10)  # 10 is for fast
pen.color("red")
pen.forward(50)


pen.speed(6)  # 6 is for normal
pen.color("purple")
pen.forward(50)

pen.speed(3)  # for controlling speed of a pen ;  3 is slow
pen.color("red")
pen.forward(50)

pen.speed(1)  # for controlling speed of a pen ;  1 is slowest
pen.color("red")
pen.forward(50)


# for clearing screen use object.clear/ (built-in function)
# pen.clear()


# we can use pen in 4 direction forward,backward,left,right

pen.color("red")
pen.backward(50)  # (object.backward) use to move pen backward


pen.color("blue")
pen.backward(50)


turtle.bgcolor("yellow")
turtle.title("hello world")
pen.color("black")
pen.left(90)  # if we use left then it starts from anti-clockwise
pen.forward(100)


pen.color("blue")
pen.right(90)
pen.forward(100)


turtle.done()


turtle.mainloop()  # only use this command at last
