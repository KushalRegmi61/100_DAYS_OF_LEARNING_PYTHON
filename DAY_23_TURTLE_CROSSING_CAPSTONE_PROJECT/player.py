STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__() 
        self.shape("turtle")
        self.color("blue")   
        self.penup()
        self.seth(90)
        self.go_to_startposition()
        
      
    def move_up(self):
        self.fd(MOVE_DISTANCE)
        
    def restart(self):
        return self.ycor()>FINISH_LINE_Y
            
    def go_to_startposition(self):
        self.goto(STARTING_POSITION)