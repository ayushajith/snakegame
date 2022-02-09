from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # Detect collision with the food item
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.inc_score()
        food.refresh()

    # detect collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()

    # detect collision with the tail
    for segment in snake.segments[1:]:        # Sliced the segments list in such a way that we only search from the
        if snake.head.distance(segment) < 15:    # second item to the last one !!
            score.reset()
            snake.reset()

screen.exitonclick()
