from turtle import Turtle

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.draw_border()

    # Draw border
    def draw_border(self):
        self.penup()
        self.hideturtle()
        self.goto(-400, 300)
        self.pendown()
        self.color("white")
        self.pensize(5)
        self.forward(800)

        


