from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
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
    new_data = {
        website_name.title(): {
            "Email/UserName": email,  # Remove colon from key names
            "Password": password  # Remove colon from key names
        }
    }

    if len(website_name) < 4 or len(password) < 4 or len(email) < 7:
        messagebox.showinfo(title="Retry!!!", message=f"\nInformation insufficient!!\nPlease don't leave fields empty.")
    else:
        user_choice = messagebox.askokcancel(title=website_name, message=f"Email:{email} \n Password: {password}\n Do You Want to SAVE THE DATA?")
        if user_choice:
            # Opening the file to load json data
            try:
                with open("DAY_29_&_30_Password_Manager_App\data.json", "r") as data_file: 
                    data = json.load(data_file)
                    
                    
            except  FileNotFoundError:
            #dumping the updated data
                    with open("DAY_29_&_30_Password_Manager_App\data.json", "w") as data_file: 
                        json.dump(new_data, data_file, indent=4)  
            else:
                data.update(new_data)#updating the data
                with open("DAY_29_&_30_Password_Manager_App\data.json", "w") as data_file: 
                    json.dump(data, data_file, indent=4)  
            finally:                   
        # Clear input fields after data is saved
                web_link_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    try:
        with open(r"DAY_29_&_30_Password_Manager_App\data.json", "r") as data_fie:
            data = json.load(data_fie)
    
    except FileNotFoundError as error_message:
        messagebox.showinfo(title=error_message, message="No Data file found.... :(")
   
    else:
        web_name = web_link_entry.get().title()
        if web_name in data.keys():
            messagebox.showinfo(title=f"Website Name: {web_name}", message=f"Email/UserName: {data[web_name]['Email/UserName']}\n Passowrd: {data[web_name]['Password']}")
        else:
            messagebox.showinfo(title="KeyError", message= "No Details for the website exists!! :(")
                
   
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager!!!")
window.config(padx=50, pady=50)

# Provide the correct file path to the image
photo = PhotoImage(file=r"DAY_29_&_30_Password_Manager_App\logo.png")

canvas = Canvas(window, height=200, width=200, highlightthickness=0)
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=0, columnspan=3)

# Label: Website
website_label = Label(window, text="Website:", font=("Times New Roman", 20))
website_label.grid(row=1, column=0)

# Entry: Enter the website link
web_link_entry = Entry(window, width=45)
web_link_entry.grid(row=1, column=1, columnspan=1)
web_link_entry.focus()

#Search WEbsite button
search = Button(window, text="Search", font=("Times New Roman", 15), width= 10, command= find_password)
search.grid(row= 1, column= 2 )

# Label: Email/Username
username_label = Label(window, text="Email/Username:", font=("Times New Roman", 15))
username_label.grid(row=2, column=0)


# Entry: Enter the username / email
username_entry = Entry(window, width=69)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "Hancy_BoY")

# Label: Password
password_label = Label(window, text="Password:", font=("Times New Roman", 15))
password_label.grid(row=3, column=0)

# Entry: Password Entry
password_entry = Entry(window, width=45)
password_entry.grid(row=3, column=1)

# Generate Password Button
generate_pass_button = Button(window, text="Generate Password", font=("Times New Roman", 12), command= generate_password)
generate_pass_button.grid(row=3, column=2)

# Add Button
add_button = Button(window, text="Add", font=("Times New Roman", 12), width=45, command= save_password)
add_button.grid(row=4, column=1, columnspan=2)

# Holding the main screen
window.mainloop()
