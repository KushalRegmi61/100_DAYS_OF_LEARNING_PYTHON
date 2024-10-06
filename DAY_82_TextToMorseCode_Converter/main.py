"""Code to convert text to  morse code"""

#           ********     MORSE CODE CONVERTER   *********

a_list = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--',
          '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']

num_list = ['-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']

istring = input("Enter a String: ")

# converted text
ostring = ""

# Code to convert istring to morse code
for i in istring:
    if i.upper().isalpha():
        temp = ord(i.upper()) - 65
        ostring += a_list[temp] + " "
    elif i.isdigit():
        ostring += num_list[int(i)] + " "
    else:
        ostring += " "

# Output
print(f"Input Text: {istring}")
print(f"Output MorseCode:{ostring} ")
