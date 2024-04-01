from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("white")
        self.penup()
        #opening the file data.txt
        with open("E:\python\DAY_20_& _21_SNAKE_GAME\DAY21&22_snake_game_data.txt") as file:
            self.high_score = int(file.read())
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High_Score = {self.high_score}", align=ALIGNMENT, font=FONT)

#method to check current score with highscore
    def reset(self):
        if self.score>=int(self.high_score):
            self.high_score = self.score
            with open("E:\python\DAY_20_& _21_SNAKE_GAME/DAY21&22_snake_game_data.txt", mode= "w") as file:
                file.write(str(self.high_score))
            
        self.score =0
        self.update_scoreboard()
        

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
