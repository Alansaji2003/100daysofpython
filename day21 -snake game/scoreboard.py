from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        with open("score.txt", mode="r") as self.file:

            self.highscore = self.file.read()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-150, 250)
        self.update_scoreboard()

    def increase(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}    High Score: {self.highscore}", move=False, align="left", font=("Lilita One", 25, "normal"))

    def reset(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            with open("score.txt", mode="w") as self.file:
                self.file.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()



