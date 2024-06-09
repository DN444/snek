from turtle import *
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.goto(0,320)
        self.update()
        self.penup()
        self.hideturtle()
        self.update()
    def update(self):
        self.clear()
        self.write(f"Score: {self.score}",align="center",font=("Courier",24,"normal"))
    def increase_score(self):
        self.score+=1
        self.update()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Courier",24,"normal"))