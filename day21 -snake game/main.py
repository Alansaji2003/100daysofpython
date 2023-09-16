from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Python snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update() #we stop updating the snake on screen, above at tracer(0) we restart it here and give it a bit more time before next execution
    time.sleep(0.15)
    snake.move()


    #COLLISION DETECTION WITH FOOD
    if snake.segments[0].distance(food) < 15:         #using the distance method of turtle class to find the distance between head and food object
        food.refresh()
        score.increase()
        snake.extend()
    #collision with wall
    if snake.segments[0].xcor() < -280 or  snake.segments[0].xcor() > 280 or  snake.segments[0].ycor() < -280 or  snake.segments[0].ycor() > 280:
        score.reset()
        snake.reset()

    #collision with tail
    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
