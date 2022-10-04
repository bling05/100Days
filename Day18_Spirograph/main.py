import turtle
import random

myturt = turtle.Turtle()
myturt.speed("fastest")
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

#  Degree of movement
dom = 5 
for i in range(int(360/dom)):
    myturt.color(random_color())
    myturt.circle(80, None, None)
    myturt.rt(dom)

turtle.Screen().exitonclick()