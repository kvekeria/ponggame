from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.user_score = 0
        self.hideturtle()
        self.computer_score = 0
        self.color("white")
        self.pu()
        self.goto(0, 200)
        self.write_to_board()

    def update_user(self):
        self.user_score += 1
        self.write_to_board()

    def update_computer(self):
        self.computer_score += 1
        self.write_to_board()

    def write_to_board(self):
        self.clear()
        self.write(f"{self.user_score} | {self.computer_score}", move=False, align='center',
                   font=('Courier', 80, 'normal'))
