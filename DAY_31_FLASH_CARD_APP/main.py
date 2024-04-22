from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

#-----------------------------------------reading from csv file
try:
    words = pandas.read_csv(r"E:\python\DAY_31_FLASH_CARD_APP\data\words_to_learn.csv")
except FileNotFoundError:
    words = pandas.read_csv(r"E:\python\DAY_31_FLASH_CARD_APP\data\french_words.csv") 
finally:
    data_list = words.to_dict(orient="records")#converting the data to list
   
NEW_CARD = {}
TIMER = NONE

#------------------------------------- functions to flip cards ---------------------------------------------#
def display_time(count):#function to display time remaining
    canvas.itemconfigure(time, text = f"TIME_LEFT = 00:0{count}")
    global TIMER
    if count>0:
        window.after(1000, display_time, count-1)
        
def pop_card():#function to pop_new_card
    global NEW_CARD 
    
    next_card()
    data_list.remove(NEW_CARD)
    words_to_learn = pandas.DataFrame(data_list)
    words_to_learn.to_csv(r"E:\python\DAY_31_FLASH_CARD_APP\data\words_to_learn.csv", index= False)
    
def next_card():#displaying the random french words to the screen.......
    new_data = random.choice(data_list)
    global NEW_CARD , flip_timer
    NEW_CARD = new_data
    window.after_cancel(flip_timer)
    #configing the canvas objects
    canvas.itemconfig(canvas_img, image = card_front)
    canvas.itemconfig(language, text= "French", fill = "black")
    canvas.itemconfig(Word, text= new_data["French"], fill = "black")
    display_time(3)
    flip_timer= window.after(3000,flip_card)

def flip_card():#displaying the english translation of french words to the screen.............
    canvas.itemconfig(canvas_img,image =back_card )
    canvas.itemconfig(language, text= "English", fill = "white")
    canvas.itemconfig(Word, text= NEW_CARD["English"], fill = "white")



#------------------------------------- UI SETUP -----------------------------------------------------------#
window = Tk()
window.title("FLASH_CARD APP")
window.config(padx = 50, pady= 50, bg= BACKGROUND_COLOR)

#-----Saving the photo paths
back_card = PhotoImage(file = r"DAY_31_FLASH_CARD_APP\images\card_back.png")
card_front = PhotoImage(file = r"DAY_31_FLASH_CARD_APP\images\card_front.png")
right = PhotoImage(file =r"DAY_31_FLASH_CARD_APP\images\right.png")
wrong = PhotoImage(file= r"DAY_31_FLASH_CARD_APP\images\wrong.png")

# setting canvas to the screen
canvas = Canvas(window, height=526, width=800, highlightthickness=0, bg = BACKGROUND_COLOR)
canvas_img = canvas.create_image(400, 278,image = card_front)

#creating the canvas_text
language= canvas.create_text(400, 150, text="Language", font=("Times New Roman", 30, "bold"))
Word = canvas.create_text(400,283, text="Word", font=("Times New Roman", 30, "bold"))
time = canvas.create_text(120, 490, text="TIME_LEFT = 00:00",font=("Times New Roman", 15, "bold"))
#setting Canvas to the screen
canvas.grid(row= 0, column= 1, columnspan= 3)

#setting the timer_variable
flip_timer = NONE
#adding cross button to the Left side of the screen 
unknown_button = Button(image=wrong, highlightthickness=0, command =next_card )
unknown_button.grid(row= 1, column= 0 , columnspan=2)

#adding tick button to the screen Right side of the screen 
known_button= Button(image= right, highlightthickness=0, command=pop_card)
known_button.grid(row = 1, column= 3, columnspan= 2)



#turing the screen on
window.mainloop()
