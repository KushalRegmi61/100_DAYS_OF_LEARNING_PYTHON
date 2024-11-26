from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
import os

# Global variables
TIME = 5
HIGHSCORE = 0


class TextDisappearingApp:
    def __init__(self):
        self.root = Tk()

        # Setting up the window
        self.root.title("Text Disappearing App")
        self.root.geometry("1000x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        # Load high score
        self.load_high_score()

        # Configure grid layout for proper alignment
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)

        # Score Label
        self.score = 0
        self.score_label = Label(
            text=f"Score: {self.score}",
            font=("Times New Roman", 20, "bold"),
            fg="#333333",
            bg="#f0f0f0",
        )
        self.score_label.grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=10)

        # High Score Label
        self.high_score_label = Label(
            text=f"High Score: {HIGHSCORE}",
            font=("Times New Roman", 20, "bold"),
            fg="#333333",
            bg="#f0f0f0",
        )
        self.high_score_label.grid(row=0, column=1, columnspan=2, sticky="e", padx=10, pady=10)



        # Text Widget
        self.text_widget = Text(
            self.root,
            font=("Times New Roman", 18),
            height=12,
            width=70,
            wrap=WORD,
            relief=GROOVE,
            borderwidth=2,
        )
        self.text_widget.insert("1.0", "Start typing here...")
        self.text_widget.config(state=DISABLED)
        self.text_widget.grid(row=1, column=0, columnspan=5, padx=20, pady=20)

        # Time Left Label
        self.time_left = TIME
        self.time_label = Label(
            text=f"Time Left: {self.time_left} Sec",
            font=("Times New Roman", 18, "bold"),
            bg="#000000",
            fg="#FFFFFF",
        )
        self.time_label.grid(row=3, column=0, columnspan=2,sticky="e", padx=10, pady=10)

        # Progress Bar
        self.progress = Progressbar(
            self.root, orient=HORIZONTAL, length=500, mode="determinate"
        )
        self.progress.grid(row=3, column=1, columnspan=5, pady=10)

        # Start Button
        self.start_button = Button(
            text="Start",
            font=("Times New Roman", 20, "bold"),
            command=self.start_game,
        )
        self.start_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Quit Button
        self.quit_button = Button(
            text="Quit",
            font=("Times New Roman", 20, "bold"),
            command=self.quit_game,
        )
        self.quit_button.grid(row=4, column=4, columnspan=2, pady=10)

        # Dark Mode Toggle
        self.dark_mode = False
        self.toggle_button = Button(
            text="Toggle Theme",
            font=("Times New Roman", 16),
            command=self.toggle_theme,
        )
        self.toggle_button.grid(row=0, column=3, sticky="e", padx=20)

        # Run the app
        self.root.mainloop()

    def start_game(self):
        """Start the game and reset necessary components."""
        self.time_left = TIME
        self.score = 0
        self.update_score_label()
        self.text_widget.config(state=NORMAL)
        self.text_widget.delete("1.0", END)
        self.text_widget.focus()
        self.reset_time_label()
        self.display_time_left()
        self.text_widget.bind("<KeyPress>", self.reset_time_label)
        self.start_button.config(state=DISABLED)  # Disable start button during the game

    def quit_game(self):
        """Exit the app after confirmation."""
        if messagebox.askokcancel("Quit", "Do you want to quit the game?"):
            self.root.destroy()

    def reset_time_label(self, event=None):
        """Reset the timer when a key is pressed."""
        self.time_left = TIME

    def display_time_left(self):
        """Update the time left and manage countdown logic."""
        self.time_label.config(text=f"Time Left: {self.time_left} Sec")
        self.progress["value"] = TIME - self.time_left  # Update the progress bar
        
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.after(950, self.display_time_left)  # Slightly less than 1 second
        else:
            self.end_game()


    def end_game(self):
        """End the game and update high score if applicable."""
        self.text_widget.unbind("<KeyPress>")
        self.text_widget.config(state=DISABLED)
        messagebox.showinfo("Time's Up!", "Time's up! Game over.")
        self.update_high_score()
        self.start_button.config(state=NORMAL)  # Re-enable start button

    def update_score_label(self):
        """Update the score label."""
        self.score_label.config(text=f"Score: {self.score}")

    def update_high_score(self):
        """Check and update the high score."""
        global HIGHSCORE
        if self.score > HIGHSCORE:
            HIGHSCORE = self.score
            self.high_score_label.config(text=f"High Score: {HIGHSCORE}")
            with open("highscore.txt", "w") as file:
                file.write(str(HIGHSCORE))

    def load_high_score(self):
        """Load the high score from file."""
        global HIGHSCORE
        if os.path.exists("highscore.txt"):
            with open("highscore.txt", "r") as file:
                HIGHSCORE = int(file.read())

    def toggle_theme(self):
        """Switch between light and dark themes."""
        self.dark_mode = not self.dark_mode
        if self.dark_mode:
            self.root.config(bg="#333333")
            self.score_label.config(bg="#333333", fg="#FFFFFF")
            self.high_score_label.config(bg="#333333", fg="#FFFFFF")
            self.time_label.config(bg="#333333", fg="#FFFFFF")
            self.text_widget.config(bg="#555555", fg="#FFFFFF")
        else:
            self.root.config(bg="#f0f0f0")
            self.score_label.config(bg="#f0f0f0", fg="#333333")
            self.high_score_label.config(bg="#f0f0f0", fg="#333333")
            self.time_label.config(bg="#000000", fg="#FFFFFF")
            self.text_widget.config(bg="#FFFFFF", fg="#000000")



