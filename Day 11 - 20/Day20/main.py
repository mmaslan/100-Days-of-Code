
from turtle import Turtle, Screen
import Time
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

screen.update()

while game_is_on:
    for seg in segments:
        seg.forward(20)



def turn_left():
    snake.left(90)


def turn_right():
    snake.right(90)



screen.exitonclick()