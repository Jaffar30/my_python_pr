from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

red_snake = Snake("red")
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(red_snake.up,"Up")
screen.onkey(red_snake.down,"Down")
screen.onkey(red_snake.left,"Left")
screen.onkey(red_snake.right,"Right")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    red_snake.move()

    #detect collision with food
    if red_snake.segments[0].distance(food) < 15:
        food.refresh()
        red_snake.extend()
        scoreboard.increase_score()
        

    # detect collision with wall
    if red_snake.segments[0].xcor() > 280 or red_snake.segments[0].xcor() <-280 or red_snake.segments[0].ycor() > 280 or red_snake.segments[0].ycor() <-280:
       scoreboard.reset()
       red_snake.reset()

    for segment in red_snake.segments[1:]:
        if red_snake.segments[0].distance(segment) < 10:
           scoreboard.reset()
           red_snake.reset()
            
    


screen.exitonclick()