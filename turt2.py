import turtle
'''
turtle.Screen()

turtle.bgcolor("pink")

pen = turtle.Turtle()

pen.shape("arrow")

pen.pensize(5)

pen.color("green")

# 'for making square
clockwise' ##########
pen.forward(100)
pen.rt(90)
pen.speed(1)
pen.forward(100)

pen.rt(90)
pen.speed(0)
pen.forward(100)


pen.rt(90)
pen.speed(1)
pen.forward(100)


# 'for making square
anti-clockwise' ##########

pen.forward(100)
pen.left(90)
pen.speed(1)
pen.forward(100)

pen.left(90)
pen.speed(0)
pen.forward(100)


pen.left(90)
pen.speed(1)
pen.forward(100)


'''
# "drawing square using loop"

'''
turtle.Screen()
pen = turtle.Turtle()
pen.color("red")
pen.pensize(5)
pen.begin_fill()
pen.fillcolor("green")
for i in range(4):  # 0 to 3 because a square has 4 sides so we use 4
    pen.forward(50)
    pen.left(90)

pen.end_fill()

pen.hideturtle()

turtle.done()


turtle.mainloop()
'''

# drawing pentagon ### side: 5 and angle: 72 degree
'''
turtle.Screen()
pen = turtle.Turtle()
pen.color("red")
pen.pensize(10)

pen.forward(100)
pen.left(72)
pen.forward(100)


pen.left(72)
pen.forward(100)


pen.left(72)
pen.forward(100)


pen.left(72)
pen.forward(100)


turtle.done()
turtle.mainloop()
'''

# using for loop : pentagon
'''
turtle.Screen()
pen = turtle.Turtle()
pen.begin_fill()
pen.fillcolor("pink")
for i in range(5):
    pen.forward(100)
    pen.right(72)
pen.end_fill()
turtle.done()
turtle.mainlop()
'''

# for creating hexagon##### side: 6, angle = 60 deg
'''
turtle.Screen()
pen = turtle.Turtle()
pen.color("red")
pen.pensize(10)

pen.forward(100) # since forward(amount = 100)
pen.left(60)  # since left(degree)
pen.forward(100)


pen.left(60)
pen.forward(100)


pen.left(60)
pen.forward(100)


pen.left(60)
pen.forward(100)

pen.left(60)
pen.forward(100)

turtle.done()
turtle.mainloop()

'''


# using loop ; hexagon
'''
turtle.Screen()
pen = turtle.Turtle()
pen.begin_fill()
pen.fillcolor("pink")
for i in range(6):
    pen.forward(100)
    pen.right(60)
pen.end_fill()
turtle.done()
turtle.mainloop()
'''


# for heptagon . sides: 7, exterior angle = 51.42
'''
turtle.Screen()
pen = turtle.Turtle()
pen.color("red")
pen.pensize(10)

pen.forward(100)  # since forward(amount = 100)
pen.left(51.42)  # since left(degree)
pen.forward(100)


pen.left(51.42)
pen.forward(100)


pen.left(51.42)
pen.forward(100)


pen.left(51.42)
pen.forward(100)

pen.left(51.42)
pen.forward(100)


pen.left(51.42)
pen.forward(100)


turtle.done()
turtle.mainloop()
'''

# using loop : heptagon ;;;; attribute error
'''
turtle.Screen()
pen = turtle.Turtle()
pen.begin_fill()
pen.fillcolor("pink")
for i in range(7):
    pen.forward(100)
    pen.right(51.42)
pen.end_fill()
turtle.done()
turtle.mainloop()
'''

# using loop: octagon; side:8 and angle : 45

'''
turtle.Screen()
pen = turtle.Turtle()
pen.begin_fill()
pen.fillcolor("pink")
for i in range(8):
    pen.forward(100)
    pen.right(45)
pen.end_fill()
turtle.done()
turtle.mainloop()
'''

# using loop: nanogon; side:9 and angle : 40
'''
turtle.Screen()
pen = turtle.Turtle()
pen.begin_fill()
pen.fillcolor("pink")
for i in range(10):
    pen.forward(100)
    pen.right(40)
pen.end_fill()
turtle.done()
turtle.mainloop()
'''

# using loop: decagon; side:10 and angle : 36
'''
turtle.Screen()
pen = turtle.Turtle()
pen.begin_fill()
pen.fillcolor("pink")
for i in range(11):
    pen.forward(100)
    pen.right(36)
pen.end_fill()
pen.hideturtle() # for hiding turtle
turtle.done()
turtle.mainloop()
'''

### for creating circle ###


turtle.Screen()
pen = turtle.Turtle()


pen.begin_fill()
pen.fillcolor("blue")

pen.circle(150)

pen.end_fill()

pen.hideturtle()
turtle.done()
turtle.mainloop()


# creating a dot

'''
turtle.Screen()
pen = turtle.Turtle()

#pen.color("green")

pen.dot(70)


turtle.done()
turtle.mainloop()
'''

# to draw shape from different position
