import turtle

turtle.hideturtle()
turtle.fillcolor('blue')
turtle.begin_fill()
for x in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

turtle.fillcolor('red')
turtle.penup()
turtle.goto(100,50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.fillcolor('cyan')
turtle.penup()
turtle.goto(100,100)
turtle.pendown()
turtle.begin_fill()
for x in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

turtle.done()