from turtle import Turtle
turt = Turtle(shape="square")
STARTING_POSITIONS = [(0, 0),(-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
up = 90
down = 270
right = 0
left= 180
class Snake():
    def  __init__(self): 
        
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        
    def create_snake(self):        
        for j in STARTING_POSITIONS:
            self.new_segments(j)
            
    #appending new position
    def new_segments(self, postion):
            turtle = Turtle(shape="square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(postion)
            self.segment.append(turtle)
    
    # extend list
    def extend(self):
        self.new_segments(self.segment[-1].position())
         
    
    #FUCNTION THAT UPDATES ALL THE CORDINATES OF THE SQUARES
    def move(self):
        for i in range(len(self.segment)-1, 0, -1):
            new_x = self.segment[i-1].xcor()
            new_y = self.segment[i-1].ycor()
            self.segment[i].goto(new_x,new_y)
        self.head.forward(MOVING_DISTANCE)
        
 #TODO FUNTION TO CONTROL MOVEMENTS OF THE SNAKES                  
    def up(self):
        if self.head.heading()!= down:
            self.head.seth(up)
             
    def down(self):
        if self.head.heading() != up:
            self.head.seth(down)
          
        
    def right(self):
        if self.head.heading() != left: 
            self.head.seth(right)
             
        
    def left(self):
        if self.head.heading() != right:
            self.head.seth(left)
            
        
        
               