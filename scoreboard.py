from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.refresh()

    def write_score(self, arg):
        self.write(arg, align=ALIGNMENT, font=FONT)

    def add_l(self):
        self.l_score += 1
        self.refresh()

    def add_r(self):
        self.r_score += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(-100, 200)
        self.write_score(self.l_score)
        self.goto(100, 200)
        self.write_score(self.r_score)
