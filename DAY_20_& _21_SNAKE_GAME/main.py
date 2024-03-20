from turtle import Screen
from snake import Snake
import time
from food import Food
#creating Screen class object
screen = Screen()
#creating a Food class object
food = Food()

#modifying the screen
screen.setup(width= 600 , height= 600) 
screen.bgcolor("black")
screen.title("Snake Game...")
screen.tracer(0)
screen.listen()

#creating Score class object
from scorecard import Score
score = Score()

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
        if snake.head.distance(segment)< 10:
            is_game_on = False       

#decting collision with food
    if snake.head.distance(food)<15:
        food.new_position()
        snake.extend()
        score.increase_score()
            
 #decting collison with wall       
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()<-290 or snake.head.ycor()>290:
        is_game_on = False       
    
    screen.update()
    time.sleep(.1)
    snake.move()
    screen.title(f"Score = {score.score}")
                     
#TODO PRINTING THE FINAL SCORE

score.game_over()    
    
    
screen.exitonclick()