from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos, HEIGHT):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.direction = 0
        self.screen_height = HEIGHT
        self.shape("square")
        self.shapesize(5,1,0)
        self.color("white")
        self.penup()
        self.goto(x_pos, y_pos)

    def up(self):
        if self.y_pos + 60 < self.screen_height/2-40:
            self.y_pos += 60
            self.goto(self.x_pos, self.y_pos)

    def down(self):
        if self.y_pos - 60 > -self.screen_height/2+40:
            self.y_pos -= 60
            self.goto(self.x_pos, self.y_pos)