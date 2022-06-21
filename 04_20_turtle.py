import turtle
for x in range (4):
    turtle.forward(100)
    turtle.right(90)


turtle.penup()
turtle.goto(200,0)
turtle.pendown()

for x in range (8):
    turtle.forward(100)
    turtle.right(45)

for r in range(8):
    turtle.penup()
    turtle.right(10)
    turtle.forward(10)
    turtle.pendown()
    for x in range (8):
        turtle.forward(100)
        turtle.right(45)
        
turtle.done()