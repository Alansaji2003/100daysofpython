from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_AMOUNT = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.createsnake()

    def createsnake(self):
        for position in POSITIONS:
            self.addsegment(position)

    def addsegment(self, position):
        new_segment = Turtle("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    def extend(self):
        self.addsegment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_corX = self.segments[seg_num - 1].xcor()
            new_corY = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_corX, new_corY)
        self.segments[0].forward(MOVE_AMOUNT)


    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

