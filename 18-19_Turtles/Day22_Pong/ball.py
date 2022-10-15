from turtle import Turtle
import random

SPEED = 10

class Ball(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_velocity = random.choice([SPEED,-SPEED])
        self.y_velocity = random.choice([SPEED,-SPEED])
        self.shape("circle")
        self.shapesize(1,1,0)
        self.color("pink")
        self.penup()

    def move(self):
        self.x_pos += self.x_velocity
        self.y_pos += self.y_velocity
        self.goto(self.x_pos, self.y_pos)

    def bounce(self):
        self.y_velocity *= -1

    def hit(self):
        self.x_velocity *= -1

    def reset_pos(self):
        self.x_pos = 0
        self.y_pos = 0
        self.x_velocity = random.choice([SPEED,-SPEED])
        self.y_velocity = random.choice([SPEED,-SPEED])