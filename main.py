from turtle import Screen
from class_turtle import Tuga
from class_cars import Car
from class_scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

level = 1
timer = 0.1

tuga = Tuga()
cars = []
car = Car()

scoreboard = Scoreboard()

game_status = True
while game_status:

    scoreboard.show_score(level)
    screen.listen()
    screen.onkey(key='w', fun=tuga.move)
    car.automatic_creation()

    if tuga.next_level():
        print('Next level')
        level += 1
        timer *= 0.5

    if car.collision(tuga):
        print('EEEE AQUIIII')
        scoreboard.game_over()
        game_status = False

    time.sleep(timer)
    screen.update()


screen.exitonclick()
