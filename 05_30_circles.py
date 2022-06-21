import turtle

def main():
    turtle.hideturtle()
    circle(0,0,50,"red")
    turtle.done()

def circle(x,y,radius,color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(radius)
    turtle.end_fill()
main()