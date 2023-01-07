
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        paddle = Turtle()
        paddle.shape("square")
        paddle.color("white")
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.penup()
        paddle.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)