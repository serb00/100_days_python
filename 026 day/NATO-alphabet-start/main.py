import pandas


df = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_alphabet = {row.letter: row.code for (index, row) in df.iterrows()}

user_input = input("Write your word: ")
result = [NATO_alphabet[letter.upper()] for letter in user_input]
print(result)
