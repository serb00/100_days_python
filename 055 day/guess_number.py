from enum import Enum
from flask import Flask
from random import randint

MIN_VALUE = 0
MAX_VALUE = 10
GUESSES_PER_GAME = 5


class GuessResult(Enum):
    OUT_OF_BOUNDS = 1,
    LOWER = 2,
    HIGHER = 3,
    MATCH = 4,
    NO_GUESSES_LEFT = 5


class Game:
    def __init__(self) -> None:
        self.number = randint(MIN_VALUE, MAX_VALUE)
        self.guesses_left = GUESSES_PER_GAME

    # TODO: Make this function return codes using GuessResult
    # instead of strings
    # TODO: move reinitialization of game out from this function

    def guess_number(self, number):
        self.guesses_left -= 1
        if MIN_VALUE < number < self.number:
            return "Your number is lower.<br/>" \
                f"You have {self.guesses_left} attempts left."
        elif MAX_VALUE > number > self.number:
            return "Your number is higher.<br/>" \
                f"You have {self.guesses_left} attempts left."
        elif number == self.number:
            self.__init__()
            return "You guessed the number!<br/>" \
                f"Still having {self.guesses_left} attempts left."
        elif number < MIN_VALUE or number > MAX_VALUE:
            return "Your number is out of bounds.<br/>" \
                f"Number should be between {MIN_VALUE} and {MAX_VALUE}."
        elif self.guesses_left < 0:
            self.__init__()
            return "You ran out of guesses.<br/>Game over."
        else:
            return "Unknown behavior"

    def get_answer(self):
        return self.number.__str__()


app = Flask(__name__)
game = Game()


@app.route('/')
def index():
    return "Guess the number!"


@app.route('/<int:number>')
def guess(number):
    return game.guess_number(number)


@app.route('/answer')
def func_name():
    return game.get_answer()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)
