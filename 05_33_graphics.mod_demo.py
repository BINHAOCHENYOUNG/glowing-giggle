import chen_graphics
import turtle
#x,y,radius,color
#x,y,width,color
#startX,startY,endX,endY,color

def main():
    turtle.hideturtle()
    chen_graphics.circle(0,0,25,"yellow")
    chen_graphics.square(0,25,50, "red")
    chen_graphics.circle(50,50,25,"blue")
    chen_graphics.square(50,75,50, "green")


    chen_graphics.circle(50,-50,25,"green")
    chen_graphics.circle(100,0,25,"red")
    chen_graphics.square(50, -25, 50, "blue")
    chen_graphics.square(100, 25, 50, "yellow")

    turtle.done()



main()