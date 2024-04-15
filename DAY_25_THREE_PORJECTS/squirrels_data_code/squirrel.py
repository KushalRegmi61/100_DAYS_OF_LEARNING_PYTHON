import csv
import pandas
data = pandas.read_csv(r"DAY_25\squirrels_data_code\2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240402.csv")
grey_sq =len(data[data["Primary Fur Color"] == "Gray" ])
black_sq =len(data[data["Primary Fur Color"] == "Black" ])
cinnamon_sq =len(data[data["Primary Fur Color"] == "Cinnamon" ])

#creating the dict
dict= { 
       "Squirrel Color":["Grey", "Black", "Cinnamon"],
       "Count":[grey_sq, black_sq, cinnamon_sq]
       }
sq_data = pandas.DataFrame(dict)
print(sq_data)
sq_data.to_csv(r"DAY_25\squirrels_data_code\sq_color_&_count.csv")