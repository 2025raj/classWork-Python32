import turtle

# without using loop
#sides: 5
'''
turtle.Screen()
pen = turtle.Turtle()
pen.shape("arrow")
pen.pensize(5)
pen.color("red")

pen.forward(300)
pen.right(144)
pen.forward(300)

pen.right(144)
pen.forward(300)


pen.right(144)
pen.forward(300)


pen.right(144)
pen.forward(300)

pen.hideturtle()

turtle.done()
turtle.mainloop()
'''

# using loop.

'''
turtle.Screen()
pen = turtle.Turtle()
pen.shape("arrow")
pen.pensize(5)
pen.color("red")
turtle.bgcolor("pink")

for i in range(5):
    pen.forward(300)
    pen.right(144)
pen.hideturtle()
turtle.done()
turtle.mainloop()
'''

##### to draw shape from different position ###


# using: dot method
'''
turtle.Screen()
pen = turtle.Turtle()
pen.shape("arrow")
pen.pensize(10)
turtle.bgcolor("pink")
pen.up()
pen.goto(300, -220)
pen.down()
pen.color("red")
pen.dot(90)

pen.up()
pen.goto(-300, -220)
pen.down()
pen.color("yellow")
pen.dot(100)

pen.up()
pen.goto(-300, 220)
pen.down()
pen.color("green")
pen.dot(100)

pen.up()
pen.goto(300, 220)
pen.down()
pen.color("blue")
pen.dot(100)

pen.up()
pen.goto(0, 0)
pen.down()
pen.color("black")
pen.dot(100)

turtle.done()
turtle.mainloop()

'''

# using another method: made circle first then fill the circles.

'''
turtle.Screen()
pen = turtle.Turtle()
pen.shape("arrow")
pen.pensize(5)
turtle.bgcolor("pink")

pen.speed(0)
pen.up()
pen.goto(300, -220)
pen.down()


pen.begin_fill()
pen.fillcolor("yellow")
pen.circle(50)
pen.end_fill()

pen.up()
pen.goto(-300, -220)
pen.down()

pen.begin_fill()
pen.fillcolor("red")
pen.circle(50)
pen.end_fill()

pen.up()
pen.goto(-300, 220)
pen.down()


pen.begin_fill()
pen.fillcolor("green")
pen.circle(50)
pen.end_fill()

pen.up()
pen.goto(300, 220)
pen.down()

pen.begin_fill()
pen.fillcolor("blue")
pen.circle(50)
pen.end_fill()


pen.up()
pen.goto(0, 0)
pen.down()

pen.begin_fill()
pen.fillcolor("black")
pen.circle(50)
pen.end_fill()

pen.hideturtle()


turtle.done()
turtle.mainloop()
'''
