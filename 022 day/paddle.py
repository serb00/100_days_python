from turtle import Turtle

# Snake setup parameters
SNAKE_SEGMENT_PIXELS = 20
COLOR = "white"


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.vert_speed = ""
        self.shape("square")
        self.color(COLOR)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setposition(position)

    def up(self):
        if self.ycor() < 240:
            self.goto(x=self.xcor(), y=self.ycor() + 20)
            self.vert_speed = "up"

    def down(self):
        if self.ycor() > -230:
            self.goto(x=self.xcor(), y=self.ycor() - 20)
            self.vert_speed = "down"
