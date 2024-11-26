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
        self.text_widget = Text(self.root, font=("Times New Roman", 20), height=10, width=73, wrap=WORD, state=DISABLED)
        self.text_widget.insert("1.0", "Start typing here...")
        self.text_widget.grid(row=1, column=0, columnspan=7, pady=20 )
                   
        # setting up the time left label
        self.time_left = TIME
        self.time_label = Label(text=f"Time Left: {self.time_left} Sec", font=("Times New Roman", 18, "bold"), background="black", fg="white") # Time left label
        self.time_label.grid(row=2, column=0)

        # setting up the start button
        self.start_button = Button(text="Start", font=("Times New Roman", 20, "bold" ), command=self.start_game) # Start button
        self.start_button.grid(row=3, column=0, pady=50)

        # setting up the quit button 
        self.quit_button = Button(text="Quit", font=("Times New Roman", 20, "bold"), command=self.quit_game) # Quit button
        self.quit_button.grid(row=3, column=6, pady=50)




        # run the app
        self.root.mainloop()

    # function to start the game
    def start_game(self):
        self.time_left = TIME
        self.text_widget.config(state=NORMAL)
        self.text_widget.delete("1.0", END)

        # calling the reset_time_label function
        self.reset_time_label()


 
    # function to quit the game
    def quit_game(self):
        if  messagebox.askokcancel("Quit", "Do you want to quit the game?"):
            self.root.destroy()

    # function to display the timer for timer_label
    def display_timer(self):
        # start the timer for 0 sec and keep incrementing it by 1 sec
        pass

    # function to reset the time_label
    def reset_time_label(self):
        # reset the time_label to 10 sec
        self.time_left = TIME
        self.display_time_left()

    # function to update the time_label
    def display_time_left(self):
        """Update the time_label every second and handle countdown logic."""
        if self.time_left >= 0:
            self.time_label.config(text=f"Time Left: {self.time_left} Sec")
            self.time_left -= 1
            self.time_label.after(1000, self.display_time_left)
        else:
            messagebox.showinfo("Time's up", "Time's up! Start again...") # Display "Time's up" message
            
            # Stop the timer and display "Time's up" message
            self.time_label.config(text="Time Left: 0 Sec")
            self.text_widget.config(state="normal")  # Allow editing temporarily to insert message
            self.text_widget.delete("1.0", "end")  # Clear existing content

            # Insert "Time's up! Start again..." centered vertically and horizontally
            center_message = "Time's up! Start again..."
            self.text_widget.tag_config("center", justify="center")  # Center text horizontally

            # Calculate vertical centering by adding enough newlines
            num_lines = 10  # Adjust this value based on the height of your Text widget
            centered_text = "\n" * (num_lines // 2) + center_message
            self.text_widget.insert("1.0", centered_text, "center")  # Insert text with "center" tag

            # Highlight specific parts of the text
            self.text_widget.tag_add("start", f"{num_lines//2 + 1}.0", f"{num_lines//2 + 1}.9")  # "Time's up"
            self.text_widget.tag_config("start", foreground="red", font=("Times New Roman", 20, "bold"))
            self.text_widget.tag_add("again", f"{num_lines//2 + 1}.10", f"{num_lines//2 + 1}.22")  # "Start again"
            self.text_widget.tag_config("again", foreground="red", font=("Times New Roman", 20, "bold"))

            self.text_widget.config(state="disabled")  # Prevent further editing

            


    # function to update the score_label
            



        


