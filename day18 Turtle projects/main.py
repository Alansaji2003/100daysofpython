# from turtle import Turtle, Screen
# import random
#
# pen = Turtle()
# pen.pensize(7)
# screen = Screen()
#
# r = random.randint(0, 255)
# g = random.randint(0, 255)
# b = random.randint(0, 255)
# screen.colormode(255)
# while 2 < 5:
#     pen.speed(20)
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     pen.color(r, g, b)
#     pen.forward(20)
#     directions = [90, 180, 270, 0]
#     pen.right(random.choice(directions))
#
#
# screen.exitonclick()
# from turtle import Turtle, Screen
# import random
#
# pen = Turtle()
#
# screen = Screen()
#
#
# screen.colormode(255)
# pen.speed(20)
# i = 0
# while i < 200:
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     pen.color(r, g, b)
#     pen.circle(100)
#     pen.left(2)
#     i += 1
#
#
# screen.exitonclick()

import colorgram
from turtle import Turtle, Screen
import random

pen = Turtle()

screen = Screen()
screen.colormode(255)
# rgb = []
# colors = colorgram.extract('ref.jpg', 10)
# for i in range(10):
#     rgb.append(colors[i].rgb)
#
# for i in range(2):
#     rgb.pop(0)

RGB = [(232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227,5), (229, 159, 46), (27, 40, 157)]

pen.penup()
pen.hideturtle()
pen.speed(20)
pen.setheading(225)
pen.forward(300)
pen.setheading(0)
number_of_dots = 100

for i in range(1, number_of_dots + 1):
    pen.dot(20, random.choice(RGB))
    pen.forward(50)

    if i % 10 == 0:
        pen.setheading(90)
        pen.forward(50)
        pen.setheading(180)
        pen.forward(500)
        pen.setheading(0)



screen.exitonclick()
