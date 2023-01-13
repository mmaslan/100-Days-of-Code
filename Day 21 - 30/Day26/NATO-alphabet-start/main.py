
import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

name = input("Enter your name: ").upper()

output_list = [phonetic_dict[letter] for letter in name]
print(output_list)


