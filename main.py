import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Harry's Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()
harry_snake = Snake()
food = Food()
screen.listen()
screen.onkey(harry_snake.go_up, 'Up')
screen.onkey(harry_snake.turn_left, 'Left')
screen.onkey(harry_snake.turn_right, 'Right')
screen.onkey(harry_snake.go_down, 'Down')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    harry_snake.snake_move()

    #detect snake distance to food
    if harry_snake.head.distance(food) < 15:
        print("nom, nom, nom")
        food.regenerate()
        scoreboard.increase_score()
        harry_snake.grow_snake()

    #detect collision with wall
    if harry_snake.head.xcor() > 280 or harry_snake.head.xcor() < -300 or harry_snake.head.ycor() > 300 or harry_snake.head.ycor() < -280:
        scoreboard.reset()
        harry_snake.reset()


    #detect collision with tail
    for segment in harry_snake.snake_segments[1:]:
        if harry_snake.head.distance(segment) < 10:
            scoreboard.reset()
            harry_snake.reset()

screen.exitonclick()
