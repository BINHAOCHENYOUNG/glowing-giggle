import turtle

def main():
    turtle.hideturtle()
    square(100,0,50,"red")
    turtle.done()

def square(x,y,width, color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pendown()
    for count in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()

    

main()
