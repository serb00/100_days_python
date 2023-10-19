from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.hideturtle()
        self.penup()
        self.setposition(x=-20, y=screen_height / 2 - 30)
        self.color("white")
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Player 1 score: {self.p1_score} | Player 2 score: {self.p2_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self, player):
        if player == "p1":
            self.p1_score += 1
        else:
            self.p2_score += 1
        self.display_score()

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"""GAME OVER\nPlayer {self.get_winner()} won!""", align=ALIGNMENT, font=FONT)

    def get_winner(self):
        if self.p1_score > 2:
            return "1"
        elif self.p2_score > 2:
            return "2"
        else:
            return "none"

