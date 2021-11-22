from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.pencolor("white")

    def update_scoreboard(self):
        self.write("Game over", move=False, align='center', font=FONT)
