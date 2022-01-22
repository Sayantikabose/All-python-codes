from turtle import Turtle

class Scoreoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore=0
        self.rscore=0  
        self.updatescore()
        
    def updatescore(self): 
        self.clear()
        self.goto(-180,200) 
        self.write(f"{self.lscore}", align="center", font=("Courier", 80, "normal")) 
        self.goto(180,200) 
        self.write(f"{self.rscore}", align="center", font=("Courier", 80, "normal"))

    def lpoint(self):
        self.lscore=self.lscore+1 
        self.updatescore()
    
    def rpoint(self):
        self.rscore=self.rscore+1 
        self.updatescore()