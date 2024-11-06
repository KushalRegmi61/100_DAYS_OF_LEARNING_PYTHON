from turtle import Screen, Turtle
from border import Border
from scoreboard import Scoreboard
from pedal import Pedal
from ball import Ball
from brick import Brick
import time

# Global variable
is_game_on = False

# Set up the screen
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)  # Disable automatic animation for faster drawing

# Create game elements
border = Border()
brick = Brick()
scoreboard = Scoreboard()
pedal = Pedal((0, -320))
ball = Ball((0, 0))

# Notification to start game
notification = Turtle()
notification.hideturtle()
notification.penup()
notification.color("white")

def display_start_notification():
    """Displays the start notification for the player."""
    notification.clear()
    notification.goto(0, -40)
    notification.write("Press SPACE to start the game", align="center", font=("Courier", 24, "normal"))

display_start_notification()  # Initial notification

# Start game function
def start_game():
    global is_game_on
    is_game_on = True
    scoreboard.new_turtle.clear()
    notification.clear()  # Clear notification on game start

# Bind start_game function to spacebar key
screen.listen()
screen.onkey(start_game, "space")

# Paddle movement controls
screen.onkeypress(pedal.move_left, "Left")
screen.onkeypress(pedal.move_right, "Right")

# Main game loop
while True:
    # Wait until game starts
    while not is_game_on:
        screen.update()

    # Start game play loop
    while is_game_on:
        screen.update()
        ball.move()
        time.sleep(0.02)  # Lower sleep time for smoother animation

        # Detect collision with the walls
        if ball.xcor() > 380 or ball.xcor() < -380:
            ball.bounce_x()

        # Detect collision with the ceiling
        if ball.ycor() > 290:
            ball.bounce_y()

        # Restrict paddle within screen limits
        if pedal.xcor() > 350:
            pedal.setx(350)
        if pedal.xcor() < -350:
            pedal.setx(-350)

        # Detect collision with the paddle
        if ball.ycor() < -300 and pedal.xcor() - 70 < ball.xcor() < pedal.xcor() + 70:
            ball.bounce_y()

        # Check if ball is out of bounds
        #checking the ball out of range
        if ball.ycor() < -330 or ball.xcor() < -395:
            if scoreboard.life > 1:
                ball.reset_position()
                scoreboard.life =scoreboard.life-1
                is_game_on = False

            else:
                scoreboard.life = 0

                #reseting the ball position
                ball.reset_position()

                #recreating the bricks
                brick.reset_bricks()

                #updating the scoreboard
                scoreboard.game_over()
                #restarting the game
                scoreboard.restart_game()
                is_game_on = False

            # update the scoreboard
            scoreboard.update_scoreboard()

            # Notify the user to start the game again
            display_start_notification()
            #reset the pedal position
            pedal.reset_position()

        # Detect collision with bricks
        for demo_brick in brick.bricks_list:
            if ball.distance(demo_brick) < 30:
                ball.bounce_y()
                brick.remove_brick(demo_brick)
                scoreboard.increase_score()
                break

        # Check if all bricks are cleared
        if len(brick.bricks_list) == 0:
            scoreboard.game_win()
            brick.reset_bricks()
            ball.reset_position()
            pedal.reset_position()
            is_game_on = False
            display_start_notification()
            break

screen.mainloop()
