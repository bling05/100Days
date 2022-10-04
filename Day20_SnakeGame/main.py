import turtle
import time

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
turtle.tracer(0)

starting_pos = [(0,0), (-20,0), (-40,0)]
segments = []

for pos in starting_pos:
    new_segment = turtle.Turtle("square")
    new_segment.color("white")
    new_segment.up()
    new_segment.goto(pos)
    segments.append(new_segment)

on = True
while on:
    for seg in segments:
        seg.fd(20)
        screen.update()
    time.sleep(0.2)

turtle.exitonclick()