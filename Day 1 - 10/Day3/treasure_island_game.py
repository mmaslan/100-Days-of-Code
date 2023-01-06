print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************''')

print("Welcome to Treasure Island.")
print("Your mission is to find treasure.")
print("Welcome to Treasure Island")

choice1 = input('You\'re at crossroad, where do you want to go? Type "left" or "right".').lower()

if choice1 == "left":
    choice2 = input(
        'You\'ve have came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. '
        'Type "swim" to swim across.').lower()
    if choice2 == "wait":
        choice3 = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and "
                        "one blue. Which color do you chose?").lower()
        if choice3 == "red":
            print("The room is full of fire. Game over.")
        elif choice3 == "yellow":
            print("You have found a treasure! You win!")
        elif choice3 == "blue":
            print("Skeleton attack you, you die.")
        else:
            print("The door does not exist, it was a spell, you die.")
    else:
        print("You got attacked by angry trout. Game over.")
else:
    print("You fell into hole. Game over")
