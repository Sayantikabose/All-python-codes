from turtle import Turtle, Screen
import random

screen= Screen()
screen.setup(500,500) 
is_race_on=False

user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win Enter the color")

if user_bet:
    is_race_on=True

timmy1=Turtle()
timmy2=Turtle()
timmy3=Turtle()
timmy4=Turtle()
timmy5=Turtle()

all_turtle = [timmy5,timmy4,timmy3,timmy2,timmy1]

timmy1.penup()
timmy2.penup()
timmy3.penup()
timmy4.penup()
timmy5.penup() 

timmy1.shape("turtle")
timmy2.shape("turtle")
timmy3.shape("turtle")
timmy4.shape("turtle")
timmy5.shape("turtle")


timmy1.color("blue")
timmy2.color("green")
timmy3.color("violet")
timmy4.color("orange")
timmy5.color("red")

timmy1.goto(-230,0)
timmy2.goto(-230,50)
timmy3.goto(-230,100)
timmy4.goto(-230,-50)
timmy5.goto(-230,-100)

while(is_race_on==True):
    for turtles in all_turtle: 
        if (turtles.xcor()>230): 
            is_race_on=False
            winning_color=turtles.pencolor()
            if(winning_color==user_bet):
                print(f"You won, the winning turtle is {winning_color}")
            else:
                print(f"You lose, the winning turtle is {winning_color}")
        rand_dis=random.randint(1,10)
        turtles.forward(rand_dis)
    

screen.exitonclick()
