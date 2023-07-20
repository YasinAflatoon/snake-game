from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.color("blue")
        self.speed(0)
        self.place()

    def place(self):
        x_pos = random.randint(-280, 280)
        y_pos = random.randint(-280, 280)
        if -20 < x_pos < 20 and 260 < y_pos < 280:
            self.place()
        else:
            self.goto(x_pos, y_pos)
