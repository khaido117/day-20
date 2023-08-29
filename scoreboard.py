from turtle import Turtle

ALIGHMENT = "center"
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(x=0, y=270)
        self.score = 0
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()
        
    def update_scoreboard(self):
        self.write(f"Score = {self.score}", align=ALIGHMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGHMENT, font=FONT)
    
    def get_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

