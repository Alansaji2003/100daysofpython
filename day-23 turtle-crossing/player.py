from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def up(self):
        new_position = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_position)
    def down(self):
        new_position = self.ycor() - MOVE_DISTANCE
        self.goto(0, new_position)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish(self):
        if self.ycor()> FINISH_LINE_Y:
            return True
        else:
            return False

