from tkinter import *

#global variables
THEME_COLOR = "#375362"

class TypingSpeedTestApp:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1300x700")
        self.root.config(bg=THEME_COLOR)

        #setting the title of the window
        self.root.title("Typing Speed Test App")
        #adding padding to the window
        self.root.config(padx=35, pady=20)

        #creating the highest score label 
        self.highest_score_label = Label(self.root, text="Highest Score: 0", font=("Times New Roman", 18, "bold"))
        self.highest_score_label.grid(row=0, column=0, padx=10, pady=10)

        #creating the WPM label
        self.wpm_label = Label(self.root, text="WPM: 0", font=("Times New Roman", 18, "bold"))
        self.wpm_label.grid(row=0, column=2, padx=10, pady=10)

        #creating the timer label
        self.timer_label = Label(self.root, text="Timer: 0", font=("Times New Roman", 18, "bold"))
        self.timer_label.grid(row=0, column=4, padx=10, pady=10)

        #creating the start button
        self.start_button = Button(self.root, text="Start", font=("Times New Roman", 18, "bold"))
        self.start_button.grid(row=0, column=6, padx=10, pady=10)

        #creating the text widget
        self.text_widget = Text(self.root, font=("Times New Roman", 18, "bold"), wrap=WORD, width=100, height=10)
        self.text_widget.grid(row=1, column=0, padx=10, pady=10, columnspan=7)

        #initializing the mainwindow loop
        self.root.mainloop()