from turtle import Turtle
import random
import icecream
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars: list[Turtle] = []

    def add_car(self):
        car = Turtle(shape="square")
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=0.5, stretch_len=1)
        car.penup()
        car.setposition(300, random.randint(-270, 270))
        car.setheading(180)
        self.cars.append(car)

    def move_cars(self, current_level):
        for car in self.cars:
            new_x = car.xcor() - STARTING_MOVE_DISTANCE - current_level * MOVE_INCREMENT
            car.setposition(new_x, car.ycor())

    def clean_cars_not_visible(self):
        for car in self.cars:
            if car.xcor() < -300:
                self.cars.remove(car)
                car.hideturtle()
                del car

    def is_colliding_object(self, turtle: Turtle):
        for car in self.cars:
            if car.distance(turtle.pos()) < 10:
                return True
        return False
