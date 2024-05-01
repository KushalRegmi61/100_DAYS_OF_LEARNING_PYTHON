import tkinter as tk
from tkinter import messagebox
import math
from quiz_brain import QuizBrain  # Import QuizBrain from quiz_brain module

TIMER = None
START_TIME =0
THEME_COLOR = "#375362"

class Quizui():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.q_list = None
        self.window = tk.Tk()
        self.window.title("....Quiz_Brain....")
        self.window.config(padx=30, pady=30, bg=THEME_COLOR)

        # Adding Time Label to the screen
        self.timer = tk.Label(
            text="Time_Taken : 00:00",
            font=("Times New Roman", 25, "italic"),
            fg="white",
            bg=THEME_COLOR
        )
        self.timer.grid(row=0, column=2)

        # Adding score label to the screen
        self.score_label = tk.Label(
            text="Score: 0",
            font=("Times New Roman", 25, "italic"),
            fg="white",
            bg=THEME_COLOR
        )
        self.score_label.grid(row=1, column=6)

        # Creating the canvas
        self.canvas = tk.Canvas(self.window, height=200, width=700, highlightthickness=0)

        # Adding canvas widget to the screen
        self.canvas.grid(row=2, column=2, columnspan=5, pady=30)

        # Creating question label on the canvas
        self.question_text = self.canvas.create_text(
            350,
            100,
            width=680,
            text="Some Question",
            font=("Times New Roman", 20, "bold"),
            fill=THEME_COLOR
        )

        # Adding restart button to the screen
        self.start_button = tk.Button(
            text="Start",
            font=("Times New Roman", 20, "italic"),
            fg=THEME_COLOR,
            command=self.start_game
        )
        self.start_button.grid(row=1, column=2, columnspan=3)

        # Adding Exit button to the screen
        self.exit_button = tk.Button(
            text="Exit",
            font=("Times New Roman", 20, "italic"),
            fg=THEME_COLOR,
            command=self.exit_game
        )
        self.exit_button.grid(row=1, column=5, columnspan=1)

        # Creating True and False buttons
        self.true_img = tk.PhotoImage(file=r"DAY_34/images/true.png")
        self.false_img = tk.PhotoImage(file=r"DAY_34/images/false.png")
        self.false_button = tk.Button(
            image=self.false_img,
            highlightthickness=0,
            command=self.wrong_answer
        )

        self.false_button.grid(row=3, column=2, columnspan=2)
        self.true_button = tk.Button(
            image=self.true_img,
            highlightthickness=0,
            command=self.correct_answer
        )
        self.true_button.grid(row=3, column=6)

        # Initially deactivating the button Such that button will work only when Start button is pressed
        self.false_button.config(state="disabled")
        self.true_button.config(state="disabled")

        # creating the window mainloop
        self.window.mainloop()

    # method to display another question the screen
    def another_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score:{self.quiz.score} / {self.quiz.question_number}")
            self.question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=self.question)
        else:
            self.canvas.itemconfig(self.question_text, text="The Quiz Completed")
            self.score_label.config(text=f"Final Score: {self.quiz.score} / 20")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")
            self.start_button.config(text="Play Again!")

    # method to check the user Answer Whether True/ False
    def correct_answer(self):
        self.answer = self.quiz.check_answer("True")
        self.feedback(self.answer)

    def wrong_answer(self):
        self.answer = self.quiz.check_answer("False")
        self.feedback(self.answer)

    # give feedback to user answer
    def feedback(self, answer):
        if answer:
            # turn the screen green if the user guess is correct
            self.canvas.configure(bg="green")
            self.window.after(1000, self.another_question)

        else:
            # turn the screen  if the user guess is incorrect
            self.canvas.configure(bg="red")
            self.window.after(2000, self.another_question)

    # adding method for start button
    # Method to start the game
    def start_game(self):
        self.display_time(START_TIME)  # Start the timer
        self.start_button.config(text="Restart")  # Change the text of the Start button
        self.quiz.score = 0  # Reset the score
        self.quiz.question_number = 0  # Reset the question number
        self.quiz.new_qlist()  # Fetch new questions and assign them to self.quiz.question_list
        self.another_question()  # Start displaying questions
        self.false_button.config(state="active")  # Activate the False button
        self.true_button.config(state="active")  # Activate the True button
        

    # Method to handle exit functionality
    def exit_game(self):
        # Display final score
        final_score_message = f"Final Score: {self.quiz.score} / {self.quiz.question_number}"
        messagebox.showinfo(title="Final Score", message=final_score_message)
        # Close tkinter window
        self.window.destroy()

    # method to calculate the time
    def display_time(self, count):
        global TIMER
        min = math.floor(count / 60)
        sec = count % 60
        if sec > 9:
            self.timer.config(text=f"Time_Taken: {min}:{sec}")
        else:
            self.timer.config(text=f"Time_Taken: {min}:0{sec}")
        TIMER = self.window.after(1000, self.display_time, count + 1)  # fix the errors
