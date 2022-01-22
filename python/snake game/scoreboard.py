from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as file:
            self.hscore=int(file.read()) 
        
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score:{self.score} HighScore :{self.hscore}",move=False,align="center",font=(("Verdana",15,"normal"))) 
        
        self.hideturtle()
        
    def increase(self):
        self.score=self.score+1
        self.clear()
        self.write(f"Score:{self.score} HighScore :{self.hscore} ",move=False,align="center",font=(("Verdana",15,"normal")))
    
    
    def reset(self):
        if self.score > self.hscore : 
            self.hscore=self.score 
            with open("data.txt", mode="w") as f:
                f.write(f"{self.hscore}")
        self.score=0
        self.clear()
        self.write(f"Score:{self.score} HighScore :{self.hscore}",move=False,align="center",font=(("Verdana",15,"normal")))
    
