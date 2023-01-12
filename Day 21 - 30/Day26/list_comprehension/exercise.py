
numbers = [1, 2, 3, 4, 5]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Marek"
letter_list = [letter for letter in name]
print(letter_list)

new_list = [n * 2 for n in range(1, 5)]
print(new_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name.upper() for name in names if len(name) > 5]
print(short_names)

