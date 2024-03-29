from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.lines = Turtle()
        self.lines.hideturtle()
        self.lines.color('white')
        self.lines.penup()
        self.lines.goto(-300, -230)
        self.lines.pendown()
        self.lines.goto(300, -230)
        self.lines.penup()
        self.lines.goto(-300, 210)
        self.lines.pendown()
        self.lines.goto(300, 210)
        self.lines.penup()

        self.score = Turtle()
        self.score.hideturtle()
        self.score.color('white')
        self.score.penup()

    def show_score(self, level):

        self.score.goto(-240, 250)
        self.score.clear()
        self.score.write(arg=f'Level {level}', align='center', font=("Arial", 18, "normal"))

    def game_over(self):
        self.score.goto(0, 250)
        self.score.write(arg='Game Over', align='center', font=("Arial", 18, "normal"))
