
import random
from higher_lower_art import logo, vs
from game_data import data
from replit import clear


def random_data_accounts():
    return random.choice(data)


def format_data(accounts):
    name = data['name']
    description = data['description']
    country = data['country']
    return f"{name}, {description}, from {country}"

def run_game():



    print(logo)

    print(f"Compare A: {name}, {description}, from {country}")

    print(vs)

    print(f"Against B: {name}, {description}, from {country}")


clear()