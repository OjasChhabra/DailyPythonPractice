from food import Food
from snake import Snake
from scoreboard import Scoreboard
from turtle import Screen
from time import sleep

screen = Screen()
screen.title("Snake Game")
screen.setup(800, 800)
screen.bgcolor("black")
screen.tracer(0)
screen.colormode(255)

food = Food()
snake = Snake()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")

game_on = True
while game_on:
    screen.update()
    sleep(0.1)
    snake.move_head()
    if food.distance(snake.head) < 20:
        food.move()
        scoreboard.update()
        snake.extend()
    if snake.head.xcor() < -390 or snake.head.xcor() > 390 or snake.head.ycor() < -390 or snake.head.ycor() > 390:
        scoreboard.game_over()
        game_on = False
    for i in snake.body:
        if i != snake.head and i != snake.body[1]:
            if snake.head.distance(i) < 20:
                screen.update()
                scoreboard.game_over()
                game_on = False

screen.exitonclick()