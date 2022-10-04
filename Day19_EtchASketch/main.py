import turtle

myturt = turtle.Turtle()
screen = turtle.Screen()

def move_forwards():
    myturt.forward(10)
def move_backwards():
    myturt.back(10)
def counter_clockwise():
    myturt.lt(30)
def clockwise():
    myturt.rt(30)
def clear_drawing():
    myturt.clear()
    myturt.up()
    myturt.home()
    myturt.down()

screen.listen()
screen.onkey(key="w",fun=move_forwards)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="a",fun=counter_clockwise)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="c",fun=clear_drawing)
screen.exitonclick()