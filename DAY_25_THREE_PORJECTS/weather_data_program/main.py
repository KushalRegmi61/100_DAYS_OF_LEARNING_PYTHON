import csv
import pandas
data = pandas.read_csv(r"DAY_25_THREE_PORJECTS\weather_data_program\weather_data.csv")
print(data["temp"].mean())

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.temp * 9/5 + 32)
std_data = {
    "Name": [ "kushal ", "Aditya"," chandan"],
    "Roll No":[42, 11, 23],
    "Rank":[77, 17, 15]
    }
data = pandas.DataFrame(std_data)
print(data)
data.to_csv(r"DAY_25_THREE_PORJECTS\weather_data_program\std_data.csv")