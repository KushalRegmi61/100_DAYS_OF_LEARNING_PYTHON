from turtle import Turtle
turt = Turtle(shape="square")
STARTING_POSITIONS = [(0, 0),(-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
class Snake():
    def  __init__(self): 
        self.segment = []
        self.create_snake()
        
    def create_snake(self):        
        for j in STARTING_POSITIONS:
            turtle = Turtle(shape="square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(j)
            self.segment.append(turtle)
    
    #FUCNTION THAT UPDATES ALL THE CORDINATES OF THE SQUARES
    def move(self):
        for i in range(len(self.segment)-1, 0, -1):
            new_x = self.segment[i-1].xcor()
            new_y = self.segment[i-1].ycor()
            self.segment[i].goto(new_x,new_y)
        self.segment[0].forward(MOVING_DISTANCE)
        
 #TODO FUNTION TO CONTROL MOVEMENTS OF THE SNAKES                  
    def up(self):
        
        self.segment[0].seth(90)
        self.segment[0].forward(MOVING_DISTANCE)  
    
    def down(self):
        
        self.segment[0].seth(270)
        self.segment[0].forward(MOVING_DISTANCE)  
        
    def right(self):
         
        self.segment[0].seth(0)
        self.segment[0].forward(MOVING_DISTANCE)     
        
    def left(self):
        
        self.segment[0].seth(180)
        self.segment[0].forward(MOVING_DISTANCE)       
        
        
               