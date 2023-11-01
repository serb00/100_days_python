import pandas


df = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_alphabet = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phonetics():
    user_input = input("Write your word: ")
    try:
        result = [NATO_alphabet[letter.upper()] for letter in user_input]
    except KeyError:
        print("Only latin letters, please.")
        generate_phonetics()
    else:
        print(result)


generate_phonetics()
