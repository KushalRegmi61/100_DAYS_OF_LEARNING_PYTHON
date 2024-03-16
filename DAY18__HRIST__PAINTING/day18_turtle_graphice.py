import turtle as t
import random

turtle = t.Turtle()
t.colormode(255)
def color_generator():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    random_color = (r, g, b)
    return random_color
 
tp = turtle.pos()
tp
(0.00,0.00)
turtle.goto(60)
turtle.pos()
(60.00,0.00)
turtle.goto(y=10)
turtle.pos()
(60.00,10.00)
turtle.goto(20, 30)
turtle.pos()
(20.00,30.00)    

# turt.speed(10000)
# def draw_oscillograph(tilt_size):
#     for i in range(int(360/tilt_size)):
#             turt.pencolor(color_generator())
#             turt.circle(100)
#             turt.setheading(turt.heading()+tilt_size)
#             turt.circle(100)  
# draw_oscillograph(5)            


#TODO HOLDING THE SCREEN UNTIL THE CLICK
holdscreen =t.Screen()
holdscreen.exitonclick()
 