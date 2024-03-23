from turtle import Turtle

class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(position)  # Set initial position
        self.x_move = 10
        self.y_move = 20
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() +self.x_move , self.ycor() + self.y_move)  # Move diagonally
        

    def bounce_y(self):
        self.y_move *= -1
        
    def bounce_x(self):
        self.x_move *= -1  
        self.move_speed *= 0.9 
        
    def reset_position(self):
        self.home() 
        self.move_speed = 0.1
        self.bounce_x()
        

