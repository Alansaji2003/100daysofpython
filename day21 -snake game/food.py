from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.penup()
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 250)
        y = random.randint(-280, 250)
        self.goto(x, y)
