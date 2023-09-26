from turtle import Turtle

# Snake setup parameters
SNAKE_SEGMENT_PIXELS = 20
SNAKE_STARTING_SEGMENTS = 3
SNAKE_START_X = 0
SNAKE_START_Y = 0
SNAKE_COLOR = "white"
SNAKE_SPEED = 20

# Movement angles
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self,
                 segments=SNAKE_STARTING_SEGMENTS,
                 color=SNAKE_COLOR,
                 size=SNAKE_SEGMENT_PIXELS,
                 start_x=SNAKE_START_X,
                 start_y=SNAKE_START_Y):
        snake: list[Turtle] = []
        for i in range(segments):
            t = Turtle(shape="square")
            t.color(color)
            t.penup()
            t.setposition(x=start_x - size * i, y=start_y)
            snake.append(t)

        self.snake = snake
        self.head = self.snake[0]

    def move(self, speed=SNAKE_SPEED):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].setpos(self.snake[i - 1].pos())
        self.head.forward(speed)

    def grow_tail(self, color=SNAKE_COLOR):
        t = Turtle(shape="square")
        t.color(color)
        t.penup()
        t.setposition(self.snake[-1].pos())
        self.snake.append(t)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def is_hitting_wall(self, screen_width, screen_height):
        return (self.head.xcor() > screen_width / 2 - SNAKE_SEGMENT_PIXELS or
                self.head.xcor() < -screen_width / 2 + SNAKE_SEGMENT_PIXELS or
                self.head.ycor() > screen_height / 2 - SNAKE_SEGMENT_PIXELS or
                self.head.ycor() < -screen_height / 2 + SNAKE_SEGMENT_PIXELS)

    def is_hitting_tail(self):
        for segment in self.snake[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False
