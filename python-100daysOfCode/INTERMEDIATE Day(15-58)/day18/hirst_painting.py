# import colorgram

# colors = colorgram.extract("C:/Users/Harshit Boghara/vs_codeProjects/python-100daysOfCode/INTERMEDIATE/day18/image1.jpg", 8) #filr not found error

# print(colors)

import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
tim.speed(0)
tim.penup()
tim.hideturtle()
color_list = [(100, 134, 97), (125, 37, 155), (123, 50, 68), (180, 35, 100), (160, 140, 150), (120, 120, 160), (122,
                                                                                                                33, 55), (22, 140, 60), (20, 100, 100), (40, 20, 150), (25, 60, 155), (12, 38, 78), (15, 36, 144), (100, 200, 123)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

num_dots = 100
for dot_count in range(1, num_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()
