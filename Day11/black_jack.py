
import random
from black_jack_art import logo
from replit import clear


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    pass


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False
    pass


def compare():
    pass


game = input("Do you want to play a game of Black Jack? Type 'yes' or 'no': ")

print(logo)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()