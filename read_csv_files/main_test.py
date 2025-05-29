# with open("read_csv_files/weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

import csv


# data = []
# temps = []
# with open("read_csv_files/weather_data.csv") as file:
#     data = csv.reader(file)
#     for row in data:
#         if row[1] != "temp":
#             temps.append(int(row[1]))
# print(temps)

import pandas

data = pandas.read_csv("read_csv_files/weather_data.csv")

# print(data["temp"][0])


    
