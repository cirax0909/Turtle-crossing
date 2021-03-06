from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.goto(x=-220, y=260)
        self.write(f'Level: {self.level}', move=False, align='center', font=FONT)

    def update_scoreboard(self):
        self.goto(x=0, y=0)
        self.write("Game over", move=False, align='center', font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f'Level: {self.level}', move=False, align='center', font=FONT)

