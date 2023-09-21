import colorgram
import turtle
import random

# Global constants
PICTURE_ROWS = 14
PICTURE_COLUMNS = 9
FILE_NAME = 'hirst.jpg'
SPACE_PIXELS = 45
DOTS_SIZE = 20

# global variables
colors = []
color_index = 0


def get_next_color():
    global colors, color_index
    if color_index >= len(colors):
        color_index = 0
    next_color = colors[color_index].rgb
    color_index += 1
    return next_color


def get_random_color():
    global colors
    return random.choice(colors).rgb


def draw_picture(rows, columns):
    turtle.colormode(255)
    tim = turtle.Turtle()
    tim.speed(0)
    offset_x = -(columns / 2 * SPACE_PIXELS)
    offset_y = -(rows / 2 * SPACE_PIXELS)
    tim.penup()
    for row in range(rows):
        tim.setposition(0 + offset_x, row * SPACE_PIXELS + offset_y)
        for column in range(columns):
            tim.dot(DOTS_SIZE, get_random_color())
            tim.forward(SPACE_PIXELS)
    tim.setposition(1000, 1000)


def hirst(rows, columns):
    screen = turtle.Screen()
    get_colors_from_file(FILE_NAME)
    draw_picture(rows, columns)
    screen.exitonclick()


def get_colors_from_file(file):
    global colors
    colors = colorgram.extract(file, 25)


if __name__ == "__main__":
    hirst(PICTURE_ROWS, PICTURE_COLUMNS)
