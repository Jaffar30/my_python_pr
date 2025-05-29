from turtle import Screen
import time
from  car import Car
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.listen()
screen.tracer(0)
player = Player()
screen.onkey(player.move,"Up")
scoreboard = Scoreboard()
is_game_on = True

cars = []
for _ in range(3):
    cars.append(Car())

while is_game_on:
    time.sleep(0.1)
    screen.update()

    for car in cars:
        car.move()
        if car.xcor() <= -250:
            car.reposition()
    # check collition with car
        if player.distance(car) < 30:
            is_game_on = False
            player.lost()
            scoreboard.game_over()

    if player.ycor() >= 250:
        scoreboard.win()
        scoreboard.update_scoreboard()
        player.reposition()
        # add more cars:
        for _ in range(5):
            cars.append(Car())
        

screen.exitonclick()