#This program demonstrate a function 

#1. Write mysum() function 
def mysum(num1,num2):
    mysum = num1 + num2
    print(mysum)


#2. Write myaver()function
def myaver(num1,num2,num3):
    myaver= (num1 + num2 + num3)/2
    print(myaver)

def circle(x,y,radiu,color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(radiu)
    turtle.end_fill()
    turtle.penup()



def rectangle(x,y,length,color):
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for t in range(4):
        turtle.forward(length)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()


        




#call a function
mysum(789,567)
myaver(123,321)

