from turtle import  Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.pu()
        self.hideturtle()
        self.goto(-210, 265)
        self.score = 0
        self.display_score()
    
    #display score method
    def display_score(self):
        self.clear()
        self.write(f"Level = {self.score}",align="center" , font=FONT)
    
    #method to update the score
    def update_score(self):
        self.score += 1
        self.display_score()
    
    #display final score
    def final_score(self):
        self.clear()
        self.home()
        self.write(f"oop!, You got hit by a car: \n  Your final Level = {self.score}",align="center" , font=FONT)
        
           