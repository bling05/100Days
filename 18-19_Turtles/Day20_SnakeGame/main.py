import turtle
import time
import food
import snake
import scoreboard

WIDTH = 600
HEIGHT = 600

def restart(snake, food, scoreboard):
    for seg in snake.segments:
        seg.reset()
        seg.hideturtle()
    food.reset()
    food.hideturtle()
    scoreboard.score = 0
    scoreboard.reset()
    scoreboard.hideturtle()

on = True
while on:
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("black")
    screen.title("Snake Game")
    turtle.tracer(0)

    snek = snake.Snake()
    fod = food.Food()
    board = scoreboard.Scoreboard()

    screen.listen()
    screen.onkeypress(snek.up, "w")
    screen.onkeypress(snek.left, "a")
    screen.onkeypress(snek.down, "s")
    screen.onkeypress(snek.right, "d")

    alive = True
    while alive:
        screen.update()
        time.sleep(0.1)
        snek.move()
        
        if snek.head.distance(fod) < 5:
            fod.refresh()
            snek.grow()
            board.update()

        if abs(snek.head.xcor()) > 280 or abs(snek.head.ycor())> 280:
            board.game_over()
            time.sleep(3)
            restart(snek,fod,board)
            break

        Break = False
        for seg in snek.segments[1:]:
            if snek.head.distance(seg) < 5:
                board.game_over()
                time.sleep(3)
                restart(snek,fod,board)
                Break = True
        if Break == True: break
    




screen.exitonclick()
