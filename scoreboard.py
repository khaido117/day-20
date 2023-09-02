from turtle import Turtle

ALIGHMENT = "center"
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(x=0, y=270)
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}, High score: {self.high_score}", align=ALIGHMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score 
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.update_scoreboard()
    
    def get_score(self):
        self.score += 1
        self.update_scoreboard()

