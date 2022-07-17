from turtle import * 
import turtle as t
import random
timmy = Turtle()
timmy.shape('circle')

t.colormode(255)

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    my_tuple = (r,g,b)
    return my_tuple


direction = [0, 90, 180, 270]
count = [20,25,30,40,50,35,45]
timmy.speed(0)

timmy.pensize(7)   #another approach on line 47
for i in range(500):
    timmy.width(12)
    timmy.color(random_colour())
    # timmy.random.choice(direction)
    timmy.forward(random.choice(count))
    timmy.setheading(random.choice(direction))



screen = Screen()
screen.exitonclick()
