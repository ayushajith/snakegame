from turtle import Turtle
import random


class Food(Turtle):  # Food class has inherited the appearance and the behaviour from the Turtle class

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 280)
        self.goto(x=x_cor, y=y_cor)
