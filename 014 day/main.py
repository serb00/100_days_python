from game_data import data
from art import logo, vs
from os import system
import random


def format_data(person):
    return (f"{person['name']}, a {person['description'].lower()}"
            f" from {person['country']}")


def get_followers(person: dict) -> int:
    """
    Gets the number of followers by the dict instance of a person
    :param person:
    :return int:
    """
    return int(person['follower_count'])


def display_compare(person1, person2):
    print(f"Compare A: {format_data(person1)}")
    print(vs)
    print(f"Against B: {format_data(person2)}")


def pick_next():
    return random.choice(data)


def get_player_input() -> int:
    """
    Gets the player input and returns 1 or 2 as a result.
    If input is not correct informs player and ask for input again.
    :rtype: int
    :return:
    """
    input_correct = False
    while not input_correct:
        player_input = input("Who has more followers? Type 'A' or 'B':")
        if player_input == 'A' or player_input == 'a':
            return 1
        elif player_input == 'B' or player_input == 'b':
            return 2
        else:
            print("Wrong input. Please type 'A' or 'B'.")


def guess_is_correct(person1: dict, person2: dict, guess: int) -> bool:
    if get_followers(person1) >= get_followers(person2) and guess == 1:
        return True
    elif get_followers(person1) <= get_followers(person2) and guess == 2:
        return True
    else:
        return False


def display_game_over(player_score):
    print(logo)
    print(f"Sorry, that's wrong. Your final score: {player_score}")


score = 0
game_over = False

pick_1 = pick_next()

while not game_over:
    system('clear')
    print(logo)
    if score > 0:
        print(f"You're right. Current score: {score}")
    pick_2 = pick_next()
    display_compare(pick_1, pick_2)
    selection = get_player_input()
    if guess_is_correct(pick_1, pick_2, selection):
        score += 1
        if selection == 2:
            pick_1 = pick_2
    else:
        game_over = True

display_game_over(score)
