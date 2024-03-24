from turtle import Turtle


class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        angle = self.towards(x=400, y=300)
        self.setheading(angle)

    def move(self):
        self.forward(10)

