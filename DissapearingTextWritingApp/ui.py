from tkinter import *
from tkinter import messagebox

#global variables   
TIME = 10
HIGHSCORE = 0



class TextDisappearingApp:
    def __init__(self) :
        self.root = Tk()

        #setting up the window
        self.root.title("Text Disappearing App") # Title of the window
        self.root.config(padx=20, pady=20) # Padding of the window
        self.root.resizable(False, False) # Disable resizing of the window
        # self.root.iconbitmap("icon.ico") # Icon of the window
        self.root.geometry("1000x600")    #seting the window size 

        # setting up the score label
        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", font=("Times New Roman", 20, "bold"), fg="black")
        self.score_label.grid(row=0, column=0)

        # setting up the timer 
        self.timer_label = Label(text="Timer", font=("Times New Roman", 20, "bold"), fg="black")
        # right corner
        self.timer_label.grid(row=0, column=5, sticky="e")      

 

        # setting up the text widget
        self.text = Text(self.root, font=("Times New Roman", 20), height=10, width=73, wrap=WORD, state=DISABLED)
        self.text.grid(row=1, column=0, columnspan=7, pady=20 )
                   
        # setting up the time left label
        self.time_left = TIME
        self.time_label = Label(text=f"Time Left: {self.time_left} Sec", font=("Times New Roman", 18, "bold"), background="black", fg="white") # Time left label
        self.time_label.grid(row=2, column=0)

        # setting up the start button
        self.start_button = Button(text="Start", font=("Times New Roman", 20, "bold" ) )
        self.start_button.grid(row=3, column=0, pady=50)

        # setting up the quit button 
        self.quit_button = Button(text="Quit", font=("Times New Roman", 20, "bold") )
        self.quit_button.grid(row=3, column=6, pady=50)




        # run the app
        self.root.mainloop()
