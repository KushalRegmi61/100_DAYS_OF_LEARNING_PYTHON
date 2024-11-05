from turtle import Screen, Turtle
from border import Border
from scoreboard import Scoreboard
from pedal import Pedal
from ball import Ball
from brick import Brick
import time


#global varible
is_game_on = False

# Create a screen
screen = Screen()

# Set up the screen
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)  # Disable automatic animation for faster drawing
screen.listen()


# Notify the user to start the game
notification = Turtle()
def start_notification():
    notification.hideturtle()
    notification.penup()
    notification.color("white")
    notification.goto(0, 0)
    notification.write("Press SPACE to start the game", align="center", font=("Courier", 24, "normal"))

start_notification() # Display the notification

# Create the border for the game
border = Border()

#creating the bricks
brick = Brick()

#create a scorecard
scoreboard = Scoreboard()


#creating a pedal
pedal = Pedal((0, -320))


#creating a ball
ball = Ball((0, 0))

#Start the game function
def start_game():
    global is_game_on
    is_game_on = True
    notification.clear()  # Clear the notification


# Bind start_game function to spacebar key
screen.onkey(start_game, "space")


while True:

    is_game_on = False # Stop the game

    while not is_game_on:
        screen.update()

    #binding the pedal to the left and right key
    screen.onkeypress(pedal.move_left, "Left")
    screen.onkeypress(pedal.move_right, "Right")

    # Start the game
    while is_game_on:
        screen.update()
        
        # Move the ball 
        ball.move() 


        time.sleep(.02)

         

        # Detect collision with the wall
        if ball.xcor() > 380 or ball.xcor() < -380:
            ball.bounce_x()

        # Detect collision with the ceiling
        if ball.ycor() > 290:
            ball.bounce_y()

        #function to stop pedal from moving outof the screen
        if pedal.xcor() > 350:
            pedal.goto(350, -320)
        if pedal.xcor() < -350:
            pedal.goto(-350, -320)

        # Detect collision with the pedal
        if ball.distance(pedal) < 50 and ball.ycor() < -300:
            ball.bounce_y()

        #checking the ball out of range
        if ball.ycor() < -380 and ball.xcor() < -350:
            if scoreboard.life > 0:
                ball.reset_position()
                scoreboard.life =scoreboard.life-1
                scoreboard.update_scoreboard()

            else:
                scoreboard.game_over()
                is_game_on = False

        # Detect collision with the bricks
        for demo_brick in brick.bricks_list:
            if ball.distance(demo_brick) < 20:
                ball.bounce_y()
                brick.remove_brick(demo_brick)
                scoreboard.increase_score()
                break

    # Start the main loop
    # screen.mainloop()




