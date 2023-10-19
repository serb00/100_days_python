from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.set_starting_position()
        self.setheading(90)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        print(new_y)
        self.goto(x=0, y=new_y)

    def is_finished(self):
        return self.ycor() >= FINISH_LINE_Y

    def set_starting_position(self):
        self.goto(STARTING_POSITION)
