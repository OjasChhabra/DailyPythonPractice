from turtle import Turtle, Screen
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.screen.colormode(255)
        self.shape("circle")
        self.color(self.random_color())
        self.penup()
        self.move()

    def move(self):
        self.color(self.random_color())
        x_cor = randint(-280, 280)
        y_cor = randint(-280, 280)
        self.goto(x_cor, y_cor)

    def random_color(self):
        r = randint(1,255)
        g = randint(1,255)
        b = randint(1,255)
        return r,g,b