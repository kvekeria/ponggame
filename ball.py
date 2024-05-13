from turtle import Turtle


class Ball(Turtle):

    def __init__(self, pos):
        super(Ball, self).__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1, 1)
        self.pu()
        self.goto(pos)
        self.change = True
        self.x_move = 2
        self.y_move = 2

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def change_direction(self):
        self.x_move *= -1
        self.y_move *= 1
