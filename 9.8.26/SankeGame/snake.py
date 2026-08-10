from turtle import Turtle,Screen
from random import randint
class Snake():

    def __init__(self):
        screen = Screen()
        screen.colormode(255)
        self.body = []
        self.x_cor = 0
        self.create_body()
        self.head = self.body[0]

    def create_body(self):
        for i in range(3):
            body = Turtle()
            body.color("white",self.random_color())
            body.penup()
            body.speed(0)
            body.shape("circle")
            self.body.append(body)
            body.goto(self.x_cor, 0)
            self.x_cor -= 20

    def move_body(self):
        for i in range(len(self.body)-1,0,-1):
            xcor = self.body[i-1].xcor()
            ycor = self.body[i-1].ycor()
            self.body[i].goto(xcor,ycor)

    def move_head(self):
        self.move_body()
        self.head.fd(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)

    def extend(self):
        body = Turtle()
        body.color("white",self.random_color())
        body.penup()
        body.speed(0)
        body.shape("circle")
        xcor = self.body[-1].xcor()
        ycor = self.body[-1].ycor()
        self.body.append(body)
        self.body[-1].goto(xcor,ycor)

    def random_color(self):
            r = randint(1,255)
            g = randint(1,255)
            b = randint(1,255)
            return r,g,b
