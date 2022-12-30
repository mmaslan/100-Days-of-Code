
import random
from higher_lower_art import logo, vs
from game_data import data
from replit import clear


def random_accounts():
    return random.choice(data)


def format_data(accounts):
    name = data['name']
    description = data['description']
    country = data['country']
    return f"{name}, {description}, from {country}"


def check_answer(guess, followers_a, followers_b):
    if followers_a > followers_b:
        return guess == "a"
    else:
        return guess == "b"


def run_game():

    score = 0
    game_should_continue = True
    account_a = random_accounts()
    account_b = random_accounts()

    print(logo)

    while game_should_continue:
        account_a = account_b
        account_b = random_accounts()

        while account_a == account_b:
            account_b = random_accounts()

            print(f"Compare A: {format_data(account_a)}")

            print(vs)

            print(f"Against B: {format_data(account_b)}")


run_game()