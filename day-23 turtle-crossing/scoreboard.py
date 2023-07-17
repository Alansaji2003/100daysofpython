from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.write(f"LEVEL: {self.level} ", align="left", font=FONT )

    def update(self):
        self.clear()
        self.write(f"LEVEL: {self.level} ", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"LEVEL: {self.level} GAME OVER ", align="CENTER", font=FONT)

    def increase_lvl(self):
        self.level += 1
        self.update()
