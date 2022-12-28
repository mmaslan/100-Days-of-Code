
import random
from random import randint
from number_guessing_game_art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def roll_the_numbers():
    list_of_numbers = []
    for i in range(1, 101):
        list_of_numbers.append(i)
    random_number = random.choice(list_of_numbers)
    return random_number


def compare():
    pass


def the_game():

    print(logo)

    user_number = []
    computer_number = []
    turns = 0
    is_game_over = False

    print("I'm thinking of number between 1 and 100")
    difficulty = input("Choose a difficulty: 'easy' or 'hard.")
    if difficulty.lower == 'easy':
        turns = EASY_LEVEL_TURNS
    elif difficulty.lower == 'hard':
        turns = HARD_LEVEL_TURNS

    user_number.append(roll_the_numbers)
    computer_number .append(roll_the_numbers)
