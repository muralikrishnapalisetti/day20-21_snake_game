from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def start_game():
    screen.clear()
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
            scoreboard.game_over()
            game_is_on = False

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                game_is_on = False

    screen.onkey(start_game, "r")


# Main screen setup
screen = Screen()
screen.setup(width=600, height=600)
start_game()
screen.mainloop()
