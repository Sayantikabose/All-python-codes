from turtle import Turtle

class Padle(Turtle):
    def __init__(self,x,y): 
        super().__init__()
       
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(x,y) 
    
    def up(self):
        new_y=self.ycor()+40
        self.goto(self.xcor(),new_y)
    
    def down(self):
        new_y=self.ycor()-40
        self.goto(self.xcor(),new_y)
    

