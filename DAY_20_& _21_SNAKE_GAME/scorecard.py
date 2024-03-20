from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("Blue")
        self.pu()
        self.hideturtle()
        
    def increase_score(self):    
        self.score += 1       
        
         
    def game_over(self):
        self.goto( 0, 250)
        self.write(f"Your final Score ={self.score}", align="center", font = ('Courier', 24,'normal'))
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font = ('Courier', 24,'normal'))    
        