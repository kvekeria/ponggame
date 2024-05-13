from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
game_is_on = True
user = Paddle((-350, 0))
computer = Paddle((350, 0))
ball = Ball((0, 0))
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key="w", fun=user.go_up)
screen.onkey(key="s", fun=user.go_down)
screen.onkey(key="Up", fun=computer.go_up)
screen.onkey(key="Down", fun=computer.go_down)

while game_is_on:
    ball.move()
    screen.update()

    # Detect collision with the wall
    if ball.ycor() >= 287 or ball.ycor() <= -287:
        ball.bounce()

    # Detect collision with paddle
    if (ball.distance(user) < 50 or ball.distance(computer) < 50) and (ball.xcor() > 320 or ball.xcor() < -320):
        ball.change_direction()
        ball.increase_speed(1)

    # Detect out of bounds
    if ball.xcor() < -380:
        scoreboard.update_computer()
        ball.reset()

    if ball.xcor() > 380:
        scoreboard.update_user()
        ball.reset()

screen.exitonclick()
