from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.goto(x=-200, y=260)
        self.hideturtle()
        self.speed("fastest")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.score} ", False, align="center", font=FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write("GAME OVER!", False, align="center", font=FONT)


