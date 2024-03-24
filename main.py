from turtle import Screen
from paddle import Paddle
from ball import  Ball
import time

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
ball = Ball()

screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")


is_running = True
while is_running:
    screen.update()
    time.sleep(0.05)
    ball.move()

    if ball.ycor() <= -280 or ball.ycor() >= 280:
        ball.bounce_on_wall()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_on_paddle()


























screen.exitonclick()
