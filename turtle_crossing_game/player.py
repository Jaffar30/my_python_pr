from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.reposition()
        self.move_distance = 20

    def move(self):
        self.forward(self.move_distance)

    def lost(self):
        self.move_distance = 0

    def reposition(self):
        self.goto(0,-280)