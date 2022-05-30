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


turtle.Screen()
pen = turtle.Turtle()
pen.shape("arrow")
pen.pensize(5)
pen.color("red")

for i in range(5):
    pen.forward(300)
    pen.right(144)
pen.hideturtle()
turtle.done()
turtle.mainloop()
