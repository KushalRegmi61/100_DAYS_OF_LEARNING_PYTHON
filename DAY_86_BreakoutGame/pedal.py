from turtle import Turtle

class Pedal(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_len=7, stretch_wid= 1)
        self.penup()
        self.goto(position)
    
        # function to move the turtle left  and reight
    def move_left(self):
        new_x = self.xcor()-20
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor()+20
        self.goto(new_x, self.ycor())