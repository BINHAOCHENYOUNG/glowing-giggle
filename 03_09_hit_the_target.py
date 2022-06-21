#In this program user ask to enter angle an force to hit the target 

import turtle

#Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TARGET_LLEFT_X = 100 #Target's lower-left X coordination
TARGET_LLEFT_Y = 250 #Target's lower-left Y coordination
TARGET_WIDTH = 25
FORCE_FACTOR = 30 #a numbber that will multiply to the distance 
PROJECTILE_SPEED = 1
NORTH = 90
SOUTH = 270
EAST = 0
WEST =180

#Set up the window
turtle.setup(SCREEN_HEIGHT,SCREEN_WIDTH)

#Draw the target
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X,TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)



turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)

turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)

turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()


# Center the turtle
turtle.goto(0,0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

#Get the angle and force  
angle = float(input("Enter the projectile's angle: "))

force = float(input("Enter the launch force: "))

#Calculate
distance =force * FORCE_FACTOR

#Set heading 
turtle.setheading(angle)

#launch the projectile 
turtle.pendown()
turtle.forward(distance)

#did it hit the target?
if (turtle.xcor() >=TARGET_LLEFT_X and 
    turtle.xcor() <=(TARGET_LLEFT_X +TARGET_WIDTH) and
    turtle.ycor() >=TARGET_LLEFT_Y and 
    turtle.ycor() <=(TARGET_LLEFT_Y + TARGET_WIDTH)): 
    print("Target hit!!!, you have got 1000000 points")
else:
    print("You missed the target~")


turtle.done()

