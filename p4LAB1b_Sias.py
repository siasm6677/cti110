import turtle
wn = turtle.Screen()

name = turtle.Turtle()
name.shape("circle")
name.color("purple")
name.pensize(4)

name.left(90)
name.forward(100)
name.right(135)
name.forward(75)
name.left(90)
name.forward(75)
name.right(135)
name.forward(100)

name.penup()
name.left(90)
name.forward(50)
name.pendown()

name.forward(20)
name.circle(25, 185)
name.right(180)
name.circle(25, -185)
name.backward(20)




wn.mainloop()
