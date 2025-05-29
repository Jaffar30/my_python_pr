from turtle import Turtle
import random

class Car(Turtle):
    colors = ["red","yellow","blue","orange","purple","pink","green"]
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(Car.colors))
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.penup()
        self.goto(random.randint(-250,250),random.randint(-250,250))

    def move(self):
        self.forward(-20)

    def reposition(self):
        self.goto(250,self.ycor())