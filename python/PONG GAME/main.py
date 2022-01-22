from turtle import Turtle, Screen
from padii import Padle 
from ball import Ball  
from scoreboard import Scoreoard
import time
screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("PONG PONG GAME")
screen.tracer(0)

tim=Turtle() 

rpadle=Padle(380,0)
lpadle=Padle(-380,0)

ball=Ball() 
scoreboard= Scoreoard()
screen.listen()
screen.onkey(rpadle.up,"Up")
screen.onkey(rpadle.down,"Down")
screen.onkey(lpadle.up,"w")
screen.onkey(lpadle.down,"s")


game_is_on=True
while game_is_on: 
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()
    if ball.ycor()>290 or ball.ycor()<-290 :
        ball.bounce()
    if (ball.distance(rpadle)<50 and ball.xcor() > 360) or (ball.distance(lpadle)<50 and ball.xcor() > -360) :
        ball.bouncy() 

    if ball.xcor()>390 :
       ball.restart()
       scoreboard.lpoint()
    
    if ball.xcor()<-390 :
        ball.restart() 
        scoreboard.rpoint()
screen.exitonclick()