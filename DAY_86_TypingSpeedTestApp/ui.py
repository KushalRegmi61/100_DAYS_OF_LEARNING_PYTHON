from tkinter import *
from tkinter import messagebox

#global variables
THEME_COLOR = "#375362"
TIME = 60
HIGH_SCORE = 80

class TypingSpeedTestApp:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1300x700")
        self.root.config(bg=THEME_COLOR)

        #setting the title of the window
        self.root.title("Typing Speed Test App")
        #adding padding to the window
        self.root.config(padx=35, pady=20)

        #self repeat variable for the timer
        self.repeat = 1


        #creating a list 
        self.QUOTES = ["The quick brown fox jumps over the lazy dog"]


        #creating the highest score label 
        self.highest_score_label = Label(self.root, text=f"Highest Score: {HIGH_SCORE} WPM ", font=("Times New Roman", 18, "bold"))
        self.highest_score_label.grid(row=0, column=0, padx=10, pady=10)

        #creating the WPM label
        self.wpm_label = Label(self.root, text="WPM: 0", font=("Times New Roman", 18, "bold"))
        self.wpm_label.grid(row=0, column=2, padx=10, pady=10)

        #creating the timer label
        self.timer_label = Label(self.root, text="Timer: 0", font=("Times New Roman", 18, "bold"))
        self.timer_label.grid(row=0, column=4, padx=10, pady=10)

        #creating the start button
        self.start_button = Button(self.root, text="Start", font=("Times New Roman", 18, "bold"), command=self.start_game)
        self.start_button.grid(row=0, column=6, padx=10, pady=10)

        #creating a canvas to display the text
        self.text_canvas = Canvas(self.root, bg="white", width=1200, height=200)
        self.text_canvas.grid(row=1, column=0, padx=10, pady=10, columnspan=7)
        
        #displaying the text
        self.demo_text=self.text_canvas.create_text(600, 100, text="Press Start Button to Begin.", font=("Times New Roman", 18, "bold"))

        #creating the text widget
        self.text_widget = Text(self.root, font=("Times New Roman", 18, "bold"), wrap=WORD, width=100, height=10, state=DISABLED)
        self.text_widget.grid(row=2, column=0, padx=10, pady=10, columnspan=7)

        #creating the submit button 
        self.submit_button = Button(self.root, text="Submit", font=("Times New Roman", 18, "bold"), command=self.submit_text)
        self.submit_button.grid(row=3, column=0, padx=10, pady=10)

        #initializing the mainwindow loop
        self.root.mainloop()


    #TODO: create a function to display the text "When the start_game button is clicked"
    def start_game(self):
        # Clear the text widget and enable it
        self.text_widget.config(state=NORMAL)
        self.text_widget.delete("1.0", END)

        #getting hold of start_button text
        self.start_text = self.start_button.cget("text")
        
        #fixing the timer 
        if self.start_text == "Restart" and self.repeat == 1:
            self.submit_text()

        # Change the start button text to "Restart"
        self.start_button.config(text="Restart")
        
        # Set the text for the typing test
        self.TEXT = self.QUOTES[0]
        self.text_canvas.itemconfig(self.demo_text, text=self.QUOTES[0])
        
        # Reset timer variables
        global TIME
        TIME = 20
        self.net_time = TIME
        self.timer_label.config(text=f"Timer: {TIME} Sec")
        
        # Reset repeat variable to allow binding
        self.repeat = 1
        
        # Bind the display_time method to start when any key is pressed
        self.bind_display_time()



    #TODO: create a function to start the timer
    def display_time(self):
        global TIME
        self.timer_label.config(text=f"Timer: {TIME} Sec")
        if TIME > 0:
            TIME -= 1
            
            # Check if repeat is still set to 1, preventing duplicate timers
            if self.repeat == 1:
                self.root.after(1000, self.display_time)

            # Update the WPM label
            wpm = self.calculate_wpm()
            self.wpm_label.config(text=f"WPM: {wpm}")
        else:
            # Stop the timer and notify the user
            self.text_canvas.itemconfig(self.demo_text, text="Time's Up!")
            messagebox.showinfo("Time's Up!", "Time's Up!")
            self.submit_text()
            self.text_widget.config(state=DISABLED)


    #TODO: create a function to calculate the WPM
    def calculate_wpm(self):
        # Get the typed text and calculate the number of characters
        typed_text = self.text_widget.get("1.0", END).strip()
        characters_typed = len(typed_text)
        
        # Calculate time elapsed in minutes
        time_elapsed = (self.net_time- TIME) / 60  # Converting seconds to minutes
        
        # Calculate WPM using standard formula
        wpm = (characters_typed / 5) / time_elapsed if time_elapsed > 0 else 0
        
        return int(wpm)
    

    #TODO: METHOD TO CALCULAAT THE ACCURACY 
    def calculate_accuracy(self):
        # Get the provided text and the typed text
        original_text = self.TEXT
        typed_text = self.text_widget.get("1.0", END).strip()
        
        # Calculate the total number of characters typed
        total_characters_typed = len(typed_text)
        
        # Initialize a counter for correct characters
        correct_characters = 0
        
        # Count correct characters (up to the length of the typed text or original text, whichever is shorter)
        for i in range(min(len(original_text), total_characters_typed)):
            if typed_text[i] == original_text[i]:
                correct_characters += 1
        
        # Calculate accuracy (if no characters are typed, accuracy is 0)
        accuracy = (correct_characters / total_characters_typed) * 100 if total_characters_typed > 0 else 0
        return round(accuracy, 2)
    

    #TODO: METHOD TO WORK WHEN THE SUBBMIT BUTTON IS CLICKED
    def submit_text(self):
        # Calculate the WPM and accuracy
        wpm = self.calculate_wpm()
        accuracy = self.calculate_accuracy() 
        
        # chaanging the self.repeat variable to 0
        self.repeat = 0

        # Display the results in a message box
        messagebox.showinfo("Typing Test Results", f"WPM: {wpm}\nAccuracy: {accuracy}%")
        


    #binding the display_time method to start when any key is pressed
    def bind_display_time(self):
        self.text_widget.bind("<KeyPress>", self.start_timer_once)

    #method to start the timer once
    def start_timer_once(self, event):
        self.text_widget.unbind("<KeyPress>")
        self.display_time()