from turtle import *
from random import randint
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("dark green")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        randx=randint(-330,330)
        randy=randint(-330,330)
        self.goto(randx,randy)