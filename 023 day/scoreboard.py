from turtle import Turtle

ALIGNMENT = "center"
ALIGNMENT_SCORE = "left"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.score = 0
        self.hideturtle()
        self.penup()
        self.setposition(x=-280, y=270)
        self.color("Black")
        self.display_score()

    def next_level(self):
        self.level += 1

    def is_last_level(self):
        return self.level > 5

    def increase_score(self, score_to_add):
        self.score += score_to_add

    def game_over(self, win):
        self.setposition(0, 0)
        if win:
            self.write(f"""GAME OVER\nYou WON the game!!!""", align=ALIGNMENT, font=FONT)
        else:
            self.write(f"""GAME OVER\nYou crashed with car :(\nYour score: {self.score}""", align=ALIGNMENT, font=FONT)

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT_SCORE, font=FONT)
