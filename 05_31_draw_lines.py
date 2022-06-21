import turtle as chen

def main():
    line(0,100,-100,-100,"red")
    line(-100,-100,100,-100,"yellow")
    line(0,100,100,-100,"blue")
    chen.done()

def line(startX,startY,endX,endY,color):
    chen.penup()
    chen.hideturtle()
    chen.goto(startX,startY)
    chen.pendown()
    chen.pencolor(color)
    chen.goto(endX,endY)

main()
