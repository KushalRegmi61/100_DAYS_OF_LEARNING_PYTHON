import turtle
import csv
import pandas
#creating a screen class object
screen = turtle.Screen()
image =r"DAY_25\us_states_game\blank_states_img.gif"

#adding image to screen
screen.addshape(image)
turtle.shape(image)

# creating states varible
states = pandas.read_csv(r"DAY_25\us_states_game\50_states.csv")
states_name = []
#creating a states_name list
for name in states["state"].to_list():
    states_name.append(name.strip())
#turning the screen tracer off
screen.tracer(0)    
# print(states_name)
guessed_states = [] # creating an empty guessed state list

while len(guessed_states)<50:
        #askking user to input state name
    answer_state = screen.textinput(title= f"{len(guessed_states)}/50 State_Correct", prompt="Enter the state name...").title()
    if answer_state in states_name : #checking if the user's answer is in the state
        state_name = states[states.state == answer_state]
        turtle.penup()
        turtle.goto(x = int(state_name["x"]), y = int(state_name["y"]))
        turtle.write(answer_state) #writing the states name to the screen
        turtle.home()
        guessed_states.append(answer_state)
    elif answer_state == "Exit":
        break    
    #updating the screen    
    screen.update()        
    
#creating a csv file that containg list of missing states   
for state in guessed_states:
    if state in states_name:
        states_name.remove(state)   
  
#creating a csv file for  the missing states 
dict = {"Missing_States_Name": states_name }
missing_states = pandas.DataFrame(dict)
# print(missing_states)
missing_states.to_csv(r"DAY_25\us_states_game\missing_states_to_learn.csv")

