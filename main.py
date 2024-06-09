from turtle import *
import time
from snek import Snake
from food import Food
from score import Scoreboard
screen=Screen()
screen.setup(700,700)
screen.bgcolor("blue")
screen.title("Play with the snake!")
screen.tracer(0)
snek=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snek.up,"Up")
screen.onkey(snek.down,"Down")
screen.onkey(snek.left,"Left")
screen.onkey(snek.right,"Right")
game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snek.slither()
    if snek.head.distance(food)<20:
        food.refresh()
        snek.extend()
        scoreboard.increase_score()
    if snek.head.xcor()>340 or snek.head.xcor()<-340 or snek.head.ycor()>340 or snek.head.ycor()<-340:
        game_on=False
        scoreboard.game_over()
    for segment in snek.segments[1:]:
        if snek.head.distance(segment)<10:
            game_on=False
            scoreboard.game_over()
screen.exitonclick()