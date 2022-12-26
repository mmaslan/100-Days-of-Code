
from replit import clear
from blind_auction_art import logo

print(logo)

print("Welcome to secret auction program!")

bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name? ")
    price = input("What is your bid? $")
    bids[name] = price
    should_continue = str(input("Are there other bidders? Type: 'yes' or 'no'"))
    if should_continue == "no":
        bidding_finished = True
    elif should_continue == "yes":
        clear()
    else:
        print("Please write 'yes' or 'no'")
