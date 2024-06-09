from turtle import *
list_of_pos=[(0,0),(-20,0),(-40,0)]
dist=20
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for i in list_of_pos:
            self.add_segment(i)
    def add_segment(self,pos):
        p=Turtle("square")
        p.color("white")
        p.penup()
        p.goto(pos)
        self.segments.append(p)
    def slither(self):
        for i in range(len(self.segments)-1,0,-1):
            self.segments[i].goto(self.segments[i-1].xcor(),self.segments[i-1].ycor())
        self.head.forward(dist)
    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)
    def extend(self):
        self.add_segment(self.segments[-1].position())