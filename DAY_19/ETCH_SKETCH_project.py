from turtle import Screen, Turtle
turt = Turtle()
screen = Screen()

#function to input the direction 
def forward():
    turt.forward(20)

def backward():
    turt.backward(20)

def anti_clockwise():
    turt.left(10) 

def clockwise():
    turt.right(10)
       
def returnhome():
    turt.home()
    screen.clear()
        
turt.speed(100)

#TODO USING SCREEN ONKEY FUNCTION TO CREATE ETCH-A-SKETCH GAME...
screen.listen()    
screen.onkey(fun=forward, key ="w")
screen.onkey(fun =backward,key="s")
screen.onkey(anti_clockwise,key="a")
screen.onkey(clockwise,key="d") 
screen.onkey(returnhome, "c")

#TODO HOLD THE SCREEN UNTIL THE CLICK
screen.exitonclick()