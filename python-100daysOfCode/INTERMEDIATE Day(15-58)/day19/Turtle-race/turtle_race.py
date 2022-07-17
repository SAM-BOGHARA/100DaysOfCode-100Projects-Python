from turtle import *
import turtle as t
import random as r


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
make_bet = screen.textinput(
    title="Make Your Bet", prompt="Which turtle will win the race? Enter your choice").lower()
# print(make_bet)


colors = ["red", "green", "blue", "yellow", "orange", "purple", "black"]

y_positions = [-70, -40, -10, 20, 50, 80, 110]

all_turtles = []

for i in range(0, 7):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)

if make_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == make_bet:
                print(f"You won!, The {winning_color} turtle is the winner!")
            else:
                print(f"You lost!, The {winning_color} turtle is the winner!")
        random_distance = r.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
