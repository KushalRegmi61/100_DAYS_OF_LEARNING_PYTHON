COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
import random
from turtle import Turtle
class CarManager():
    def __init__(self):
        self.all_cars =[]
        self.car_speed = STARTING_MOVE_DISTANCE
        
        #   method  for creating new car:
    def create_newcar(self):
        if (random.randint(1,5) ==1):
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid= 1)
            new_car.penup()
            y_cor= random.randint(-255,260)
            new_car.goto(300, y_cor)
            self.all_cars.append(new_car)
        
        #  method to move car
    def moving_car(self):
        for j in self.all_cars:
            j.backward(self.car_speed)    
        
        #method to increase car speed
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
        