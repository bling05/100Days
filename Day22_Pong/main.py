import turtle
import paddle
import ball
import time
import scoreboard

WIDTH = 800
HEIGHT = 600 

screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
turtle.speed("fastest")
turtle.tracer(0)

paddle1 = paddle.Paddle(-350, 0, HEIGHT)
paddle2 = paddle.Paddle(350, 0, HEIGHT)
ball1 = ball.Ball(0, 0)
board = scoreboard.Scoreboard()

screen.listen()
screen.onkeypress(paddle1.up, "w")
screen.onkeypress(paddle1.down, "s")
screen.onkeypress(paddle2.up, "o")
screen.onkeypress(paddle2.down, "l")

on = True
delay = 0.001
while on:
    time.sleep(delay)
    screen.update()
    ball1.move()
    
    if ball1.y_pos > HEIGHT/2-40 or ball1.y_pos < -HEIGHT/2+40:
        ball1.bounce()

    collision1 = range(paddle1.y_pos-50, paddle1.y_pos+50)
    collision2 = range(paddle2.y_pos-50, paddle2.y_pos+50)

    if (ball1.y_pos in collision1 and ball1.x_pos < -320) or (ball1.y_pos in collision2 and ball1.x_pos > 320):
        ball1.hit()

    if ball1.x_pos > 400:
        board.p1_point()
        ball1.reset_pos()

    if ball1.x_pos < -400:
        board.p2_point()
        ball1.reset_pos()

screen.exitonclick()
