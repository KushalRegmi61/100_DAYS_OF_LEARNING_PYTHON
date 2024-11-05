from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food
from scorecard import Scoreboard

# Create Screen object
screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.title("Snake Game...")
screen.tracer(0)
screen.listen()

#creating a white broder at x= 300
border = Turtle()
border.penup()
border.goto(-300, -300)
border.pendown()
border.color("white")
border.pensize(10)
border.forward(600)
border.penup()
border.goto(-300, 300)
border.pendown()
border.forward(600)

# Create Snake object
snake = Snake()

# Create Food object
food = Food()

# Create Scoreboard object
score = Scoreboard()



#creating notifiaction for the user
notification = Turtle()

def draw_notification():
    notification.penup()
    notification.hideturtle()
    notification.color("white")
    notification.goto(0,0)
    notification.write("Press Space to start the game", align="center", font=("Courier", 24, "normal"))


draw_notification()
# Function to start the game
def start_game():
    global is_game_on
    is_game_on = True

    # Clear the notification
    notification.clear()

# Bind start_game function to spacebar key
screen.onkey(start_game, "space")


# Game loop
while True:
    is_game_on = False  # Game starts only when spacebar is pressed

    # Wait for spacebar press to start the game
    while not is_game_on:
        screen.update()

    # Reset snake, food, and score
    snake.reset()
    food.new_position()
    score.reset()

    # Event listeners for snake movement
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")

    while is_game_on:
        screen.update()
        time.sleep(0.1)

        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.new_position()
            snake.extend()
            score.increase_score()

        # Detect collision with walls
        if (
            abs(snake.head.xcor()) > 295
            or snake.head.ycor() > 298 or snake.head.ycor() < -298
        ):
            score.reset()
            snake.reset()
            is_game_on = False  # End the game loop
            draw_notification()

        # Detect collision with tail
        for segment in snake.segment[1:]:
            if snake.head.distance(segment) < 10:
                score.reset()
                snake.reset()
                is_game_on = False  # End the game loop

# Print final score
print("Final score:", score.current_score)

screen.exitonclick()
