from turtle import Turtle, Screen, colormode
def init_turtle(color):
    colormode(255)  
    tim = Turtle()
    tim.shape("circle")
    tim.color(color) 
    tim.pensize(20)
    return tim

def show_screen():
    screen = Screen()
    screen.exitonclick()