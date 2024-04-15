import turtle
import csv
import pandas
#creating a screen class object
screen = turtle.Screen()
image =r"DAY_25_THREE_PORJECTS\us_states_game\blank_states_img.gif"

#adding image to screen
screen.addshape(image)
turtle.shape(image)

# creating states varible 
states = pandas.read_csv(r"DAY_25_THREE_PORJECTS\us_states_game\50_states.csv")
states_name =[ name.strip() for name in states["state"].to_list()]

#turning the screen tracer off
screen.tracer(0)    

guessed_states = [] # creating an empty guessed state list

while len(guessed_states)<50:
    
#askking user to input state name
    answer_state = screen.textinput(title= f"{len(guessed_states)}/50 State_Correct", prompt="Enter the state name...").title()
    
#checking if the user's answer is in the state
    if answer_state in states_name and answer_state not in guessed_states : 
        state_name = states[states.state == answer_state]
        turtle.penup()
        turtle.goto(x = int(state_name["x"]), y = int(state_name["y"]))
        turtle.write(answer_state) #writing the states name to the screen
        turtle.home()
        guessed_states.append(answer_state)
        
#exiting the loop if user enter exit    
    elif answer_state == "Exit":
        break    
#updating the screen    
    screen.update()        

#creating  list containg name  of missing states    
missing_states_names= [state for state in states_name if state not in guessed_states]        

#creating a csv file for  the missing states 
dict = {"Missing_States_Name": missing_states_names }
missing_states = pandas.DataFrame(dict)
missing_states.to_csv(r"DAY_25_THREE_PROJECTS\us_states_game\missing_states_to_learn.csv")

