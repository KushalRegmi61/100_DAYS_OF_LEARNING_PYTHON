from turtle import Screen
from snake import Snake
import time
from food import Food
#creating Screen class object
screen = Screen()
#creating a Food class object
food = Food()

#creating a function to ask for the user input
def user_choice():
    choice = screen.textinput("Do you want to play the game?")
    return choice.lower() == "y"
#modifying the screen
screen.setup(width= 600 , height= 600) 
screen.bgcolor("black")
screen.title("Snake Game...")
screen.tracer(0)
screen.listen()

#creating Score class object
from scorecard import Scoreboard
score = Scoreboard()

#creating snake class object and moving the snake
snake = Snake()
# snake.speed(900)
screen.onkey(snake.up, key = "Up")
screen.onkey(snake.down, key = "Down")
screen.onkey(snake.right, key = "Right")
screen.onkey(snake.left, key = "Left")



is_game_on = True

while is_game_on:

#decting collision with  its tail   
    for segment in snake.segment[1:]:
        if snake.segment[0].distance(segment)< 10:
            score.reset() 
            snake.reset()      

#decting collision with food
    if snake.head.distance(food)<15:
        food.new_position()
        snake.extend()
        score.increase_score()
            
 #decting collison with wall       
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()<-290 or snake.head.ycor()>290:
        score.reset()
        snake.reset()
    
    screen.update()
    time.sleep(.1)
    snake.move()
    
    
                     
#TODO PRINTING THE FINAL SCORE
 
    
    
screen.exitonclick()