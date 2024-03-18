from turtle import Turtle, Screen
import random
screen  = Screen()

screen.setup(height= 700, width=1200)
def race():
    is_race_on = False
    colors = ['red','blue', 'green', 'yellow', 'violet', 'orange']
    new_turtle = []
    y_index = [90, 60,30, 0, -30, -60]
    for i in range(6) :
        turtle = Turtle(shape= "turtle")
        turtle.color(colors[i])
        turtle.pu()
        turtle.goto(x=-590,y=y_index[i])
        new_turtle.append(turtle)
    user_choice = screen.textinput("MAKE YOUR BET!", "Which turtle will win the race? [choose the color:]")
        #starting the race 
    if user_choice:
        is_race_on = True

    while is_race_on:
        for turtle in new_turtle:
            if turtle.xcor()>= 580:
                turt_color = turtle.pencolor()
                is_race_on = False
                
            else:
                rand_distance = random.randint(1, 11)
                turtle.fd(rand_distance)

    screen.clear()   
        #TODO CHECKS IF THE USER HAS WON THE RACE OR NOT 
    if user_choice == turt_color:
            result_text = f"Congratulations! You won!\nYour Turtle Color Was: {turt_color}"
    else:
        result_text = f"Oops! {turt_color} color turtle has won the race.\nYou Lose :("

    result_display = Turtle()
    result_display.penup()
    result_display.goto(0, 0)
    result_display.write(result_text, align="center", font=("Arial", 24, "normal"))

race()
choice = screen.textinput(title="play again!", prompt="Do want to restart the game?(Y/N)") 
if choice.lower() == "yes" or choice.lower() == "y":
    screen.clear()
    race()
screen.exitonclick()