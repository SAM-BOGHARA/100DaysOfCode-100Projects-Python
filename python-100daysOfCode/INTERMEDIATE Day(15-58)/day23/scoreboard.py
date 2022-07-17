from turtle import *

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-275, 265)
        self.update()

    def update(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increse_level(self):
        self.level += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

