import colorgram
from turtle import Turtle, Screen, colormode

image_colors = colorgram.extract('color_project/image.jpg', 10)

def get_colors(image_colors):
    colors = []
    for color in image_colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        colors.append((r, g, b))
    return colors

colors = get_colors(image_colors)

colormode(255)  
tim = Turtle()

tim.shape("circle")
tim.color(colors[-1]) 
tim.pensize(20)

tim.pendown()
tim.goto(100,0)
tim.penup()
tim.forward(1)
tim.penup()
tim.forward(100)

tim.pendown()
tim.forward(1)

screen = Screen()
screen.exitonclick()
