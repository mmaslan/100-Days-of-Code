
import random
from black_jack_art import logo
from replit import clear


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

game = input("Do you want to play a game of Black Jack? Type 'yes' or 'no': ")

print(logo)

