from turtle import Turtle


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.width(5)
        self.color('white')
        self.p1_score = 0
        self.p2_score = 0
        self.update_scoreboard()

    def draw_center(self):
        self.goto((0, -300))
        self.setheading(90)
        while self.ycor() < 280:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def player1_score(self):
        self.p1_score += 1
        self.update_scoreboard()

    def player2_score(self):
        self.p2_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.draw_center()
        self.goto(-100, 200)
        self.write(self.p1_score, align='center',
                   font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.p2_score, align='center',
                   font=('Courier', 80, 'normal'))
