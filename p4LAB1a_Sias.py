import turtle
wn = turtle.Screen()

tess = turtle.Turtle()
tess.shape("turtle")
tess.color("pink")
tess.pensize(2)

alex = turtle.Turtle()
alex.shape("turtle")
alex.color("green")

i = 1
while i <= 3:
    tess.forward(80)
    tess.left(120)
    i += 1

alex.penup()
alex.right(90)
alex.forward(100)
alex.left(90)
alex.pendown()


i = 1
while i <= 4:
    alex.forward(80)
    alex.left(90)
    i += 1

wn.mainloop()
