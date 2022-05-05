from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=2)
        self.color(choice(COLORS))
        self.setheading(180)
        y = randint(-280, 280)
        self.goto(320, y)

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)


