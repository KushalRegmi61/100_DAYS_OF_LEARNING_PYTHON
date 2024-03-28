import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#creating a player calss object
player = Player()

#creating a car_manager class object
car =CarManager()

#creating a scoreboard class object
score = Scoreboard()
#TODO  making screen to listen for events
screen.listen()
screen.onkey(fun = player.move_up, key= "Up")

game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()
    car.create_newcar()
    car.moving_car()
    
    #CHECKING IF THE PLAYER HAS COLLIDED WITH THE CAR
    for acar in car.all_cars:
        if acar.distance(player)<20:
            game_is_on = False
            # displaying the final score 
            screen.clear()
            score.final_score()
    #CHECKING IF THE PLAYER HAS REACHED FINISH LINE OR NOT
    if player.restart():
        player.go_to_startposition()
        car.increase_speed()
        score.update_score()

       

screen.exitonclick()    