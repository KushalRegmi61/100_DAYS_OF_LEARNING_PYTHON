from turtle import Screen, Turtle
from snake import Snake
import time
#creating Screen class object
screen = Screen()
screen.setup(width= 600 , height= 600) 
screen.bgcolor("black")
screen.title("Snake Game...")
screen.tracer(0)

#creating a Snake class object
snake = Snake()
screen.listen()
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(.1)
    
    snake.move()
    screen.onkey(snake.up, key = "Up")
    screen.onkey(snake.down, key = "Down")
    screen.onkey(snake.right, key = "Right")
    screen.onkey(snake.left, key = "Left")
    
    
    
    
screen.exitonclick()