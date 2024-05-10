from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
game_is_on = True
user = Paddle(-360,0)
computer = Paddle(350,0)


screen.listen()
screen.onkey(key="Up", fun=user.go_up)
screen.onkey(key="Down", fun=user.go_down)

while game_is_on:
    screen.update()

screen.exitonclick()
