
import random
import string

letters = list(string.ascii_letters)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator!")

number_of_letters = int(input("How many letters would you like in your password?\n"))
number_of_numbers = int(input("How many numbers would you like?\n"))
number_of_symbols = int(input("How many symbols would you like?\n"))

password = ''
password_list = []

for char in range(1, number_of_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, number_of_numbers + 1):
    password_list.append(random.choice(numbers))

for char in range(1, number_of_symbols + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

for char in password_list:
    password += char

message = f"Here is your password: {password}"
print(message)