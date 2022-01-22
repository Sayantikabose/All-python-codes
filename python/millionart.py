import random
import turtle
a = turtle.Turtle()      #instantiate a new turtle object called 'a' 
a.shape("turtle")
a.penup()                #don't draw when turtle moves
a.goto(-250, -250)       #move the turtle to a location
a.showturtle()           #make the turtle visible
screen=turtle.Screen()
screen.colormode(255) 
for j in range (1, 20):
    for i in range(-250,-235):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        rgb = [r,g,b]
        a.pencolor(rgb) 
        a.pendown()
        a.dot(10)
        a.penup()
        a.forward(50)
    a.goto(-250, (-250+(j*20)))
    

screen.exitonclick()