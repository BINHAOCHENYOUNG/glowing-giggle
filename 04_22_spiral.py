import turtle
NUM_CIRCLE = 36
RADIUS = 100
ANGLE = 10
ANIMATIONSPEED = 0

turtle.speed(ANIMATIONSPEED)
for x in range(NUM_CIRCLE):
    turtle.circle(RADIUS)
    turtle.left(ANGLE)

turtle.done()