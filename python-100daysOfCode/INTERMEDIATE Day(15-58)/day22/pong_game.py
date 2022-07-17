from turtle import *

from paddle import Paddle
from ball import Ball
from scoreboard import *
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game by shubham")
screen.tracer(0)


r_pad = Paddle((350, 0))
l_pad = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_pad.go_up, "Up")
screen.onkey(r_pad.go_down, "Down")

screen.onkey(l_pad.go_up, "w")
screen.onkey(l_pad.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_pad) < 50 and ball.xcor() > 320 or ball.distance(l_pad) < 50 and ball.xcor() > -340:
        ball.bounce_x()

    # detect miss by right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect miss by left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
