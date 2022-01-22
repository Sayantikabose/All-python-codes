from turtle import Turtle
starting_pos=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake: 

    def __init__(self):
        self.segments=[]
        self.create_Snake()
         

    def create_Snake(self):
       for pos in starting_pos:
           self.add_snake(pos)
            
    
    def add_snake(self,position):
        new_tim=Turtle("square")
        new_tim.color("white") 
        new_tim.penup()
        new_tim.goto(position)
        self.segments.append(new_tim) 

    def extend(self):
        self.add_snake(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
    
        self.segments[0].forward(20)
    
    def up(self):
        if self.segments[0].heading()!= DOWN:
            self.segments[0].setheading(90)  

    def down(self):
        if self.segments[0].heading()!=UP:
            self.segments[0].setheading(270) 

    def left(self):
        if self.segments[0].heading()!=RIGHT:
            self.segments[0].setheading(180)
    def right(self):
        if self.segments[0].heading()!=LEFT:
            self.segments[0].setheading(360)
    
    def reset(self): 
        for seg in self.segments:
            seg.goto(9000,9000)
        self.segments.clear()
        self.create_Snake()