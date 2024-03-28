# Assuming that the Scoreboard class is defined in "scorecard.py" file
# Make sure the file name and class name match

from turtle import Screen
from pedal import Pedal
from ball import Ball
import scorecard
import random
scoreboard = scorecard.Scorecard()

# Rest of your code...
import time

# Create a screen
screen = Screen()
# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Pedal((-375,0))
r_paddle = Pedal((370, 0))

#creating a ball class object
from ball import Ball
ball = Ball((0,0))


         

# using screen listen function to move turtle up and down
screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.listen()
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

is_game_on = True
while is_game_on:
        #detect it the ball out range of l_paddle      
    if ball.xcor() < -380:
        ball.reset_position()  
        scoreboard.right_score()    
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor()< -280:
        ball.bounce_y()
    
    #dtect collsion with paddle
    if ball.distance(l_paddle)<45 and ball.xcor()<-340 or ball.distance(r_paddle)<45  and ball.xcor()>330:
        ball.bounce_x()
        ball.speed(random.randint(0, 10))
    
    #detect it the ball out range of r_paddle        
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_score()
        

        
        

                
    
screen.exitonclick()

