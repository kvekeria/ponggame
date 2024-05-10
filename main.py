from turtle import Turtle, Screen

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle = Turtle(shape='square')
paddle.shapesize(5, 1)
paddle.color("white")
paddle.pu()
paddle.goto(350, 0)
game_is_on = True


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)



def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)



screen.listen()
screen.onkey(key="Up", fun=go_up)
screen.onkey(key="Down", fun=go_down)

while game_is_on:
    screen.update()

screen.exitonclick()
