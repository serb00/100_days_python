from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen setup parameters
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_BG_COLOR = "black"

# Game parameters
GAME_IS_ON = True
FPS = 10


def run():
    global GAME_IS_ON
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard(SCREEN_HEIGHT)
    screen = Screen()
    setup_screen(screen, snake)

    # main game loop
    while GAME_IS_ON:
        screen.update()
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 10:
            food.refresh_location()
            snake.grow_tail()
            scoreboard.increase_score()

        # Detect collision with the wall or own tail
        if snake.is_hitting_wall(screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT) or snake.is_hitting_tail():
            scoreboard.reset_score()
            snake.reset_snake()

        time.sleep(1 / FPS)

    screen.exitonclick()


def setup_screen(screen, snake):
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.title("Snake game")
    screen.bgcolor(SCREEN_BG_COLOR)
    screen.tracer(0)  # turn off tracer

    screen.listen()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)


if __name__ == "__main__":
    run()
