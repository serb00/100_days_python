import pandas
import turtle


def find_state_by_name(state_name: str, data_frame):
    state_guess = data_frame[data_frame["state"] == state_name]
    if not state_guess.empty:
        x = int(state_guess["x"].item())
        y = int(state_guess["y"].item())
        remove_state_from_df(data_frame, state_guess.index)
    else:
        x = y = None
    return x, y


def remove_state_from_df(data_frame, index):
    data_frame.drop(index, inplace=True)


def put_name_on_screen(x, y, user_guess):
    text_turtle = turtle.Turtle()
    text_turtle.hideturtle()
    text_turtle.write(user_guess, align="center", font=("Arial", 16, "normal"))
    frames = 20
    for frame in range(frames):
        turtle.delay(int(100 / frames))
        text_turtle.undo()  # Remove the previous text
        text_turtle.penup()
        text_turtle.goto(x * frame / frames, y * frame / frames)
        text_turtle.pendown()
        text_turtle.write(user_guess, align="center", font=("Arial", 16, "normal"))


def game_won(win, data_frame: pandas.DataFrame = None):
    text_turtle = turtle.Turtle()
    text_turtle.hideturtle()
    text_turtle.write("You WON!!!" if win else "You lost :(", align="center", font=("Arial", 16, "normal"))
    if not win:
        data_frame.to_csv("states_to_learn.csv")


def run():
    df = pandas.read_csv("50_states.csv")
    states_count: int = int(df.count(0).iloc[0])  # get # of states
    screen = turtle.Screen()
    screen.bgpic("blank_states_img.gif")
    screen.setup(725, 491)
    screen.title("Guess all states")

    game_is_on: bool = True
    score = 0

    while game_is_on:
        user_guess = screen.textinput(f"{score}/50 states guessed", "Enter state name:").title()
        if user_guess.lower() == "exit":
            game_is_on = False
            game_won(False, df)

        x, y = find_state_by_name(user_guess, df)
        if x is not None:
            put_name_on_screen(x, y, user_guess)
            score += 1

        if score == states_count:
            game_is_on = False
            game_won(True)

    screen.exitonclick()


if __name__ == "__main__":
    run()
