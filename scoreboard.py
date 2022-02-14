from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 16, "normal")
COLOR = "white"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.points = 0

        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.color(COLOR)
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.points} Highest Score: {self.high_score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.points += 1
        self.update_scoreboard()

    def reset(self):
        if self.points > self.high_score:
            self.high_score = self.points

            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.points = 0
        self.update_scoreboard()
