
from random import randint
from number_guessing_game_art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def numbers():
    list_of_numbers = []
    for i in range(1, 101):
        list_of_numbers.append(i)

    print(list_of_numbers)


print("I'm thinking of number between 1 and 100")
difficulty = input("Choose a difficulty: 'easy' or 'hard.")
