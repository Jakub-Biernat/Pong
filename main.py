from turtle import Screen
from paddle import Paddle

WIDTH = 800
HEIGHT = 600
L_POSITION = (-350, 0)
R_POSITION = (350, 0)


screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(position=L_POSITION)
r_paddle = Paddle(position=R_POSITION)

screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")


is_running = True
while is_running:
    screen.update()


























screen.exitonclick()
