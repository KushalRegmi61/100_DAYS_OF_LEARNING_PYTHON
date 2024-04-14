from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- GENERATE PASSWORD ------------------------------- #
#Password Generator Project
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for char in range( random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for char in range (random.randint(2, 4))]
    password_list = password_letters+password_symbols+ password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_name = web_link_entry.get()
    password = password_entry.get()
    email = username_entry.get()    
    if len(website_name)<5 or len(password)<4 or  len(email)<7:
        messagebox.showinfo(title="Retry!!!", message=f"\n information insufficient!!\n Please, Don't field empty")
    #opening the file to write the data
    else:
        #asking user to check the data before writing it to the file:
        user_choice =messagebox.askokcancel(title=f"Website:{website_name}", message=f"Email:{email} \n Password: {password}\n Do You Want to Save the data?")
        if user_choice:
            with open(r"DAY_29\password_data.txt", "a") as file:
                file.write(f"Website:{website_name} || Email:{email} || Password: {password}\n")
            web_link_entry.delete(0, END)
            password_entry.delete(0, END)    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)

# Provide the correct file path to the image
photo = PhotoImage(file=r"DAY_29\logo.png")

canvas = Canvas(window, height=200, width=200, highlightthickness=0)
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=0, columnspan=3)

# Label: Website
website_label = Label(window, text="Website:", font=("Times New Roman", 18))
website_label.grid(row=1, column=0)

# Entry: Enter the website link
web_link_entry = Entry(window, width=70)
web_link_entry.grid(row=1, column=1, columnspan=2)
web_link_entry.focus()

# Label: Email/Username
username_label = Label(window, text="Email/Username:", font=("Times New Roman", 18))
username_label.grid(row=2, column=0)


# Entry: Enter the username / email
username_entry = Entry(window, width=70)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "Hancy_BoY")

# Label: Password
password_label = Label(window, text="Password:", font=("Times New Roman", 18))
password_label.grid(row=3, column=0)

# Entry: Password Entry
password_entry = Entry(window, width=30)
password_entry.grid(row=3, column=1)

# Generate Password Button
generate_pass_button = Button(window, text="Generate Password", font=("Times New Roman", 11), command= generate_password)
generate_pass_button.grid(row=3, column=2)

# Add Button
add_button = Button(window, text="Add", font=("Times New Roman", 16), width=45, command= save_password)
add_button.grid(row=4, column=1, columnspan=2)

# Holding the main screen
window.mainloop()
