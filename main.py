# PONG!!
# classes to great: board, paddle, ball, score

# steps:
# create screen
# create and move a paddle
# create another paddle
# create the ball and make it move
# detect collision with wall and make it bounce
# detect collision with paddle
# detect when paddle misses
# keep score

from turtle import Turtle, Screen
from board import Board
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("PyPONG")
screen.tracer(0)

board = Board()
r_paddle = Paddle(350)
l_paddle = Paddle(-360)
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
ball_speed = 0.1
while game_on:
    time.sleep(ball_speed)
    screen.update()
    ball.move()
    # detect ball hits upper or lower balls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect ball hits paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -330 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
        ball_speed *= 0.9

    # detect if a score happens
    if ball.xcor() > 380:
        print('Player 1 scores!')
        board.player1_score()
        ball.reset_position()
        ball_speed = 0.1

    elif ball.xcor() < -380:
        print('Player 2 scores!')
        board.player2_score()
        ball.reset_position()
        ball_speed = 0.1


screen.exitonclick()
