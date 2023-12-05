from secrets import randbelow
from flask import Flask, session
from enum import Enum

MIN_VALUE = 1
MAX_VALUE = 10
GUESSES_PER_GAME = 5


class GuessResult(Enum):
    LOWER = "Your number is lower.<br/>You have {self.guesses_left} " \
        "attempts left."
    HIGHER = "Your number is higher.<br/>You have {self.guesses_left} " \
        "attempts left."
    CORRECT = "You guessed the number!<br/>Still having {self.guesses_left} " \
        "attempts left."
    OUT_OF_BOUNDS = "Your number is out of bounds.<br/>Number should be " \
        " between {MIN_VALUE} and {MAX_VALUE}."
    OUT_OF_GUESSES = "You ran out of guesses.<br/>Game over."
    UNKNOWN = "Unknown behavior"


class Game:
    def __init__(self) -> None:
        self.number = randbelow(MAX_VALUE - MIN_VALUE + 1) + MIN_VALUE
        self.guesses_left = GUESSES_PER_GAME

    def reset_game(self):
        self.number = randbelow(MAX_VALUE - MIN_VALUE + 1) + MIN_VALUE
        self.guesses_left = GUESSES_PER_GAME

    def guess_number(self, number):
        self.guesses_left -= 1
        if self.guesses_left < 0:
            return GuessResult.OUT_OF_GUESSES.value
        elif number < MIN_VALUE or number > MAX_VALUE:
            return GuessResult.OUT_OF_BOUNDS.value
        elif MIN_VALUE < number < self.number:
            return GuessResult.LOWER.value
        elif MAX_VALUE > number > self.number:
            return GuessResult.HIGHER.value
        elif number == self.number:
            return GuessResult.CORRECT.value
        else:
            return GuessResult.UNKNOWN.value

    @property
    def answer(self):
        return str(self.number)


app = Flask(__name__)


@app.route('/')
def index():
    session['game'] = Game()
    return "Guess the number!"


@app.route('/<int:number>')
def guess(number):
    game = session.get('game')
    if game is None:
        game = Game()
        session['game'] = game
    return game.guess_number(number)


@app.route('/answer')
def func_name():
    game = session.get('game')
    if game is None:
        game = Game()
        session['game'] = game
    return game.answer


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)
