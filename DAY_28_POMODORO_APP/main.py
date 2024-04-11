import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN =5
LONG_BREAK_MIN = 20
ROUND = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_button():
    window.after_cancel(TIMER)
    label_1.config(text = "Timer")
    canvas.itemconfig(canvas_text, text = "00:00")
    global ROUND
    ROUND =0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global  ROUND
    ROUND += 1
    SHORT_BREAK_sec =SHORT_BREAK_MIN * 60
    LONG_BREAK_sec = LONG_BREAK_MIN*60
    work_sec =WORK_MIN*60
    if  ROUND %2 ==0:
        display_time(SHORT_BREAK_sec)
        label_1.config(text= "SHORT BREAK!...", fg = PINK)
    elif ROUND %8 ==0:
        display_time(LONG_BREAK_sec)
        label_1.config(text= "TAKE A BREAK!...", fg = RED)
    else:
        display_time(work_sec)
        label_1.config(text= "STUDY TIME!...", fg = GREEN)
 
            
  
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def display_time(count):
    marks = ""
    global ROUND
    work_session = math.floor(ROUND/2)    
    for i in range(work_session):
            marks +="✓"   
    tick.config(text = marks) #display tick on completion on each study session
    if count >=0:
        min = math.floor(count/60)
        sec = count%60
        if sec >9:
            canvas.itemconfig(canvas_text, text =f"{min}:{sec}")
        else:
            canvas.itemconfig(canvas_text, text =f"{min}:0{sec}")
        
        global TIMER        
        TIMER =window.after(1000,display_time, count-1)
            
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()       # creating a Tk() object
window.title("Pomodoro")    #setting window_title
#adding "Timer label to the screen"
label_1 = Label(text="Timer", fg=GREEN, font= ("Times New Roman", 45), bg = YELLOW)
label_1.grid(row= 0, column= 1)
# Set the window background color to yellow
window.config(padx= 50, pady=50, bg=YELLOW)
#crating a variable that store the tomato_image
tomato_img =PhotoImage(file= r"DAY_28\tomato.png")
#crating a canvas object
canvas = Canvas(width= 300, height= 300,bg = YELLOW, highlightthickness= 0)
#adding tomato image to the screen
canvas.create_image(150, 150, image = tomato_img)
#writing text to the screen
canvas_text = canvas.create_text(150, 170, text="00:00", fill= "white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row = 1, column= 1)    #setting canvas to the screen

#creating Start_button...
start_button = Button(text="Start", font= ("Times New Roman", 15), command= start_timer)
start_button.grid(row = 3, column= 0)


#creating Reset_button...
reset_button = Button(text="Reset", font= ("Times New Roman", 15), command=reset_button)
reset_button.grid(row = 3, column= 2)

#creating a function to display "✓" on screen 

tick = Label(fg = GREEN ,bg = YELLOW, font=( 0,20,) )
tick.grid(row = 3, column= 1)


# Opening the window
window.mainloop()
