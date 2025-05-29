from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-230,250)
        self.hideturtle()
        self.count = 0
        self.update_scoreboard()

    def win(self):
        self.count += 1
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"level: {self.count}",align="center",font=("Courier",20,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=("Courier",20,"normal"))