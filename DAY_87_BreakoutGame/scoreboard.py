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
        self.update_scoreboard()
        self.new_turtle = Turtle()

    def update_scoreboard(self):
        self.clear()  # Clear previous score text before updating
        self.goto(0, 300)
        self.write(f"Score: {self.score}        Life: {self.life}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.update_scoreboard()
        
        self.new_turtle.hideturtle()
        self.new_turtle.penup()
        self.new_turtle.color("white")
        self.new_turtle.goto(0, 0)
        self.new_turtle.write(f"GAME OVER :(\t\tScore: {self.score}", align="center", font=("Courier", 24, "normal"))
        
    def restart_game(self):
        self.score = 0
        self.life = 3
        self.clear()  # Clear previous score text before updating
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()  # Update scoreboard after increasing score

    # method to detect the game win
    def game_win(self):
        self.update_scoreboard()
        self.new_turtle.write("YOU WIN", align="center", font=("Courier", 24, "normal"))

