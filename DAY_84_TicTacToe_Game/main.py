from tkinter import *


window = Tk()


# #creating a window
# tk.title("Tic Tac Toe")
# tk.geometry("400x400")


# #creating a label
# lbl = Label(tk, text="Hello World")
# lbl.grid(row=0, column=0)
# #creating a input field
# entry = Entry(tk)
# entry.grid(row=1, column=0, columnspan=2)

# #fucntion to get the input from the input field
# def get_input():
#     lbl.config(text=entry.get())

# #creating a button
# btn = Button(tk, text="Click Me", command=get_input)
# btn.grid(row=2, column=0, columnspan=2)

#language= canvas.create_text(400, 150, text="Language", font=("Times New Roman", 30, "bold"))



#creating a window
window.title("Tic Tac Toe")
window.geometry("600x500")
#adding padding to the window
window.config(padx=100, pady=40)

#creating a title_label
title_label = Label(text="Start", font=("Times New Roman", 20, "bold"))
title_label.grid(row=0, column=1, columnspan=3)

#creating cells for the game
def create_cells():
    for i in range(3):
        for j in range(3):
            cell = Button(
                text=" ", 
                font=("Times New Roman", 20, "bold"), 
                width=8, 
                height=3, 
                # bg="lightblue", 
                # fg="black", 
                # relief="solid", 
                borderwidth=1
            )
            cell.grid(row=i+1, column=j+1, )

#creating two additional buttons 
# 1. start button
start_button = Button(text="Start", font=("Times New Roman", 16, "bold"))
start_button.grid(row=4, column=3, padx=15, pady=10)


# 2. Restart button
restart_button = Button(text="Restart", font=("Times New Roman", 16, "bold"))
restart_button.grid(row=4, column=1, padx=10, pady=10)  
restart_button.config(state=DISABLED)
       

create_cells()
#creating mainloop for the window
window.mainloop()