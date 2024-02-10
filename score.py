from turtle import Turtle

ALIGNMENT = "center"
MOVE = False
FONT = ("Times New Roman", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open('data.txt', mode='r') as file:
            self.high_score = int(file.read())
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.high_score):
            with open('data.txt', mode='w') as f:
                f.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

