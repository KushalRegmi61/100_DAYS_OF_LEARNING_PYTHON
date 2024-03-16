import turtle as t
import random
turt = t.Turtle()
t.colormode(255)

#TODO  random color generator function color_generator()
def color_generator():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    random_color = (r, g, b)
    return random_color

j = -100
turt.pu()
turt.setx(-140)
turt.sety(-100)
turt.hideturtle()
#TODO dot() function to generate spot painting
def dot():
    
    turt.dot(10,color_generator())
    turt.pu()
    turt.fd(30)
    
    turt.dot(10,color_generator())
    
#TODO MAIN BLOCK OF CODE    
for i in range(10):
    for k in range(10):
        dot()
    turt.setx(-140)
    j = j+30
    turt.sety(j)

#TODO HOLDING THE SCREEN UNTIL THE CLICK
holdscreen =t.Screen()
holdscreen.exitonclick()
 