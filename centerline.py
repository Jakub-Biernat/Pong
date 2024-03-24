from turtle import Turtle


class CenterLine(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.draw_line()

    def draw_line(self):
        self.goto(0, -300)
        while self.ycor() < 330:
            new_y = self.ycor() + 20
            if self.isdown():
                self.penup()
            else:
                self.pendown()
            self.goto(0, new_y)