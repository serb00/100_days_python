from turtle import Turtle
import random

CELL_SIZE = 20
STRETCH = 0.5


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=STRETCH, stretch_wid=STRETCH)
        self.color("green")
        self.speed("fastest")
        self.refresh_location()

    def refresh_location(self):
        self.goto(x=random.randint(-14, 14) * CELL_SIZE,
                  y=random.randint(-14, 14) * CELL_SIZE)
