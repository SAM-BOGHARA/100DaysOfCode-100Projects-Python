from turtle import * 
import turtle as t
import random
timmy = Turtle()
timmy.shape('circle')


# 2 dashed line
for i in range(20):
    # timmy.setposition(-300,0)
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()



screen = Screen()
screen.exitonclick()
