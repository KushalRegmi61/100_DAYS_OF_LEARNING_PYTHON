from tkinter import *
import random

window = Tk()


#creating a x_state and o_state
x_state = []   
o_state = []

#creating a turn variable
turn = 0


#creating a winning_list
winning_list = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]


#creating a window
window.title("Tic Tac Toe")
window.geometry("600x500")
#adding padding to the window
window.config(padx=100, pady=40)

#creating a title_label
title_label = Label(text="Let's Play", font=("Times New Roman", 20, "bold"))
title_label.grid(row=0, column=1, columnspan=3)

#creating a game_tied function  
def game_tied():
    global x_state, o_state
    if x_state.count(1) + o_state.count(1) == 9: #count 1's in x_state and o_state
        title_label.config(text="Game Tied")
        for i in button_list:
            i.config(command=DISABLED)


#creating a button list
button_list = []

#creating cells for the game
def create_cells():
    global button_list
    for i in range(3):
        for j in range(3):
            cell = Button(
                text=" ", 
                font=("Times New Roman", 20, "bold"), 
                width=8, 
                height=3, 
                borderwidth=2,
                state=DISABLED,
            )
            button_list.append(cell)
            cell.grid(row=i+1, column=j+1)

#function to print the board
def printboard(x_state, o_state):     
    #function to check game tied
    game_tied()

    #printing the board
    for i in range(3):
        for j in range(3):
            if x_state[i*3+j] == 1:
                button_list[i*3+j].config(text="X",  fg="red", command=DISABLED)
            elif o_state[i*3+j] == 1:
                button_list[i*3+j].config(text="O",  fg="blue", command=DISABLED)
            
            else:
                button_list[i*3+j].config(text=" ")


#checking the winner
def check_winner(x_state, o_state):
    for i in winning_list:
        if x_state[i[0]] and x_state[i[1]] and x_state[i[2]]:
            title_label.config(text="X wins")
            printboard(x_state, o_state)

            return 1
        if o_state[i[0]] and o_state[i[1]] and o_state[i[2]]:
            title_label.config(text="O wins")
            printboard(x_state, o_state)
            printboard(x_state, o_state)
            return 0
        
    return -1

#function to handle the button click
def handle_click(row, col):
    global turn, x_state, o_state
    if turn:
        title_label.config(text="O's turn")
        x_state[row*3+col] = 1
    else:
        title_label.config(text="X's turn")
        o_state[row*3+col] = 1
    printboard(x_state, o_state)
    result = check_winner(x_state, o_state)
    if result == 1:
        for i in button_list:
            i.config(command=DISABLED)
    elif result == 0:
        for i in button_list:
            i.config(command=DISABLED)
    turn = 1 - turn


# 1. start button
start_button = Button(text="Start", font=("Times New Roman", 16, "bold"))
start_button.grid(row=4, column=2, padx=15, pady=10)

#function to start the game
def start_game():
    global turn, x_state, o_state, button_list
    turn = random.randint(0, 1)
    x_state = [0,0,0,0,0,0,0,0,0]
    o_state = [0,0,0,0,0,0,0,0,0]

#enabling the buttons
    for i in range(3):
        for j in range(3):
            button_list[i*3+j].config( state=NORMAL,command=lambda i=i, j=j: handle_click(i, j))

    printboard(x_state, o_state)
    title_label.config(text="0's turn" if   turn == 0 else "X's turn")

#binding the start button to the start_game function
    start_button.config(text="Restart")

#binding the start button to the start_game function
start_button.config(command=start_game)    
     


# calling the create_cells function
create_cells()



#creating mainloop for the window
window.mainloop()