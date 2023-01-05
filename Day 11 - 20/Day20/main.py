
from turtle import Turtle, Screen
import time
import random


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_is_on = True
score = 0
segments = []
food_position = []


starting_position = [(0, 0),(-20, 0),(-40, 0)]
snake = Turtle("square")
snake.color("white")


for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments)):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)


screen.exitonclick()