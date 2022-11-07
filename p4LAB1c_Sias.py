import turtle
wn = turtle.Screen()
snowflake = turtle.Turtle()
snowflake.speed(10)
snowflake.color("blue")
snowflake.pensize(8)

for i in range(8):
    snowflake.forward(90)
    for i in range(3):
        snowflake.left(45)
        snowflake.forward(25)
        snowflake.backward(25)
        snowflake.right(90)
        snowflake.forward(25)
        snowflake.backward(25)
        snowflake.left(45)
        snowflake.backward(30)
    snowflake.right(45)

wn.mainloop()
    
        
