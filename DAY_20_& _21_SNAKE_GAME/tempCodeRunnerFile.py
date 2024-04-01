from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
       
       #opening the file data.txt
file = open("data.txt") 
high_score = int(file.read())
file.close()
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("white")
        self.penup()
        self.high_score = high_score
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High_Score = {self.high_score}", align=ALIGNMENT, font=FONT)

#method to check current score with highscore
    def reset(self):
        if self.score>=self.high_score:
            with open("data.txt", mode= "w") as file:
                self.high_score = self.score
                file.write(f"{self.high_score}")
            
        self.score =0
        self.update_scoreboard()
        

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
