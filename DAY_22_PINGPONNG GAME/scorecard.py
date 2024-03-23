from turtle import Turtle
class Scorecard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.r_score = 0 
        self.l_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.clear()    
        self.goto(-100,200)
        self.write(self.l_score,align = "center" , font=("Courier",80, "normal"))
        self.goto(100,200)
        self.write(self.r_score,align = "center" , font=("Courier",80, "normal"))
        
    def left_score(self):
        self.l_score += 1
        self.update_score()
        
    def right_score(self):
        self.r_score += 1
        self.update_score()    
        
            