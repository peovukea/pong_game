from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

starting_positions = [(350, 0), (-350, 0)]

HEIGHT = 600
WIDTH = 800

scoreboard = Scoreboard()
r_paddle = Paddle(starting_positions[0])
l_paddle = Paddle(starting_positions[1])

screen = Screen()
screen.bgcolor('black')
screen.setup(WIDTH, HEIGHT)
screen.title('Pong Game')
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')
screen.update()

ball = Ball()

while True:
    speed = 0.1
    screen.update()
    sleep(speed)
    ball.move()

    # detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.change_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.change_x()
        if speed - 0.01 < 0.01:
            speed = 0.01
        else:
            speed -= 0.01

    # if r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_score += 1
        scoreboard.update_scoreboard()

    # if l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_score += 1
        scoreboard.update_scoreboard()

screen.exitonclick()
