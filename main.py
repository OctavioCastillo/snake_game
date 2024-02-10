# TODO: 1. Create snake body
# TODO: 2. Move snake
# TODO: 3. Control snake
# TODO: 4. Detect collision with food
# TODO: 5. Create a scoreboard
# TODO: 6. Detect collision with wall
# TODO: 7. Detect collision with tail

from turtle import Screen
from snake import Snake, Board
from food import Food
from score import Scoreboard
import time

screen = Screen()
screen.title("Snake game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
board = Board()

screen.listen()
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.right, key="d")

board.create()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.ycor() > 265 or snake.head.xcor() < -300 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    # if head collides with any segment in the tail
        # trigger game_over
    # slice the list with list[::]
        # the first parameter is going from the coma you want to the next one you write in the
        # after the first :, then the last parameter is the steps
    for part in snake.body[1::]:
        # the sliced list get us everything besides the head, so it doesn't collide at the beginning

        if snake.head.distance(part) < 10:
            scoreboard.update_scoreboard()
            snake.reset()
screen.exitonclick()
