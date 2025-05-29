import pandas

data = pandas.read_csv("read_csv_files/weather_data.csv")

data_dict = data.to_dict()
print(data)

temp_list = data["temp"]
print(temp_list)

print(data["temp"].mean())

print(data["temp"].max())

print(data[data.day == "Monday"])

print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]

print(monday.temp*9/5 + 32)


student_dict = {
    "student": ["Amy", "James", "Angela"],
    "score": [76, 56, 65]
}

student_data = pandas.DataFrame(student_dict)
student_data_csv = student_data.to_csv("read_csv_files/new_data.csv")
print(student_data)