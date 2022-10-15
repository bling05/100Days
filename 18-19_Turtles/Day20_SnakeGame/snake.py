import turtle

MOVE_DIST = 20
STARTING_POS = [(0,0), (-MOVE_DIST,0), (-2*(MOVE_DIST),0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POS:
            self.add_segment(pos)

    def add_segment(self, pos):
        new_segment = turtle.Turtle("square")
        new_segment.color("white")
        new_segment.up()
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def grow(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != 270: self.head.seth(90)
    def left(self):
        if self.head.heading() != 0: self.head.seth(180)
    def down(self):
        if self.head.heading() != 90: self.head.seth(270)
    def right(self):
        if self.head.heading() != 180 : self.head.seth(0)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)