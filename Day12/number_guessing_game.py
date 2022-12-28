
from random import randint
from number_guessing_game_art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def compare(guess, answer, turns):

    if guess == answer:
        return turns - 1
    if guess > answer:
        print("Too low.")
        return turns - 1
    elif guess < answer:
        print("Too high.")
        return turns - 1
    else:
        print(f"You got it! The answer was {number_to_guess}.")


def the_game():

    print(logo)

    answer = randint(1, 100)
    is_game_over = False

    print("I'm thinking of number between 1 and 100")
    difficulty = input("Choose a difficulty: 'easy' or 'hard.")

    if difficulty.lower == 'easy':
        turns = EASY_LEVEL_TURNS
        return "You have 10 attempts remaining to guess the number."
    elif difficulty.lower == 'hard':
        turns = HARD_LEVEL_TURNS
        return "You have 5 attempts remaining to guess the number."


# You've run out of guesses, you lose.
