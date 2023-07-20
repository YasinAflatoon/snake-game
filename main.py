from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
import time


sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.title("Snake Game.")
sc.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.right, "Right")
sc.onkey(snake.left, "Left")

game_on = True
while game_on:
    sc.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 18:
        snake.extend()
        food.place()
        score_board.update_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score_board.game_over()
        sc.update()
        time.sleep(1)
        score_board.over.clear()
        snake.reset()

    for seg in snake.segments[3:]:
        if snake.head.distance(seg) < 15:
            score_board.game_over()
            sc.update()
            time.sleep(1)
            score_board.over.clear()
            snake.reset()

sc.exitonclick()
