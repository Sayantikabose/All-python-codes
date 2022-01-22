from turtle import Turtle, Screen

timmy=Turtle()  
screen= Screen() 
def moveForward():
    timmy.forward(50)

def moveBack():
    timmy.backward(50)

def turnleft():
    newheading = timmy.heading()+10
    timmy.setheading(newheading) 
def turnright():
    newheading = timmy.heading()-10
    timmy.setheading(newheading)

screen.listen()
screen.onkey(moveForward,"q")
screen.onkey(moveBack,"w")
screen.onkey(turnleft,"e")
screen.onkey(turnright,"r") 


screen.exitonclick()
