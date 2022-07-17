from sqlite3 import TimestampFromTicks
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.turtlesize(3)
timmy.setposition(-50,50)
timmy.color("DarkGoldenrod1")
timmy.forward(200)
timmy.setposition(20,20)
timmy.turtlesize(4)
timmy.backward(400)
timmy.turtlesize(5)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
