from turtle import Turtle
class Pedal(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_len=1, stretch_wid= 5)
        self.penup()
        self.goto(position)
    
        # function to move the turtle up and down
    def move_up(self):
        new_y = self.ycor()+ 20
        self.goto(self.xcor(), new_y)
    def move_down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(), new_y) 