from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1,1,0)
        self.up()
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randrange(-280, 280+20, 20)
        random_y = random.randrange(-280, 280+20, 20)
        self.goto(random_x, random_y)
