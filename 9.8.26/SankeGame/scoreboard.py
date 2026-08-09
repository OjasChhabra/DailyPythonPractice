from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update()

    def update(self):
        self.clear()
        self.goto(-380,340)
        self.score += 1
        self.write(f"Score: {self.score}", "False", "left", ("Arial", 28, "bold"))

    def game_over(self):
        self.goto(0,-14)
        self.write("Game Over", "False", "center", ("Arial", 28, "bold"))
