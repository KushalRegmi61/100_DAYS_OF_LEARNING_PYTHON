from tkinter import *
from tkinter import messagebox
import random

#global variables
THEME_COLOR = "#375362"
TIME = 60
HIGH_SCORE = 0

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
        self.QUOTES = [
    "Success is not final, failure is not fatal: It is the courage to continue that counts. The key to growth is the introduction of higher dimensions of consciousness into our awareness, bringing forth wisdom and resilience in the face of life's challenges.",
    
    "Life is not measured by the number of breaths we take, but by the moments that take our breath away. Each day is a blank canvas, an opportunity to paint with the colors of hope, perseverance, and the courage to dream without limits.",
    
    "Twenty years from now, you will be more disappointed by the things you didn’t do than by the ones you did do. So throw off the bowlines, sail away from the safe harbor, and catch the trade winds in your sails. Explore. Dream. Discover.",
    
    "Happiness is not about getting everything you want; it’s about loving what you have and being grateful for it. Appreciate the beauty in small moments, the warmth of friendship, and the kindness we extend to others, for these are the true treasures of life.",
    
    "The only way to discover the limits of the possible is to go beyond them into the impossible. True growth comes from embracing the unknown, daring to step into unfamiliar terrain, and finding strength in vulnerability along the way.",
    
    "The purpose of life is not to be happy. It is to be useful, to be honorable, to be compassionate, to make a difference that you have lived and lived well. In doing so, we create a legacy that resonates in the hearts of those who follow.",
    
    "It is our choices that show what we truly are, far more than our abilities. In the face of adversity, it is our character, resilience, and willingness to rise that define our journey and ultimately illuminate the path forward.",
    
    "Don't watch the clock; do what it does. Keep going. Persistence is the vehicle you arrive in, fueled by determination and guided by purpose. Every small step, no matter how insignificant it may seem, contributes to the grand tapestry of achievement.",
    
    "We are what we repeatedly do. Excellence, then, is not an act, but a habit. Cultivate a daily practice of gratitude, kindness, and patience, for these small actions lay the foundation for a life of fulfillment and purpose.",
    
    "In the end, it's not the years in your life that count. It's the life in your years. Make each day count, finding joy in the journey, courage in the challenges, and meaning in the connections that weave together the story of who we are."
]



        #creating the highest score label 
        self.highest_score_label = Label(self.root, text=f"Highest Score: {self.read_text()} WPM ", font=("Times New Roman", 18, "bold"))
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
        
        # Canvas to display the text with wrapping enabled
        self.text_canvas = Canvas(self.root, bg="white", width=1200, height=200)
        self.text_canvas.grid(row=1, column=0, padx=10, pady=10, columnspan=7)
        
        # Display placeholder text with center alignment and wrapping
        self.demo_text = self.text_canvas.create_text(
            600, 100, text="Press Start Button to Begin.", font=("Times New Roman", 18, "bold"),
            width=1100, anchor="center", justify="center"  # Limit width and center-align text
        )

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

        # Get the current text of the start button
        self.start_text = self.start_button.cget("text")

        # Handle timer reset when restarting
        if self.start_text == "Restart" and self.repeat == 1:
            self.submit_text()

        # Change the start button text to "Restart"
        self.start_button.config(text="Restart")
        
        # Select a random quote from self.QUOTES for the typing test
        self.TEXT = random.choice(self.QUOTES)
        self.text_canvas.itemconfig(self.demo_text, text=self.TEXT)
        
        # Reset timer variables
        global TIME
        TIME = 60
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
        original_text = self.TEXT.strip()  # Original text
        typed_text = self.text_widget.get("1.0", END).strip()  # Typed text

        # Print the typed text for debugging purposes
        print("Typed text:", typed_text)

        # Calculate the total number of characters typed
        total_characters_typed = len(typed_text)

        # Initialize a counter for correct characters
        correct_characters = sum(1 for i in range(min(len(original_text), total_characters_typed))
                                if typed_text[i] == original_text[i])

        # Calculate accuracy as a percentage
        accuracy = (correct_characters / len(original_text)) * 100 if len(original_text) > 0 else 0
        return round(accuracy, 2)


    #TODO: METHOD TO WORK WHEN THE SUBBMIT BUTTON IS CLICKED
    def submit_text(self):
        # Calculate the WPM and accuracy
        wpm = self.calculate_wpm()
        accuracy = self.calculate_accuracy() 

        # Update the highest score if the current WPM is higher
        global HIGH_SCORE
        HIGH_SCORE = int(self.read_text())

        if wpm > HIGH_SCORE:
            HIGH_SCORE = wpm
            self.write_text(str(HIGH_SCORE))
            self.highest_score_label.config(text=f"Highest Score: {HIGH_SCORE} WPM")
        
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

    #methdod to read the text from the file
    def read_text(self):
        with open("DAY_86_TypingSpeedTestApp/assets/score.txt", "r") as file:
            text = file.read()
            return text
        
    #method to write the text to the file
    def write_text(self, text):
        with open("DAY_86_TypingSpeedTestApp/assets/score.txt", "w") as file:
            file.write(text)

            