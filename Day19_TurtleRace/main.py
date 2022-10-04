import turtle
import random

is_race_on = False
screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.up()
    new_turtle.goto(-230, y_positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else: 
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()