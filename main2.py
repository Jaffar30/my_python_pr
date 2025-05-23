from turtle import Turtle, Screen,colormode
import random

def random_color():
    color = random.randint(0, 255)
    return color

def direction(tim,dir,directions):
    tim.right(90*directions[dir])


def random_walk(tim,directions,loop_times):
    for _ in range(loop_times):
        
        r = random_color()
        g = random_color()
        b = random_color()
        tim.color((r,g,b))
        direction(tim,random.choice(list(directions.keys())),directions)
        tim.forward(40)

def main():
    tim = Turtle()
    tim.shape("circle")
    colormode(255) 
    tim.pensize(20)
    tim.speed("fastest")

    directions = {
        "left": 1,
        "right": 2,
        "up": 3,
        "down": 4
    }
    random_walk(tim,directions,10)
    screen = Screen()
    screen.exitonclick()

if __name__ == "__main__":
    main()