import turtle

NUM_Circle = 20
Starting_radius = 20 
OFFset =10
Animationspeed = 0

turtle.speed(Animationspeed)
turtle.hideturtle

radius = Starting_radius

for count in range(NUM_Circle):
    turtle.circle(radius)
    x = turtle.xcor()
    y = turtle.ycor() - OFFset
    radius = radius + OFFset
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()


turtle.done()
