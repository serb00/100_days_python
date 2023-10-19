from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen setup parameters
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_BG_COLOR = "black"

# Game parameters
GAME_IS_ON = True
FPS = 10


def run():
    global GAME_IS_ON
    screen = Screen()
    scoreboard = Scoreboard(SCREEN_HEIGHT)
    p1 = Paddle((-350, 0))
    p2 = Paddle((350, 0))
    setup_screen(screen, p1, p2)
    ball = Ball()

    while GAME_IS_ON:
        screen.update()

        ball.move()

        # Detect collision with paddle
        colliding = ball.is_colliding_with_paddle(p1, p2)
        if colliding[0]:
            ball.reflect_from_paddle()

        # Detect collision with the up and bottom walls
        if ball.is_colliding_with_walls():
            ball.reflect_from_wall()

        # Detect collision with the gates
        if ball.hit_gates():
            if ball.xcor() > 0:
                scoreboard.increase_score("p1")
            else:
                scoreboard.increase_score("p2")
            ball.reset_position()

        scoreboard.display_score()

        # Check if either player won
        if scoreboard.p1_score > 2 or scoreboard.p2_score > 2:
            scoreboard.game_over()
            GAME_IS_ON = False

        time.sleep(1 / FPS)

    screen.exitonclick()


def setup_screen(screen, paddle1, paddle2):
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.title("Snake game")
    screen.bgcolor(SCREEN_BG_COLOR)
    screen.tracer(0)  # turn off tracer

    screen.listen()
    screen.onkey(key="w", fun=paddle1.up)
    screen.onkey(key="s", fun=paddle1.down)
    screen.onkey(key="Up", fun=paddle2.up)
    screen.onkey(key="Down", fun=paddle2.down)


if __name__ == "__main__":
    run()
