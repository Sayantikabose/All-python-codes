from turtle import Turtle

class Ball(Turtle):
    def __init__(self): 
        super().__init__() 
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.penup()
        self.xmove=10
        self.ymove=10 
        self.movespeed=0.1
    
    def move(self):
        newx=self.xcor()+self.xmove
        newy=self.ycor()+self.ymove
        self.goto(newx,newy)
    
    def bounce(self):
        self.ymove *= -1
       
        
    def bouncy(self):
        self.xmove *=-1 
        
    
    def restart(self):
        self.goto(0,0)  
        
        self.bouncy()