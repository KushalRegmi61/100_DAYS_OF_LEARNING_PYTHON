from tkinter import *
from tkinter import filedialog, messagebox, font
from PIL import Image, ImageTk, ImageDraw, ImageFont



# Global variables

THEME_COLOR = "#375362"
FILENAME = None
IMG_HEIGHT = None
IMG_WIDTH = None
IS_SAVED = True
TEXT = ""
FONT_PROPERTIES = []
TEXT_COLOR = "black"
x = 0
y = 0
h_multiplier = 1
w_multiplier = 1







class UI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Watermark")
        self.root.geometry('1200x700')
        self.root.config(padx=20, pady=20)
        self.image = None


        #Adding fonts
        self.FONTS = {
                "Comic Sans MS": "DAY_85_Watermark/Fonts/ComicSansMS.ttf",
                "CatShop": "DAY_85_Watermark/Fonts/CatShop.ttf",
                "FunkySignature": "DAY_85_Watermark/Fonts/FunkySignature.ttf",
                "LissainDidone": "DAY_85_Watermark/Fonts/LissainDidone.ttf",
                "NewSushi": "DAY_85_Watermark/Fonts/NewSushi.ttf",
            }

        # Add text button
        self.add_text_button = Button(text="Add Text", width=10, height=2, font=("Times New Roman", 13, "bold"), command=self.add_text)
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
        self.canvas.create_text(550, 250, text="Add an Image", font=("Times New Roman", 20, "bold"))

        self.create_text()

        self.start_x = 0
        self.start_y = 0
        
   
        # Add image button
        self.add_image_button = Button(text="Add Image", command=self.add_image, width=10, height=2, font=("Times New Roman", 13, "bold"))
        self.add_image_button.grid(row=2, column=0)

        # Preview Image button
        self.preview_button = Button(text="Preview IMG", width=10, height=2, font=("Times New Roman", 13, "bold"), command=self.preview)
        self.preview_button.grid(row=2, column=1)

        # Cancel button
        self.cancel_button = Button(text="Cancel", width=10, height=2, font=("Times New Roman", 13, "bold"), command=self.cancel)
        self.cancel_button.grid(row=2, column=4)

        # Save button
        self.save_button = Button(text="Save", width=10, height=2, font=("Times New Roman", 13, "bold"), command=self.save)
        self.save_button.grid(row=2, column=5)




        # Start the Tkinter main loop
        self.root.mainloop()

#TODO: Method to create text on the canvas
    def create_text(self):
                #creating a canvas for logo
        self.logo_text = self.canvas.create_text(
                                    100,
                                    100,
                                    width=200, 
                                    fill="black",
                                   )
        
        # self.logo_img = self.canvas.create_image(
        #                             550,
        #                             250,
        #                             anchor='nw',
        #                             image=self.logo_text    
        #                             )


        # Bind mouse events for moving the logo text
        self.canvas.tag_bind(self.logo_text, '<ButtonPress-1>', self.on_button_press)
        self.canvas.tag_bind(self.logo_text, '<B1-Motion>', self.on_mouse_drag)
        self.canvas.tag_bind(self.logo_text, '<ButtonRelease-1>', self.on_button_release)   

