from turtle import Turtle


class Slab(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.color("Yellow")
        self.shape(name="square")
        self.color("Yellow")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.setposition(pos)
        self.slab_speed = 40


    def go_up(self):

        new_y = self.ycor() + self.slab_speed
        self.goto(self.xcor(), new_y)

    def go_down(self):

        new_y = self.ycor() - self.slab_speed
        self.goto(self.xcor(), new_y)
