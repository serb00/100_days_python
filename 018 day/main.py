import random
import turtle
from turtle import Turtle, Screen, colormode
from random import randint

timmy = Turtle()
# # draw n_sided_shapes
# colormode(255)
# for angles in range(3, 20):
#     timmy.color(randint(0, 255),
#                 randint(0, 255),
#                 randint(0, 255))
#     for _ in range(angles):
#         timmy.forward(100)
#         timmy.right(360 / angles)


angles = [0, 90, 180, 270]
colormode(255)
timmy.pensize(1)
timmy.speed(0)

screen = Screen()


def randomize_color():
    timmy.color(randint(0, 255),
                randint(0, 255),
                randint(0, 255))

# # draw random walk
# for _ in range(1000):
#     randomize_color()
#     random_angle = random.choice(angles)
#     timmy.right(random_angle)
#     timmy.forward(20)

for i in range(90):
    randomize_color()
    timmy.circle(100)
    timmy.right(360 / 90)


screen.exitonclick()