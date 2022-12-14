from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        with open("high_score.txt") as data:
            self.high_score = int(data.read())
        self.up()
        self.hideturtle()
        self.goto(0,270)
        self.pencolor("white")
        self.update()

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align="center", font=('Courier', 14, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("Game over", align="center", font=("Courier", 14, 'normal'))
        if self.score > self.high_score:
            self.high_score = self.score
        with open("high_score.txt", "w") as data:
            data.write(f"{self.high_score}")