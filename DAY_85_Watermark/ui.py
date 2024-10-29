from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

THEME_COLOR = "#375362"
FILENAME = None
IMG_HEIGHT = None
IMG_WIDTH = None

class UI:

    def __init__(self):
        super().__init__()
        self.root = Tk()
        self.root.title("Watermark")
        self.root.geometry('1200x700')
        self.root.config(padx=20, pady=20)
        self.image = None

        # Add text button
        self.add_text_button = Button(text="Add Text", width=10, height=2, font=("Times New Roman", 13, "bold"))
        self.add_text_button.grid(row=0, column=0)

        # Add logo button
        self.add_logo_button = Button(text="Add Logo", width=10, height=2, font=("Times New Roman", 13, "bold"))
        self.add_logo_button.grid(row=0, column=1)

        # Quit button
        self.quit_button = Button(text="Quit", command=self.quit, width=10, height=2, font=("Times New Roman", 13, "bold"))
        self.quit_button.grid(row=0, column=5)

        # Canvas for displaying images
        self.canvas = Canvas(width=1100, height=500, highlightthickness=0, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=6, padx=40, pady=20)

        # Placeholder text on canvas
        self.canvas.create_text(550, 250, text="Add an Image", font=("Times New Roman", 20, "bold"))

        # Add image button
        self.add_image_button = Button(text="Add Image", command=self.add_image, width=10, height=2, font=("Times New Roman", 13, "bold"))
        self.add_image_button.grid(row=2, column=0)

        # Cancel button
        self.cancel_button = Button(text="Cancel", width=10, height=2, font=("Times New Roman", 13, "bold"))
        self.cancel_button.grid(row=2, column=4)

        # Save button
        self.save_button = Button(text="Save", width=10, height=2, font=("Times New Roman", 13, "bold"))
        self.save_button.grid(row=2, column=5)

        # Start the Tkinter main loop
        self.root.mainloop()










#TODO: MEHTODS TO ADD TEXT
    def add_text(self):
        pass

    def add_logo(self):
        pass

#TODO: METHODS TO ADD IMAGE
   # Method to add an image to the canvas
    def add_image(self):
        FILENAME = filedialog.askopenfilename(initialdir="~/", title="Select File")
        if FILENAME:
            self.image = Image.open(FILENAME)
            IMG_WIDTH, IMG_HEIGHT = self.image.size
            
            # Resize the image to one-fourth of the original size
            resized_image = self.image.resize((IMG_WIDTH // 3, IMG_HEIGHT // 3), Image.LANCZOS)
            
            # Adjust canvas size to match the resized image size
            self.canvas.config(width=IMG_WIDTH // 3, height=IMG_HEIGHT // 3)

            # Set the root window size slightly larger than the canvas
            # self.root.geometry(f"{IMG_WIDTH // 3+ 100}x{IMG_HEIGHT // 3 + 150}")

            # Convert resized image to PhotoImage and store in instance attribute
            self.tk_image = ImageTk.PhotoImage(resized_image)
            
            # Display the image on the canvas
            self.canvas.create_image(0, 0, anchor='nw', image=self.tk_image)


    def save(self):
        pass



    def cancel(self):
        pass


    def quit(self):
        self.root.quit()


