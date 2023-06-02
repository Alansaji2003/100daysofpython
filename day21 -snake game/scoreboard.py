from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-80, 250)
        self.write(f"Score : {self.score}", move=False, align="left", font=("Lilita One", 25, "normal"))

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", move=False, align="left", font=("Lilita One", 25, "normal"))
    def gameover(self):
        self.goto(-70,0)
        self.write("Game Over", move=False, align="left", font=("Lilita One", 25, "normal"))
