from turtle import Turtle


class Tuga(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.setheading(90)
        self.goto(0, -280)

    def move(self):
        self.forward(20)

    def next_level(self):
        if self.ycor() > 210:
            self.goto(0, -280)
            return True

