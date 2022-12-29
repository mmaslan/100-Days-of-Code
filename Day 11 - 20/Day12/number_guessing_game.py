
from random import randint
from number_guessing_game_art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def compare(guess, answer, turns):

    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


def set_difficulty():
    difficulty = input("Choose a difficulty: 'easy' or 'hard': ")
    if difficulty == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def the_game():

    print(logo)

    answer = randint(1, 100)
    turns = set_difficulty()
    guess = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = compare(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
        elif guess != answer:
            print("Guess again.")


the_game()