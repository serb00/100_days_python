import turtle

tim = turtle.Turtle()
screen = turtle.Screen()


def forwards():
    tim.forward(10)


def backwards():
    tim.backward(10)


def counter_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)


def clear_screen():
    tim.home()
    tim.clear()


def run():
    screen.listen()
    screen.onkey(key="w", fun=forwards)
    screen.onkey(key="s", fun=backwards)
    screen.onkey(key="a", fun=counter_clockwise)
    screen.onkey(key="d", fun=clockwise)
    screen.onkey(key="c", fun=clear_screen)

    screen.exitonclick()


if __name__ == "__main__":
    run()
