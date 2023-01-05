
from turtle import Screen
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

game_is_on = True
score = 0
segments = []
food_position = []

starting_position = [(0, 0),(-20, 0),(-40, 0)]


while game_is_on:
    screen.update()
    time.sleep(0.1)