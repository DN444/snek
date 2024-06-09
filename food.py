from turtle import *
from random import randint
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        randx=randint(-330,330)
        randy=randint(-330,330)
        self.goto(randx,randy)