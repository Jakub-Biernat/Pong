from turtle import Turtle, Screen

WIDTH = 800
HEIGHT = 600


def up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

screen.listen()
screen.onkeypress(up, "w")
screen.onkeypress(down, "s")


paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.setposition(x=350, y=0)

is_running = True
while is_running:
    screen.update()


























screen.exitonclick()