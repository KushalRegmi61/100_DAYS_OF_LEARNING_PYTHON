from tkinter import *
from tkinter import filedialog, messagebox
from gtts import gTTS
from PyPDF2 import PdfReader

# pdf_path = "DAY_91_Pdf-To-Audiobook/pdf_files/acknoledgement.pdf"

# # open the pdf file
# pdf = PdfReader(pdf_path)

# # variable to store the text
# text = ""

# # loop through the pages
# for page in pdf.pages:
#     text += page.extract_text()

# print(text)


# class  

# tts = gTTS('hello')
# tts.save('hello.mp3')

class PdfToAudiobook:
    def __init__(self):
        self.root = Tk()
        self.root.title("PDF to Audiobook")
        self.root.config(padx=50, pady=50) # padding
        self.root.geometry('500x500') # setting the size of the window

    #TODO: INITIALIZING THE VARIABLES
        self.text = ""
        self.file_path = ""
        self.audio_path = ""

    #TODO:   creating the labels and buttons 

        # Upload file button 
        self.upload_button = Button(self.root, text="Upload PDF", command=self.upload_pdf)
        self.upload_button.grid(row=0, column=0)

        # creating a canvas for the text
        self.text_canvas = Canvas(self.root, width=400, height=200)
        self.text_canvas.grid(row=1, column=0, columnspan=2)

        # adding the text to the canvas


        # Quit button
        self.quit_button = Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.grid(row=0, column=1)

        #  converting the pdf to audio
        self.convert_button = Button(self.root, text="Convert to Audio", command=self.save_audio)
        self.convert_button.grid(row=2, column=0, columnspan=2)

        # save audio button
        self.save_button = Button(self.root, text="Save Audio", command=self.save_audio)
        self.save_button.grid(row=3, column=0, columnspan=2)
    
        # runnig the app
        self.root.mainloop()

    #TODO: function to convert the pdf to audio
    def upload_pdf(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")], initialdir="/home/mr-kush/python/DAY_91_Pdf-To-Audiobook") # getting the file path
        if self.file_path:
            self.convert_pdf_to_audio() # converting the pdf to audio
        else:
            messagebox.showerror("Error", "No file selected") # error message if no file is selected

    #TODO: function to convert the pdf to audio
    def convert_pdf_to_audio(self):
        pdf = PdfReader(self.file_path) # open the pdf file
        self.text = "" # variable to store the text

        for page in pdf.pages: # loop through the pages
            self.text += page.extract_text()

        # creating the audio file
        self.tts = gTTS(self.text)
        # checkig if the audio file is created
        if self.tts:
            messagebox.showinfo("Success", "Audio file created successfully")
        else:
            messagebox.showerror("Error", "Audio file not created")

    # #TODO: saving the audio file
    # def save_audio(self):
    #     self.save_window = Toplevel() # creating a new window
    #     self.save_window.title("Save Audio")
    #     self.save_window.config(padx=50, pady=50)

    #     Label(self.save_window, text="Enter the name of the audio file").grid(row=0, column=0)
    #     self.audio_name = Entry(self.save_window)
    #     self.audio_name.grid(row=0, column=1)

    #     Button(self.save_window, text="Save", command=self.save_audio_file).grid(row=1, column=0, columnspan=2)
    
    #TODO: function to save the audio file
    def save_audio(self):
        self.audio_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")], initialdir="~/python/DAY_91_Pdf-To-Audiobook/Mp3") # getting the file path
        if self.audio_path:
            self.tts.save(self.audio_path)
            messagebox.showinfo("Success", "Audio file saved successfully")
        else:
            messagebox.showerror("Error", "Audio file not saved")

# running the app
PdfToAudiobook()