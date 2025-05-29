import pandas


data = pandas.read_csv("read_csv_files/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250526.csv")

# print(data["Primary Fur Color"].value_counts())

# data["Primary Fur Color"].value_counts().to_csv("read_csv_files/squirrel_count.csv")

black_squirrels = data[data["Primary Fur Color"] == "Black"]
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]  
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
squirrel_count = {
    "Fur Color": ["Black", "Gray", "Cinnamon"],
    "Count": [len(black_squirrels), len(gray_squirrels), len(red_squirrels)]
}

squirrel_count_df = pandas.DataFrame(squirrel_count)
squirrel_count_df.to_csv("read_csv_files/squirrel_count2.csv")