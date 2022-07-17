from turtle import * 
import turtle as t
import random
timmy = Turtle()
timmy.shape('circle')


# 3 shapes in turtle graphics
num_sides = 3

colours = ['Cornflowerblue', 'DarkGoldenrod1', 'DarkGoldenrod2',
          'DarkGoldenrod3', 'IndianRed', 'LightSeaGreen','SlateGray']


def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


for side in range(3, 10):
    timmy.color(random.choice(colours))
    draw_shape(num_sides)
    num_sides += 1


screen = Screen()
screen.exitonclick()
