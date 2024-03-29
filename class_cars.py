from class_turtle import Tuga
from turtle import Turtle
import random

COLORS = ['red', 'white', 'blue', 'orange', 'grey', 'pink', 'purple', 'yellow']


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.create_car()
        self.cars = []

    def car_advance(self):
        self.forward(20)

    def create_car(self):
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(COLORS[random.randint(0, len(COLORS)-1)])
        self.goto(330, random.randrange(-200, 200, 50))
        self.setheading(180)

    def automatic_creation(self):
        creation = random.randint(0, 3)
        if creation == 3:
            new_car = Car()
            self.cars.append(new_car)

        for item in self.cars:
            if item.xcor() > -320:
                item.car_advance()
            else:
                self.cars.remove(item)

    def collision(self, tuga):
        for item in self.cars:
            if item.distance(tuga) < 20:
                return True




