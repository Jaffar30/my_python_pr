from turtle import Turtle 

class scoreboard(Turtle):

    def __init__(self,snakes_number):
        super().__init__()
        self.scoreboards = []
        for snake in snakes_number:
            self.scoreboards.append(self.create_score_board())

    def create_score_board(self):
        pass