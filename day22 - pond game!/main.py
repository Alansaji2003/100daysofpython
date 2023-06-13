from turtle import Screen
from slab import Slab
from ball import Ball
import time
from score import Score
from line import Line

game_speed = 0.04


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("dark green")
screen.title("Alan's Pong")

screen.tracer(0)

r_slab = Slab((350, 0))
l_slab = Slab((-350, 0))
new_ball = Ball()
score = Score()
line = Line()


screen.listen()
screen.onkey(r_slab.go_up, "Up")
screen.onkey(r_slab.go_down, "Down")
screen.onkey(l_slab.go_up, "w")
screen.onkey(l_slab.go_down, "s")
game_on = True
while game_on:
    time.sleep(game_speed)
    screen.update()
    new_ball.move()
    # collision detection with walls
    if new_ball.ycor() > 280 or new_ball.ycor() < -280:
        new_ball.wall_bounce()

    # collision detection with slab
    if new_ball.distance(r_slab) < 80 and new_ball.xcor() > 320 or new_ball.distance(l_slab) < 80 and new_ball.xcor() < -320:
        new_ball.slab_bounce()
        if (game_speed > 0.01):
            game_speed *= 0.9
        if(r_slab.slab_speed < 80 and l_slab.slab_speed < 80):
            r_slab.slab_speed += 1
            l_slab.slab_speed += 1
    # miss detection
    if new_ball.xcor() > 380:
        new_ball.reset()
        score.l_point()
        game_speed = 0.04

    if new_ball.xcor() < -380:
        new_ball.reset()
        score.r_point()
        game_speed = 0.04

screen.exitonclick()