#TODO: Add functionality to add text to the canvas
    def add_text(self):
        self.text_window = Toplevel()
        self.text_window.geometry("400x400")
        self.text_window.config(padx=20, pady=20)

        # Label and entry for text input
        Label(self.text_window, text="Enter Text:", font=("Times New Roman", 15, "bold")).grid(row=0, column=0)
        self.entry = Entry(self.text_window, font=("Times New Roman", 15, "bold"))
        self.entry.grid(row=0, column=1, padx=10)

        # Dropdown menu to select the font family
        Label(self.text_window, text="Select Font Family", font=("Times New Roman", 12, "bold")).grid(row=1, column=0)

        self.font_family = list(self.FONTS.keys())  # Use custom font family names

        self.selected_font_family = StringVar(value=self.font_family[0])
        self.font_family_menu = OptionMenu(self.text_window, self.selected_font_family, *self.font_family)
        self.font_family_menu.grid(row=1, column=1, pady=10, padx=10)

        # Scale widget for font size selection
        Label(self.text_window, text="Select Font Size", font=("Times New Roman", 12, "bold")).grid(row=2, column=0)
        self.font_size = Scale(self.text_window, from_=0, to=100, orient=HORIZONTAL)
        self.font_size.set(12)  # Default size
        self.font_size.grid(row=2, column=1, padx=10, pady=10)

        # Dropdown menu to select font color
        Label(self.text_window, text="Select Font Color", font=("Times New Roman", 12, "bold")).grid(row=4, column=0)
        self.font_color = StringVar(value="black")
        color_options = ["black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "white"]
        self.font_color_menu = OptionMenu(self.text_window, self.font_color, *color_options)
        self.font_color_menu.grid(row=4, column=1, pady=10, padx=10)

        # Button to apply text properties to the main canvas
        self.apply_button = Button(self.text_window, text="Apply", font=("Times New Roman", 15, "bold"), command=self.apply_text)
        self.apply_button.grid(row=5, column=0, pady=10)

        # Button to cancel the text window
        self.cancel_button = Button(self.text_window, text="Close", font=("Times New Roman", 15, "bold"), command=self.text_window.destroy)
        self.cancel_button.grid(row=5, column=1, pady=10)


#TODO: Add functionality to apply the selected text properties to the canvas
    def apply_text(self):
        global TEXT, FONT_PROPERTIES, TEXT_COLOR
        TEXT = self.entry.get()
        
        # Changing the Add Text button label when the text is added
        if TEXT:
            self.add_text_button.config(text="Edit Text")
            self.text_window.title("Edit Text")

        else:
            self.add_text_button.config(text="Add Text")
            self.text_window.title("Add Text")

        FONT_PROPERTIES = [self.selected_font_family.get(), self.font_size.get()]
        TEXT_COLOR = self.font_color.get()

        # Load the selected custom font
        font_path = self.FONTS[FONT_PROPERTIES[0]]
        font = ImageFont.truetype(font_path, FONT_PROPERTIES[1])  # This will ensure the font is loaded correctly

        # Update canvas text to use custom font
        self.canvas.itemconfig(self.logo_text, text=TEXT, font=(FONT_PROPERTIES[0], FONT_PROPERTIES[1]), fill=TEXT_COLOR)

#TODO: Add functionality to add a logo to the canvas
    def add_logo(self):
        pass

#TODO: Method to add an image as the background of the canvas
    def add_image(self):
        global FILENAME, IMG_HEIGHT, IMG_WIDTH, h_multiplier, w_multiplier, IS_SAVED
        IS_SAVED = False
        FILENAME = filedialog.askopenfilename(initialdir="~/", title="Select File")
        if FILENAME:
            # Open the selected image
            self.opened_image = Image.open(FILENAME)

            # Create a drawing context for the opened image
            self.draw = ImageDraw.Draw(self.opened_image)

            self.image = Image.open(FILENAME)
            IMG_WIDTH, IMG_HEIGHT = self.image.size

            # Set maximum dimensions for the canvas
            max_canvas_width = 1100  # Set maximum width for the canvas
            max_canvas_height = 500   # Set maximum height for the canvas

            # Calculate the aspect ratio of the image
            aspect_ratio = IMG_WIDTH / IMG_HEIGHT

            # Calculate new dimensions while respecting the aspect ratio and maximum sizes
            if aspect_ratio > 1:  # Landscape orientation
                new_width = min(max_canvas_width, IMG_WIDTH)
                new_height = int(new_width / aspect_ratio)
                if new_height > max_canvas_height:
                    new_height = max_canvas_height
                    new_width = int(new_height * aspect_ratio)
            else:  # Portrait orientation or square
                new_height = min(max_canvas_height, IMG_HEIGHT)
                new_width = int(new_height * aspect_ratio)
                if new_width > max_canvas_width:
                    new_width = max_canvas_width
                    new_height = int(new_width / aspect_ratio)

            # Calculate the multipliers for resizing the image
            h_multiplier = IMG_HEIGHT / new_height
            w_multiplier = IMG_WIDTH / new_width

            # Resize the image to maintain the aspect ratio
            resized_image = self.image.resize((new_width, new_height), Image.LANCZOS)

            # Clear any existing content on the canvas
            self.canvas.delete("all")

            # Adjust canvas size to match the resized image size
            self.canvas.config(width=new_width, height=new_height)

            # Convert resized image to PhotoImage and store in instance attribute
            self.tk_image = ImageTk.PhotoImage(resized_image)

            # Display the image on the canvas as the background
            self.canvas.create_image(0, 0, anchor='nw', image=self.tk_image)

            # Adjust the main window size to fit the resized image size
            # self.root.pack_propagate(False)  # Prevent window from resizing to the canvas size
            # self.root.update_idletasks()  # Ensure all geometry requests are processed

            # # Set window size with padding
            # window_width = new_width + 50 # Add padding
            # window_height = new_height + 100 # Add padding
            # self.root.geometry(f"{window_width}x{window_height}")

            # # Optionally center the window on the screen
            # x = (self.root.winfo_screenwidth() // 2) - (window_width // 2)
            # y = (self.root.winfo_screenheight() // 2) - (window_height // 2)
            # self.root.geometry(f"+{x}+{y}")

            # # Force a refresh to apply changes
            # self.root.update()

            # print(f"New Width: {new_width}, New Height: {new_height}")


#TODO: Add functionality to save the canvas content as an image file

    def save(self):

        # Font setup for the text
        # font_family = f"fonts/{FONT_PROPERTIES[0].lower().replace(' ', '_')}.ttf"  # Convert to lowercase, handle spaces
        font_family = self.FONTS.get(FONT_PROPERTIES[0])
        print(h_multiplier, w_multiplier)

        # Calculate the font size based on the canvas and image dimensions
        # Use the actual dimensions of the resized image
        # Calculate the font size based on the canvas and image dimensions
        font_size = int(FONT_PROPERTIES[1] * (h_multiplier if h_multiplier> w_multiplier else w_multiplier) * .75)

        try:
            # Load the font
            font = ImageFont.truetype(font_family, font_size)
        except IOError:
            messagebox.showerror("Error", f"Font file '{font_family}' not found.")
            return

        # Set x and y coordinates for the text position
        # Calculate the coordinates for the text position on the original image
        x_cor = int(x * w_multiplier)
        y_cor = int(y * h_multiplier)

        # Draw the text on the image
        self.draw.text((x_cor, y_cor), TEXT, fill=TEXT_COLOR, font=font)

        # Create a window to prompt the user to enter a filename for saving
        save_window = Toplevel()
        save_window.geometry("300x200")
        save_window.config(padx=20, pady=20)
        save_window.title("Save Image")

        Label(save_window, text="Enter Filename:", font=("Times New Roman", 12, "bold")).pack(pady=10)
        filename_entry = Entry(save_window, font=("Times New Roman", 12, "bold"))
        filename_entry.pack(pady=5)

        def save_image():
            # Get the filename from the entry field
            filename = filename_entry.get()
            if filename:
                # Open file dialog for saving the image
                save_path = filedialog.asksaveasfilename(
                    defaultextension=".png", initialfile=filename,
                    filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
                )
                if save_path:
                    # Save the image to the selected path
                    self.opened_image.save(save_path)
                    global IS_SAVED
                    IS_SAVED = True
                    save_window.destroy()
                    messagebox.showinfo("Success", "Image saved successfully!")
                else:
                    messagebox.showwarning("Warning", "Please select a location to save the file.")
            else:
                messagebox.showwarning("Warning", "Please enter a filename.")

        # Button to trigger the save operation
        Button(save_window, text="Save", font=("Times New Roman", 12, "bold"), command=save_image).pack(pady=10)

#TODO: Add functionality to preview the image with the watermark
    def preview(self):
        self.opened_image.show()


#TODO: Add functionality to cancel the changes made to the canvas
    def cancel(self):
        if messagebox.askokcancel("Cancel", "Are you sure you want to cancel the changes?"):
            self.canvas.delete("all")
            self.canvas.config(width=1100, height=500)
            TEXT = ""
            self.canvas.create_text(550, 250, text="Add an Image", font=("Times New Roman", 20, "bold"))

#TODO: Add functionality to quit the application
    def quit(self):
        if IS_SAVED:
            self.root.quit()
        else:
            if messagebox.askokcancel("Quit", "You have not saved the image. Do you want to quit?"):
                self.root.quit()
      
#TODO: Add functionality to move the logo text on the canvas
    def on_button_press(self, event):
        # Store the current mouse position
        self.start_x = event.x
        self.start_y = event.y

    def on_mouse_drag(self, event):
        # Calculate the distance moved
        dx = event.x - self.start_x
        dy = event.y - self.start_y

        # Move the logo text by the calculated distance
        self.canvas.move(self.logo_text, dx, dy)

        # Update the start positions for the next motion event
        self.start_x = event.x
        self.start_y = event.y

    def on_button_release(self, event):
        global x, y
        # Get the current position of the logo_text after release
        x, y = self.canvas.coords(self.logo_text)  # Get the current coordinates of logo_text
        print(f"Logo text released at: ({x}, {y})")  # Print or log the coordinates
