import random
from turtle import Turtle
import random

BALL_SPEED = 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape("circle")
        self.penup()
        self.setposition(x=0, y=0)

        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def is_colliding_with_paddle(self, p1, p2):
        if self.xcor() > 330 and self.distance(p2) < 50:
            return True, p2
        elif self.xcor() < -330 and self.distance(p1) < 50:
            return True, p1
        else:
            return False, p1

    def reflect_from_paddle(self):
        if self.x_move > 0:
            self.x_move = int(-10 - random.random() * 10)
        else:
            self.x_move = int(10 + random.random() * 10)

    def is_colliding_with_walls(self):
        if self.ycor() > 280:
            return True
        elif self.ycor() < -280:
            return True
        else:
            return False

    def hit_gates(self):
        return abs(self.xcor()) > 370

    def reflect_from_wall(self):
        self.y_move *= -1

    def reset_position(self):
        self.setposition(x=0, y=0)
        self.reflect_from_paddle()
