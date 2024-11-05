from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.life = 3
        self.color("white")
        self.penup()
        self.hideturtle()
        # Position near the top of the screen, assuming standard turtle screen dimensions
        self.goto(0, 300)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()  # Clear previous score text before updating
        self.write(f"Score: {self.score}        Life: {self.life}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()  # Update scoreboard after increasing score
