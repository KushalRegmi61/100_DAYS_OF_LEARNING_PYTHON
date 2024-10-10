def restart_game():
    for widget in window.winfo_children():
        if isinstance(widget, Button) and widget.cget("text") == " ":
            widget.config(text=" ")

restart_button = Button(text="Restart", font=("Times New Roman", 16, "bold"), command=restart_game)
restart_button.grid(row=4, column=1, padx=10, pady=10)
