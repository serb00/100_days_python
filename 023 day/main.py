import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def run():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title("Turtle game")
    screen.tracer(0)

    p1 = Player()
    screen.listen()
    screen.onkey(p1.move_up, "w")

    car_manager = CarManager()
    scoreboard = Scoreboard()

    game_is_on = True
    frames_rendered = 0
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        frames_rendered += 1

        scoreboard.display_score()

        if frames_rendered > (9 - scoreboard.level):
            frames_rendered = 0
            car_manager.add_car()
            car_manager.add_car()

        car_manager.move_cars(scoreboard.level)

        car_manager.clean_cars_not_visible()

        # if car_manager.is_colliding_object(p1):
        #     game_is_on = False
        #     scoreboard.game_over(win=False)

        for car in car_manager.cars:
            if car.distance(p1.pos()) < 10:
                game_is_on = False
                scoreboard.game_over(win=False)

        if p1.is_finished():
            if not scoreboard.is_last_level():
                scoreboard.next_level()
                scoreboard.increase_score(1)
                p1.set_starting_position()
            else:
                game_is_on = False
                scoreboard.game_over(win=True)

    screen.exitonclick()


if __name__ == "__main__":
    run()
