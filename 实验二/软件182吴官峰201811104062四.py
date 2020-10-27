import turtle

L =320

def draw():
    for a in range(4):
        for i in range(4):   
            turtle.begin_fill()
            for j in range(4):
                turtle.forward(L/8)
                turtle.left(90)
            turtle.end_fill()
            turtle.penup()
            turtle.forward(L/4)
            turtle.pendown()
        turtle.penup()
        turtle.backward(L)
        turtle.left(90)
        turtle.forward(L/4)
        turtle.right(90)
        turtle.pendown()

turtle.pensize(3)
turtle.color("red")
turtle.penup()
turtle.goto(-L/2,-L/2)
turtle.setheading(0)
turtle.pendown()
for i in range(4):
    turtle.forward(L)
    turtle.left(90)
turtle.speed(11)
turtle.color("black")
draw()
turtle.penup()
turtle.goto(-120,-120)
turtle.pendown()
draw()

