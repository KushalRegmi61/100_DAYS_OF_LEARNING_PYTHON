import pandas as pd
data = pd.read_csv(r"DAY_26\nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format: {A:Alfa, B: Bravo}
nato_dict = { row.letter: row.code  for (index, row ) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter the user_choice:  ").upper()
code_list = {i: nato_dict[i] for i in user_input}
print(code_list)

