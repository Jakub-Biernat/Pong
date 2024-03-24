from turtle import Turtle


class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_on_wall(self):
        self.y_move *= -1

    def bounce_on_paddle(self):
        self.x_move *= -1

    def restart(self):
        self.setposition(0, 0)
        self.bounce_on_paddle()
        self.bounce_on_wall()

