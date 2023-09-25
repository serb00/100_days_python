import random
import turtle

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
DISTANCE_BETWEEN_TURTLES = 30
DISTANCE_FROM_EDGE = 20

screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
turtles: list[turtle.Turtle] = []
colors = ["red", "green", "coral", "blue", "yellow", "orange", "purple"]


def run():
    winner = ""
    user_guess = setup()

    while winner == "":
        for t in turtles:
            t.forward(random.randint(11, 31))
            if t.xcor() > SCREEN_WIDTH / 2 - DISTANCE_FROM_EDGE:
                winner = t.pencolor()
                break

    check_winner(winner, user_guess)
    screen.exitonclick()


def check_winner(winner, user_guess):
    print(f"{winner.capitalize()} won the race!")
    if winner == user_guess:
        print("You guessed right!")
    else:
        print("Unfortunately, you guessed wrong.")


def setup():
    for color in colors:
        t = turtle.Turtle(shape="turtle")
        t.color(color)
        t.penup()
        turtles.append(t)
    num_turtles = len(turtles)
    upper_turtle_y_coordinate = int(num_turtles / 2 * DISTANCE_BETWEEN_TURTLES)
    for i in range(num_turtles):
        turtles[i].setpos(-SCREEN_WIDTH / 2 + DISTANCE_FROM_EDGE,
                          upper_turtle_y_coordinate - i * DISTANCE_BETWEEN_TURTLES)
    user_guess = screen.textinput("Guess the winner", "Select winner from list:\n"
                                                      "red, green, coral, blue, yellow, orange")
    return user_guess


if __name__ == "__main__":
    run()
