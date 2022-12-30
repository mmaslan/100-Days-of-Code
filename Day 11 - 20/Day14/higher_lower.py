
import random
from higher_lower_art import logo, vs
from game_data import data


def random_data():
    return random.choice(data)


def run_game():



    print(logo)

    print(f"Compare A: {name}, {description}, from {country}")

    print(vs)

    print(f"Against B: {name}, {description}, from {country}")