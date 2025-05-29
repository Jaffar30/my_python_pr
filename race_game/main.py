from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bat = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
is_race_finished = False
winner = "None"


def set_turtle(color,x,y):
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=x,y=y)
    return turtle

colors = ["red", "blue", "yellow", "green", "purple", "orange"]
turtles = []
for i, color in enumerate(colors):
    turtles.append({"turtle": set_turtle(color, x=-230, y=150 - i * 30), "x_position": -230})

while not is_race_finished :
    for turtle_dict in turtles:
        random_step = random.randint(0,10)
        turtle_dict["turtle"].forward(random_step)
        turtle_dict["x_position"] += random_step
        if turtle_dict["x_position"] >= 230:
            winner = turtle_dict["turtle"].pencolor()
            is_race_finished = True


screen.textinput(title="Race winner",prompt=f"You Win the bet {winner} turtle finish the race first" if winner == user_bat else f" You lose The, winner is {winner}.\nYour bet was {user_bat}.")

screen.exitonclick()
