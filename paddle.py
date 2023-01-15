from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(x_pos, 0)

    def go_up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor()-20)
