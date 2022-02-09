from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 12, "normal")
FONT1 = ("Courier", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        with open("../../Desktop/data.txt") as data:
            self.high_score = int(data.read())

        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score} ", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("../../Desktop/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    def inc_score(self):
        self.score += 1
        self.update_scoreboard()
