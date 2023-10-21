from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
SAVE_FILE = "high_score"


class Scoreboard(Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.read_high_score()
        self.hideturtle()
        self.penup()
        self.setposition(x=-20, y=screen_height / 2 - 30)
        self.color("white")
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset_score(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.display_score()

    def save_high_score(self):
        with open(SAVE_FILE, mode="w") as file:
            file.write(str(self.high_score))

    def read_high_score(self):
        try:
            with open(SAVE_FILE, mode="r") as file:
                content = file.read()
                self.high_score = int(content)
        except FileNotFoundError:
            self.create_high_score_file()

    def create_high_score_file(self):
        with open(SAVE_FILE, mode="w") as file:
            content = 0
            file.write(str(content))
            self.high_score = int(content)
