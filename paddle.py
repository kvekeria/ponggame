from turtle import Turtle, Screen

class Paddle:
    def __init__(self, x_cor, y_cor):
        self.paddle = Turtle(shape='square')
        self.paddle.shapesize(5, 1)
        self.paddle.color("white")
        self.paddle.pu()
        self.paddle.goto(x_cor, y_cor)

    def go_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)