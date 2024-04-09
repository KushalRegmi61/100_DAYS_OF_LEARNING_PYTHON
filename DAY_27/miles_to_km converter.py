from tkinter import *
window = Tk()
window.title("Miles_To_KM_Converter")
# window.geometry("500x300")
window.config(padx= 40)

#entry
input = Entry(width= 15)
input.grid(row = 2, column= 2)

#label_1
label_1 = Label(text="Miles", font=("Times New Roman", 25, "italic"))
label_1.grid( row=2, column=3)
# label.config(padx= 15, pady= 15)

#label_2 
label_2 = Label(text=f"Is equal  to ", font=("Times New Roman", 25, "italic"))
label_2.grid( row=4, column=0)

#label_3 
label_3 = Label(text=f"KM", font=("Times New Roman", 25, "italic"))
label_3.grid( row=4, column=3)    

#label_4
label_4 = Label(text=f"0", font=("Times New Roman", 25, "italic"))
label_4.grid( row=4, column=2)  
def button_click():
    mile = input.get()
    label_4.config(text = int(mile) * 1.6)


  

#button_1  
button = Button(text="Calculate",font=("Times New Roman", 15, "italic") ,command= button_click)  
button.config()  
button.grid(row=6, column= 2)  







 



window.mainloop()
