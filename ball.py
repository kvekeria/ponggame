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
        self.y_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.x_move *= -1
        if self.x_move < 0:
            self.x_move = -2
            self.y_move = -2
        else:
            self.x_move = 2
            self.y_move = 2

    def increase_speed(self, amt):
        if self.x_move < 0:
            self.x_move -= amt
        elif self.x_move > 0:
            self.x_move += amt

        if self.y_move < 0:
            self.y_move -= amt
        elif self.y_move > 0:
            self.y_move += amt

