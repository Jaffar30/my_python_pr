import random
from color import get_colors
from colorgram import extract
from init_turtle import init_turtle, show_screen
image_colors = extract('color_project/image.jpg', 30)
colors = get_colors(image_colors)
tim = init_turtle(colors[-1])

def main():
    starting_x = -600 # -600    0    600
    starting_y = -400
    for i in range(starting_y,1200,100):
        for j in range(starting_x,1200,100):
            tim.color(random.choice(colors))
            tim.teleport(starting_x+j,starting_y+i)
            tim.dot(20,random.choice(colors))
    

if __name__ == "__main__":
    main()

