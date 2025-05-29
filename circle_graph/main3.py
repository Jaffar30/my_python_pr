from turtle import Turtle, Screen, colormode
import random

def random_color():
    color = random.randint(0, 255)
    return color

def draw_circle(tim, radius,forward):
    tim.color((random_color(), random_color(),random_color()))
    tim.circle(radius)
    tim.penup()
    tim.right(forward)
    # tim.forward(forward)
    tim.pendown()

def draw_circle_graph(tim,forward,radius):
    loop_times = 360 // forward
    for _ in range(loop_times):
        draw_circle(tim, radius,forward)

def main():
    print("Main Function Trigger")
    tim = Turtle()
    tim.speed("fastest")
    colormode(255)
    draw_circle_graph(tim,2,100)
    screen = Screen()
    screen.exitonclick()

if __name__ == "__main__":
    main()