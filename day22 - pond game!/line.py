from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=0.3, stretch_wid=100)