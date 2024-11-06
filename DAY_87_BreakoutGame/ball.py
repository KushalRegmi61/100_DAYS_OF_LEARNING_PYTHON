from turtle import Turtle

class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(position)
        self.x_move = 10
        self.y_move = 10
        self.speed("normal")

    def move(self):
        # Update position with boundary checks
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        # Check if the new position is within bounds
        if -400 < new_x < 400 and -400 < new_y < 400:
            self.goto(new_x, new_y)
        else:
            # Reset ball position if out of bounds
            self.reset_position()

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_y()  # Change direction on reset
