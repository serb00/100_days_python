import random
from os import system
from hangman_modules import words_list, stages, letters

# pick a random word from the list
word_to_guess = random.choice(words_list)

# create a blanc spaces to visualize a word
word_representation = ['_' for c in word_to_guess]

print(f"Word: {word_to_guess}")

# initialize game variables
game_over = False
won = False
lives = 6
replaced = 0

# main loop
while not game_over:
    # print hangman
    system('clear')
    print(f"{' '.join(word_representation)}")
    print(f"{stages[lives]}")

    # ask for next letter, get the first letter only
    letter_input = input("Guess the letter:").lower()[0]

    # check if letter wasn't already used
    if letter_input in letters:
        # search for letter in the word
        idx = 0
        found = False
        for c in word_to_guess:
            if c == letter_input:
                word_representation[idx] = c
                replaced += 1
                found = True
            idx += 1

        # remove letter from letters list
        letters.remove(letter_input)

        # take live if letter not found
        if not found:
            lives -= 1

        # end game if lives are over
        if lives < 1:
            game_over = True

        # end game and activate win state if all letters guessed
        if replaced == len(word_to_guess):
            game_over = True
            won = True

# print result message
if won:
    system('clear')
    print(f"You guessed right, "
          f"the word is: {(''.join(word_representation).upper())}")
    print("Flawless victory")
else:
    system('clear')
    print(f"The word was: {(word_to_guess.upper())}")
    print(f"{stages[lives]}")
    print("Try again.")
