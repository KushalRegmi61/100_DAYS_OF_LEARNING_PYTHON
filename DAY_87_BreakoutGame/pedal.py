from turtle import Turtle

class Pedal(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_len=7, stretch_wid=1)
        self.penup()
        self.goto(position)

    def move_left(self):
        new_x = max(self.xcor() - 20, -350)  # Prevent moving off the left side
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = min(self.xcor() + 20, 350)  # Prevent moving off the right side
        self.goto(new_x, self.ycor())

    def reset_position(self):
        self.goto(0, -320)
