from turtle import Turtle, Screen
import random


def direction(tim,dir,directions):
    tim.right(90*directions[dir])


def random_walk(tim,colors,directions,loop_times):
    for i in range(loop_times):
        tim.color(random.choice(colors))
        direction(tim,random.choice(list(directions.keys())),directions)
        tim.forward(40)

def main():
    colors = ["blue", "black", "red", "green", "pink", "purple"]
    tim = Turtle()
    tim.shape("circle")
    tim.pensize(20)
    tim.speed("fastest")

    directions = {
        "left": 1,
        "right": 2,
        "up": 3,
        "down": 4
    }
    random_walk(tim,colors,directions,1000)
    screen = Screen()
    screen.exitonclick()

if __name__ == "__main__":
    main()