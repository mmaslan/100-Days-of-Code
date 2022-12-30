
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

            guess = input("Who has more followers? Type 'A' or 'B': ").lower()
            a_followers_count = account_a["follower_count"]
            b_followers_count = account_b["follower_count"]
            is_correct = check_answer(guess, a_followers_count, b_followers_count)

            clear()

            print(logo)
            if is_correct:
                score += 1
            else:
                game_should_continue = False
                print(f"Sorry, that's wrong. Final score: {score}")



run_game()