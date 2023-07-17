from turtle import Turtle
import random



COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):

        self.car_speed = STARTING_MOVE_DISTANCE
        self.CAR_LIST = []

    def create(self):
        random_num = random.randint(1,6)
        if random_num == 6:

            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)

            new_car.penup()
            new_car.color(random.choice(COLORS))

            random_y = random.randint(-250,250)
            new_car.goto(300, random_y)
            self.CAR_LIST.append(new_car)


    def move(self):
        for car in self.CAR_LIST:
            car.backward(self.car_speed)

    def lvl_up(self):
        self.car_speed += MOVE_INCREMENT

