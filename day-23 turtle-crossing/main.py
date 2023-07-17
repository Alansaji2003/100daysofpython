import time
from turtle import Screen
from player import Player
from car_manager import CarManager
import random
from scoreboard import Scoreboard
collision_distance = 20
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
cars = CarManager()
score = Scoreboard()


screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")





game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    cars.create()
    cars.move()
    #detect collision
    for car in cars.CAR_LIST:
        if car.distance(player) < collision_distance:
            game_is_on = False
            score.game_over()

    #detect crossing
    if player.is_at_finish():
        player.go_to_start()
        cars.lvl_up()
        collision_distance += 5
        score.increase_lvl()



screen.exitonclick()