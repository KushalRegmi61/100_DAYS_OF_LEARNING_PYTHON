with open(r"DAY_24\Input\Names\invited_names.txt") as invited_names: #opening 
    names = invited_names.readlines()    
# #creating a function to repalce the letter name
def replace_name(name):
    with open(r"DAY_24\Input\Letters\starting_letter.txt") as letter:
        text = letter.read().strip()
        return text.replace("[name]", name)  
         
#creating files to send letters
for name in names:
    name = name.strip() #removing whitespaces from varible name
    letter = replace_name(name)
#creating .txt file for individual name letter
    with open(f"DAY_24\\Output\\letter_for_{name}.txt", mode = "w") as file:
        file.write(letter)
        
